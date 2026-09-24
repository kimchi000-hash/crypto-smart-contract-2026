# Lab 3B — Follow the Money — [Họ và tên] — [MSSV]

## Trạm 1 — Giao dịch gốc

| Trường | Giá trị |
| :--- | :--- |
| **Status** | Success |
| **Block** | 21.895.251 |
| **Timestamp (UTC)** | 2025-02-21 14:16:11 UTC |
| **From** | `0x0fa09c3a328792253f8dee7116848723b72a6d2e` (Ví EOA của hacker ký lệnh khởi tạo giao dịch) |
| **To** | `0x1db92e2eebc8e0c075a02bea49a2935bcd2dfcf4` (Ví lạnh Bybit - Hợp đồng Gnosis Safe multisig proxy) |
| **Value** | 0 ETH |
| **Transaction Fee** | 0,000379 ETH (≈ 1 USD) |
| **Ví nhận 401.346 ETH (Hop 0)** | `0x47666fab8bd0ac7003bce3f5c3585383f09486e2` |

**Vì sao Value = 0 mà tiền vẫn đi:**  
Trường `Value` ở tab Overview của Etherscan chỉ hiển thị số lượng ETH được chuyển trực tiếp qua lời gọi ngoài (top-level call) từ địa chỉ `From` đến `To`. Trong giao dịch này, kẻ tấn công kích hoạt ví hợp đồng đa chữ ký Safe của Bybit, sau đó hợp đồng Safe thực hiện `DELEGATECALL` sang một bản cài đặt độc hại (`0xbdd077f651ebe7f7b3ce16fe5f2b025be2969516`) đã bị tráo đổi trước đó. Hợp đồng độc hại này ra lệnh chuyển toàn bộ 401.346,7688 ETH từ ví Bybit tới ví của hacker (`0x4766...`). Vì dòng tiền dịch chuyển thông qua các lệnh gọi nội bộ giữa các hợp đồng thông minh (internal call/contract call), số tiền không nằm ở trường `Value` ngoài mà được ghi nhận đầy đủ tại tab **Internal Txns**.

---

## Trạm 2 — Hop 1

| Chỉ số | Giá trị | Bằng chứng |
| :--- | :--- | :--- |
| Giao dịch ra đầu tiên có giá trị > 0 | 1 ETH → `0xa4b2fd68...`, 14:29:47 UTC (13 phút sau vụ hack) | `0xdd5cd734d4d67ff5af7e53cdd72c26d4d7d28d08c8f0ff32d12ab3e2a277e4bc` |
| Số giao dịch ra đúng 10.000 ETH | 40 giao dịch (tổng cộng 400.000 ETH) | Tx đầu: `0x0359814b48479156b804c8330878214943204c597d88affcb164d04907fa2b25` (14:56 UTC) |
| Khoảng thời gian thực hiện phần lớn số đó | 1 tx lúc 14:56 UTC; 39 tx còn lại thực hiện từ 15:48 đến 15:50 UTC (~2 phút) | Tx mẫu: `0x9b7cbb6e23aca5ef5718602ea8342b7f67751a6867c19780c2fbe9c045abb258` |
| Số dư ETH hiện tại của ví hacker | 0,207 ETH (nonce 62) | Địa chỉ ví: `0x47666fab8bd0ac7003bce3f5c3585383f09486e2` |

**Trả lời 3 câu thảo luận:**  
1. **Giao dịch ra đầu tiên chỉ có 1 ETH:** Trong nghiệp vụ AML, đây gọi là **Test Transaction (Giao dịch thăm dò / Thử nghiệm)**. Mục đích là để kiểm tra và xác nhận tuyến đường chuyển tiền, đảm bảo địa chỉ đích hoạt động chính xác trước khi chuyển những khoản tiền lớn. Mặc dù người dùng hợp pháp cũng hay gửi thử nghiệm, nhưng việc gửi thử 1 ETH rồi ngay sau đó chuyển hàng loạt khoản tiền khổng lồ là dấu hiệu cảnh báo đỏ (red flag) điển hình.
2. **Vì sao chia thành các khoản đúng bằng nhau 10.000 ETH thay vì rút một lần:** Thuật ngữ AML cho bước này là **Layering (Phân tầng / Làm mờ dòng tiền)** — giai đoạn thứ 2 của quy trình rửa tiền. Hacker chia thành 40 khoản bằng nhau nhằm: nhân số lượng ví trung gian cần điều tra, dễ dàng phân tán và xử lý song song qua nhiều cầu nối (bridge) và sàn phi tập trung (DEX), đồng thời hạn chế trượt giá và tránh bị chặn toàn bộ số tiền nếu chỉ dồn vào một luồng rút duy nhất.
3. **~40 giao dịch trong ~2 phút: người hay máy thao tác? Căn cứ:** Đây chắc chắn là **Máy (Script/Bot tự động)** thao tác. Căn cứ: tốc độ cực nhanh (39 giao dịch diễn ra chỉ trong vòng ~120 giây), số tiền chuyển đạt độ chuẩn xác tuyệt đối (đúng 10.000 ETH/giao dịch), và mức phí gas (Gas Price) được đồng bộ đồng đều theo chương trình lập sẵn — con người thao tác thủ công qua giao diện ví (như MetaMask) hoàn toàn không thể đạt được tốc độ và tính đồng nhất này.

---

## Trạm 3 — Hop 2 & tin nhắn

