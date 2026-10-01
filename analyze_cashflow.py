import os
import sys
import time
import re
import argparse
from datetime import datetime, timezone
import requests
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv

# Tai cac bien moi truong tu tep .env
load_dotenv()

# Ham lay danh sach API Key tu bien moi truong
def get_etherscan_api_keys() -> list[str]:
    keys = []
    # Kiem tra bien ETHERSCAN_API_KEY tieu chuan
    main_key = os.getenv("ETHERSCAN_API_KEY")
    if main_key and main_key.strip():
        keys.append(main_key.strip())
    
    # Kiem tra cac bien danh so ETHERSCAN_API_KEY_1, _2, _3
    for i in range(1, 10):
        k = os.getenv(f"ETHERSCAN_API_KEY_{i}")
        if k and k.strip() and k.strip() not in keys:
            keys.append(k.strip())
            
    return keys

# Ham kiem tra dinh dang dia chi vi Ethereum hop le
def validate_eth_address(address: str) -> bool:
    if not address:
        return False
    # Kiem tra chuoi 42 ky tu bat dau bang 0x
    return bool(re.match(r"^0x[a-fA-F0-9]{40}$", address.strip()))

# Ham lay so thu tu block tai thoi diem bat dau de toi uu hoa truy van
def get_start_block_by_time(timestamp: int, api_key: str, chain_id: int = 1) -> int:
    url = "https://api.etherscan.io/v2/api"
    params = {
        "chainid": chain_id,
        "module": "block",
        "action": "getblocknobytime",
        "timestamp": timestamp,
        "closest": "before",
        "apikey": api_key
    }
    try:
        response = requests.get(url, params=params, timeout=15)
        # Luon kiem tra ma trang thai phan hoi truoc khi xu ly
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "1" and data.get("result"):
                return int(data.get("result"))
    except Exception:
        # Neu co su co thi tra ve block 0 de fallback
        pass
    return 0

# Ham goi API Etherscan de lay lich su giao dich
def fetch_normal_transactions(address: str, api_keys: list[str], days: int = 90, chain_id: int = 1) -> list[dict]:
    if not api_keys:
        print("[LOI] Khong tim thay ETHERSCAN_API_KEY trong tep .env.")
        print("[HUONG DAN] Vui long kiem tra lai tep .env va khai bao ETHERSCAN_API_KEY hoac ETHERSCAN_API_KEY_1.")
        sys.exit(1)

    target_address = address.strip().lower()
    current_time = int(time.time())
    start_timestamp = current_time - (days * 86400)
    
    key_index = 0
    current_key = api_keys[key_index]
    
    print(f"[*] Bat dau thu thap giao dich cho vi: {address}")
    start_dt_str = datetime.fromtimestamp(start_timestamp, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    print(f"[*] Pham vi thoi gian: {days} ngay gan nhat (tu {start_dt_str}, timestamp: {start_timestamp})")
    
    # Xac dinh startblock de chi truy van cac block trong ky 90 ngay
    start_block = get_start_block_by_time(start_timestamp, current_key, chain_id=chain_id)
    if start_block > 0:
        print(f"[*] Xac dinh block khoi dau: {start_block}")
    else:
        print("[*] Khong xac dinh duoc block khoi dau, quet tu block 0...")

    all_transactions = []
    page = 1
    offset = 10000 # Han muc theo quy dinh tai SPEC.md
    
    while True:
        # Su dung Etherscan API V2 theo tieu chuan hien hanh
        url = "https://api.etherscan.io/v2/api"
        params = {
            "chainid": chain_id,
            "module": "account",
            "action": "txlist",
            "address": address,
            "startblock": start_block,
            "endblock": 99999999,
            "page": page,
            "offset": offset,
            "sort": "asc",
            "apikey": current_key
        }
        
        try:
            # Gui yeu cau toi Etherscan API
            response = requests.get(url, params=params, timeout=25)
        except requests.exceptions.RequestException as e:
            print(f"[LOI] Loi ket noi mang khi goi API Etherscan: {e}")
            sys.exit(1)
            
        # Quy tac AGENTS.md: Luon kiem tra ma trang thai phan hoi truoc khi xu ly du lieu
        if response.status_code != 200:
            print(f"[LOI] Etherscan API tra ve ma trang thai HTTP: {response.status_code}")
            sys.exit(1)
            
        try:
            res_json = response.json()
        except Exception as e:
            print(f"[LOI] Khong the doc du lieu JSON tu phan hoi API: {e}")
            sys.exit(1)
            
        status = res_json.get("status")
        message = res_json.get("message")
        result = res_json.get("result")
        
        # Truong hop ngoai le E1: Neu API tra ve danh sach rong
        if status == "0" and message == "No transactions found":
            if page == 1:
                print("Vi khong co giao dich trong ky")
                sys.exit(0)
            else:
                # Da lay het toan bo cac trang truoc
                break
                
        # Xu ly ngoai le E2: API tra ve ma loi (sai API key hoac rate limit)
        if status == "0":
            err_msg = str(result)
            if "rate limit" in err_msg.lower() or "max rate limit" in err_msg.lower():
                if key_index + 1 < len(api_keys):
                    key_index += 1
                    current_key = api_keys[key_index]
                    print(f"[*] Cham rate-limit, chuyen sang dung API Key du phong thu {key_index + 1}...")
                    time.sleep(1)
                    continue
                else:
                    print(f"[LOI E2] API Etherscan bao loi rate-limit: {result}")
                    sys.exit(1)
            else:
                print(f"[LOI E2] API Etherscan bao loi: {result} (Message: {message})")
                sys.exit(1)
                
        if not isinstance(result, list):
            print(f"[LOI] Du lieu tra ve khong phai danh sach: {result}")
            sys.exit(1)
            
        if len(result) == 0:
            if page == 1:
                print("Vi khong co giao dich trong ky")
                sys.exit(0)
            break
            
        # Them cac giao dich vao danh sach tong
        all_transactions.extend(result)
        print(f"[*] Trang {page}: Da thu thap duoc {len(result)} giao dich...")
        
        # Truong hop ngoai le E3: Neu so giao dich day trang (toi da 1000 hoac 10000 theo goi API)
        # Tiep tuc phan trang (Pagination) de lay du toan bo
        if len(result) >= 1000:
            page += 1
            # Tam dung ngan tranh bi danh chan rate-limit
            time.sleep(0.3)
        else:
            # Da den trang cuoi cung
            break

    # Loc chinh xac cac giao dich phat sinh trong pham vi 'days' ngay gan nhat
    filtered_txs = [
        tx for tx in all_transactions
        if int(tx.get("timeStamp", 0)) >= start_timestamp
    ]
    
    if not filtered_txs:
        print("Vi khong co giao dich trong ky")
        sys.exit(0)
        
    print(f"[*] Tong so giao dich trong ky 90 ngay: {len(filtered_txs)}")
    return filtered_txs

# Ham xu ly tinh toan dong tien va kiem tra gian lan AML
def process_cashflow(address: str, raw_txs: list[dict]):
    target_addr = address.strip().lower()
    
    # Quy tac R6: Sap xep du lieu theo trinh tu thoi gian tang dan (timeStamp)
    raw_txs.sort(key=lambda x: int(x.get("timeStamp", 0)))
    
    records = []
    aml_warnings = []
    
    cum_balance = 0.0
    total_eth_in = 0.0
    total_eth_out = 0.0
    
    for tx in raw_txs:
        tx_hash = tx.get("hash", "")
        ts = int(tx.get("timeStamp", 0))
        dt_utc = datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        
        from_addr = tx.get("from", "").strip().lower()
        to_addr = tx.get("to", "")
        to_addr = to_addr.strip().lower() if to_addr else ""
        
        is_error = tx.get("isError", "0") == "1"
        
        # Quy tac R5: Quy doi tat ca gia tri wei sang ETH (chia cho 10^18)
        val_wei = int(tx.get("value", 0))
        val_eth = val_wei / 1e18
        
        gas_used = int(tx.get("gasUsed", 0))
        gas_price = int(tx.get("gasPrice", 0))
        # Tinh phi giao dich thuc te TxFee
        tx_fee_eth = (gas_used * gas_price) / 1e18
        
        # Xac dinh chieu dong tien theo R1, R2, R3, R4
        is_sender = (from_addr == target_addr)
        is_receiver = (to_addr == target_addr)
        
        if is_sender and is_receiver:
            # Giao dich tu gui cho chinh minh
            # Vi van bi tru phi gas mang thuc te
            tx_type = "SELF/OUT"
            eth_amount = 0.0
            actual_fee = tx_fee_eth
            delta = -tx_fee_eth
            total_eth_out += tx_fee_eth
        elif is_sender:
            # Quy tac R2: Giao dich di ra (OUT)
            tx_type = "OUT"
            actual_fee = tx_fee_eth
            if is_error:
                # Quy tac R4: Giao dich that bai van bi tru phi gas
                # So tien chuyen khong bi tru, chi tru phi gas
                eth_amount = 0.0
                delta = -actual_fee
                total_eth_out += actual_fee
            else:
                # Quy tac R3: So tien thuc tru = Value + TxFee
                eth_amount = val_eth
                delta = -(val_eth + actual_fee)
                total_eth_out += (val_eth + actual_fee)
        elif is_receiver:
            # Quy tac R1: Giao dich di vao (IN)
            tx_type = "IN"
            actual_fee = 0.0 # Nguoi gui la ben tra phi gas
            if is_error:
                # Giao dich gui den bi that bai thi khong nhan duoc tien
                eth_amount = 0.0
                delta = 0.0
            else:
                eth_amount = val_eth
                delta = val_eth
                total_eth_in += val_eth
        else:
            # Truong hop khong lien quan truc tiep den dia chi
            continue
            
        cum_balance += delta
        
        # Quy tac R7: Kiem tra canh bao gian lan / rua tien AML
        # 1. Giao dich thu nghiem (Test Txn <= 0.01 ETH)
        if 0 < val_eth <= 0.01 and not is_error:
            aml_warnings.append({
                "TxHash": tx_hash,
                "Datetime": dt_utc,
                "Type": tx_type,
                "ValueETH": val_eth,
                "Reason": "Test Txn: Giao dich thu nghiem gia tri nho (<= 0.01 ETH)"
            })
            
        # 2. Giao dich tron tien dot bien (so nguyen ETH tron va lon, vi du: >= 1 ETH)
        if val_eth >= 1.0 and abs(val_eth - round(val_eth)) < 1e-6 and not is_error:
            aml_warnings.append({
                "TxHash": tx_hash,
                "Datetime": dt_utc,
                "Type": tx_type,
                "ValueETH": val_eth,
                "Reason": f"Round Amount: Giao dich tron tien dot bien ({int(round(val_eth))} ETH)"
            })
            
        records.append({
            "Datetime UTC": dt_utc,
            "Timestamp": ts,
            "TxHash": tx_hash,
            "Type": tx_type,
            "Amount (ETH)": eth_amount,
            "Fee (ETH)": actual_fee,
            "Cumulative Balance (ETH)": cum_balance,
            "Status": "Failed" if is_error else "Success"
        })
        
    df = pd.DataFrame(records)
    summary = {
        "total_in": total_eth_in,
        "total_out": total_eth_out,
        "ending_balance_delta": cum_balance
    }
    
    return df, summary, aml_warnings

# Ham ve bieu do duong bien dong so du luy ke theo thoi gian
def plot_cumulative_chart(df: pd.DataFrame, address: str, output_path: str = "cashflow_90days.png"):
    if df.empty:
        return
        
    # Tao bieu do duong voi Matplotlib
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
    fig, ax = plt.subplots(figsize=(12, 6), dpi=150)
    
    # Chuyen cot Datetime UTC sang kieu datetime de ve truc hoanh chuan xac
    dt_series = pd.to_datetime(df["Datetime UTC"])
    
    # Ve duong bien dong so du luy ke
    ax.plot(dt_series, df["Cumulative Balance (ETH)"], color="#2563eb", linewidth=2, label="So du luy ke (ETH)")
    
    # To vung mau ben duoi duong so du
    ax.fill_between(dt_series, df["Cumulative Balance (ETH)"], color="#3b82f6", alpha=0.15)
    
    # Them diem danh dau cac giao dich
    ax.scatter(dt_series, df["Cumulative Balance (ETH)"], color="#1d4ed8", s=18, zorder=4)
    
    short_addr = f"{address[:6]}...{address[-4:]}"
    ax.set_title(f"BIEN DONG SO DU ETH LUY KE (90 NGAY) - VI: {short_addr}", fontsize=13, fontweight="bold", pad=15)
    ax.set_xlabel("Thoi gian (UTC)", fontsize=11, labelpad=10)
    ax.set_ylabel("So du luy ke (ETH)", fontsize=11, labelpad=10)
    
    # Dinh dang truc thoi gian
    fig.autofmt_xdate(rotation=30)
    ax.legend(loc="upper left", frameon=True)
    
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"[*] Da luu bieu do bien dong so du tai: {output_path}")