| Câu hỏi | Trả lời | Bằng chứng |
| :--- | :--- | :--- |
| Ví này nhận 10.000 ETH lúc nào? | 2025-02-21 14:56:11 UTC | `0x0359814b48479156b804c8330878214943204c597d88affcb164d04907fa2b25` |
| Giao dịch ra đầu tiên: bao nhiêu ETH, đến đâu, lúc nào? | 5.000 ETH → `0x4571bd67d14280e40bf3910bd39fbf60834f900a`, lúc 2025-02-22 06:28:23 UTC | `0xbf80907830e46317da2c1708a13a9f016e242f8a6db6e6b0706ea5f2328cb001` |
| Tiền nằm yên trong ví bao lâu trước khi đi tiếp? | ≈ 15,5 giờ (từ 14:56 UTC ngày 21/02 đến 06:28 UTC ngày 22/02) | Mô hình: 10.000 ETH → 2 x 5.000 ETH (giao dịch ra thứ hai: `0x84f0d4b3...` lúc 10:30:47 UTC) |

**Nội dung tin nhắn giải mã:**  
`"This is FBI. You could be arrested. We are monitoring at you over kitchen window. 100 ETH to this address and we are going away. "`  
*(Bằng chứng: Giao dịch `0xf0f7c2a84e29300089fc1049982675c68efcfc8a18557193f113f9881d014f55`, gửi từ `0x92c36f5e...`)*

**Anonymous vs pseudonymous:**  
- **Anonymous (Vô danh):** Hoàn toàn không để lại danh tính, không có dữ liệu truy vết hay mối liên kết nào về đối tượng thực hiện hành động.  
- **Pseudonymous (Bút danh / Giả danh):** Người dùng ẩn danh tính đời thực sau một "bí danh" công khai là địa chỉ ví (`0x...`). Danh tính cá nhân (tên thật, CCCD) ban đầu chưa lộ diện, nhưng toàn bộ hành vi, dòng tiền và lịch sử giao dịch gắn liền với địa chỉ đó được ghi nhận vĩnh viễn trên sổ cái công khai. Chỉ cần địa chỉ này có một lần tương tác với các điểm chạm có KYC (như nạp/rút sàn CEX) hoặc để lộ IP, toàn bộ lịch sử quá khứ sẽ lập tức được quy chiếu về chủ thể thực tế ngoài đời.

---

## Trạm 4 — Kết luận

1. **Sơ đồ dòng tiền:**  
   `Bybit (0x1db92e2e...) --[401.346,77 ETH @ 14:16 UTC 21/02]--> Hacker (0x47666fab...) --[10.000 ETH @ 14:56 UTC 21/02]--> Hop 2 (0x36ed3c02...) --[5.000 ETH @ 06:28 UTC 22/02]--> Hop 3 (0x4571bd67...)`

2. **Nếu là chuyên viên tuân thủ (Compliance/AML Officer) của sàn khi khách hàng nạp từ ví Hop 2:**  
   - **Hành động 1:** Lập tức phong tỏa/đóng băng (Freeze) khoản tiền nạp và tài khoản nhận, kích hoạt quy trình thẩm định nâng cao (EDD - Enhanced Due Diligence), yêu cầu khách hàng chứng minh nguồn gốc tài sản (Source of Funds).  
   - **Hành động 2:** Lập báo cáo giao dịch đáng ngờ (STR/SAR) gửi cho cơ quan quản lý phòng chống rửa tiền; đồng thời đưa địa chỉ vào danh sách cảnh báo nội bộ và đối chiếu với danh mục ví đen của các đơn vị tình báo on-chain (Chainalysis, TRM Labs) cùng chương trình bounty/cảnh báo của Bybit.

3. **Vì sao blockchain công khai mà hacker vẫn tẩu tán được? Giới hạn truy vết:**  
   Blockchain chỉ công khai và minh bạch trên từng mạng lưới đơn lẻ. Hacker tẩu tán tiền bằng cách phá vỡ liên kết dòng tiền qua: dịch vụ trộn tiền (như Tornado Cash), hoán đổi chuỗi chéo qua cross-chain bridge (như THORChain đổi ETH sang BTC), hoặc nạp vào các sàn không bắt buộc KYC và các bàn giao dịch OTC/P2P ngầm. Giới hạn của việc truy vết on-chain là công cụ chỉ giúp quan sát và gắn nhãn nhưng không thể tự động thu hồi tài sản phi tập trung; việc phong tỏa thực tế bắt buộc phải phụ thuộc vào các điểm rút tiền pháp định (Off-ramp) chịu sự quản lý pháp lý.

---

## AI_JOURNAL
- **Công cụ AI đã dùng:** Antigravity IDE (Gemini 3.8 Flash).
- **Prompt hiệu quả nhất:** *"Bạn là chuyên viên phân tích on-chain. Dưới đây là dữ liệu tôi copy từ Etherscan của một giao dịch Ethereum. Hãy: 1. Giải thích vì sao 'Value' = 0 ETH nhưng vẫn có 401.346 ETH được chuyển. 2. Phân biệt ví 'From', 'To' và ví nhận tiền cuối cùng. Chỉ trả lời dựa trên dữ liệu tôi cung cấp. Nếu không có trong dữ liệu, nói là không có."*
- **Một chỗ AI nói sai / thừa / không kiểm chứng được:** Khi hỏi tự do về vụ hack Bybit mà không cung cấp ngữ cảnh, AI ban đầu suy đoán sai cơ chế rút tiền là do lộ private key của ví nóng (hot wallet), trong khi thực tế trên blockchain là ví lạnh Safe multisig bị tấn công qua interface spoofing tráo implementation contract và tiền được chuyển qua giao dịch nội bộ (`DELEGATECALL`). Ngoài ra, AI thường bịa số dư hiện tại của ví hacker nếu không được chỉ định truy vấn trực tiếp qua API Blockscout/Etherscan