# Ham hien thi bang du lieu va ket qua tong hop
def display_results(df: pd.DataFrame, summary: dict, warnings: list[dict], address: str):
    print("\n" + "="*85)
    print(f"BAO CAO DONG TIEN ON-CHAIN ETHEREUM (90 NGAY)")
    print(f"Dia chi vi: {address}")
    print("="*85)
    
    # Cac cot hien thi theo dac ta SPEC.md
    display_cols = ["Datetime UTC", "Type", "Amount (ETH)", "Fee (ETH)", "Cumulative Balance (ETH)", "Status"]
    
    print("\n[+] BANG DU LIEU GIAO DICH SACH:")
    if len(df) <= 30:
        print(df[display_cols].to_string(index=False))
    else:
        print(df[display_cols].head(15).to_string(index=False))
        print(f"\n... (con {len(df) - 30} giao dich o giua) ...\n")
        print(df[display_cols].tail(15).to_string(index=False))
        
    print("\n" + "-"*85)
    print("[+] BA CON SO TONG HOP:")
    print(f" 1. Tong ETH vao (IN)       : {summary['total_in']:,.6f} ETH")
    print(f" 2. Tong ETH ra  (OUT)      : {summary['total_out']:,.6f} ETH (bao gom ca phi gas mang)")
    print(f" 3. So du bien dong cuoi ky : {summary['ending_balance_delta']:+,.6f} ETH")
    print("-"*85)
    
    print("\n[+] CANH BAO GIAN LAN / RUA TIEN (AML) (R7):")
    if not warnings:
        print(" -> Khong phat hien dau hieu giao dich dang ngo (Test Txn hoac Round Amount).")
    else:
        print(f" -> Phat hien {len(warnings)} giao dich can chu y:")
        for idx, w in enumerate(warnings[:15], start=1):
            print(f"  {idx}. [{w['Datetime']}] {w['Type']} | {w['ValueETH']:,.4f} ETH | {w['Reason']} | Hash: {w['TxHash'][:12]}...")
        if len(warnings) > 15:
            print(f"  ... va con {len(warnings) - 15} canh bao khac.")
    print("="*85 + "\n")

def main():
    parser = argparse.ArgumentParser(description="Cong cu phan tich dong tien vi On-chain (90 ngay)")
    parser.add_argument("-a", "--address", type=str, help="Dia chi vi Ethereum can phan tich (42 ky tu bat dau bang 0x)")
    parser.add_argument("-d", "--days", type=int, default=90, help="So ngay can phan tich (mac dinh: 90)")
    parser.add_argument("-c", "--chainid", type=int, default=1, help="Chain ID (1: Ethereum Mainnet, 11155111: Sepolia, mac dinh: 1)")
    parser.add_argument("-o", "--output", type=str, default="cashflow_90days.png", help="Ten tep anh bieu do xuat ra")
    
    args = parser.parse_args()
    
    # Lay dia chi vi tu tham so hoac hoi truc tiep nguoi dung
    wallet_address = args.address
    if not wallet_address:
        print("--- CONG CU PHAN TICH DONG TIEN VI ETHEREUM ON-CHAIN (90 NGAY) ---")
        wallet_address = input("Nhap dia chi vi Ethereum can kiem tra (0x...): ").strip()
        
    if not validate_eth_address(wallet_address):
        print(f"[LOI] Dia chi vi '{wallet_address}' khong dung dinh dang Ethereum (phai dai 42 ky tu va bat dau bang 0x).")
        sys.exit(1)
        
    # Doc API key
    api_keys = get_etherscan_api_keys()
    
    # Thu thap du lieu
    raw_txs = fetch_normal_transactions(wallet_address, api_keys, days=args.days, chain_id=args.chainid)
    
    # Tinh toan dong tien
    df, summary, warnings = process_cashflow(wallet_address, raw_txs)
    
    # Hien thi ket qua
    display_results(df, summary, warnings, wallet_address)
    
    # Ve bieu do duong
    plot_cumulative_chart(df, wallet_address, output_path=args.output)

if __name__ == "__main__":
    main()
