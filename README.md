# HỌC PHẦN ECO2432 — TIỀN ĐIỆN TỬ & HỢP ĐỒNG THÔNG MINH

- **Họ và tên:** Nguyễn Thị Kim Chi
- **Mã sinh viên:** 23K4300025
- **Tài khoản GitHub:** kimchi000-hash
- **Mạng thử nghiệm:** Ethereum Sepolia Testnet

---

## 📑 Bảng tra cứu tiến độ nghiệm thu (Lab 1 — Lab 7)

| Bài Lab | Tên bài thực hành | Đặc tả nghiệp vụ (SPEC) | Báo cáo / Sản phẩm bàn giao | Nhật ký AI | Trạng thái |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **Lab 01** | Chuẩn bị môi trường & Contract đầu tiên | [SPEC_LAB01.md](specs/SPEC_LAB01.md) | [AGENTS.md](AGENTS.md) | — | ✅ Hoàn thành |
| **Lab 02** | Ví và giao dịch đầu tiên | [SPEC_LAB02.md](specs/SPEC_LAB02.md) | [lab02.md](lab02.md) | — | ✅ Hoàn thành |
| **Lab 03** | Đọc giao dịch trên Etherscan & AML | [SPEC_LAB03.md](specs/SPEC_LAB03.md) | [forensics.md](forensics.md) & [trace.md](trace.md) | [AI_JOURNAL.md](AI_JOURNAL.md) | ✅ Hoàn thành |
| **Lab 04** | Nhận diện hợp đồng có rủi ro | [SPEC_LAB04.md](specs/SPEC_LAB04.md) | [lab04.md](lab04.md) | [AI_JOURNAL.md](AI_JOURNAL.md) | ✅ Hoàn thành |
| **Lab 05** | Viết đặc tả cho công cụ phân tích dòng tiền | [SPEC_LAB05.md](specs/SPEC_LAB05.md) | [SPEC.md](SPEC.md) | — | ✅ Hoàn thành |
| **Lab 06** | Sinh mã bằng AI và kiểm tra kết quả | [SPEC_LAB06.md](specs/SPEC_LAB06.md) | [analyze_cashflow.py](analyze_cashflow.py) & [cashflow_90days.png](cashflow_90days.png) | [AI_JOURNAL.md](AI_JOURNAL.md) | ✅ Hoàn thành |
| **Lab 07** | Tính chi phí vận hành thực tế | [SPEC_LAB07.md](specs/SPEC_LAB07.md) | [lab07.md](lab07.md) | — | ✅ Hoàn thành |

---
# ECO2432 Web3 Starter

Kho khởi đầu dùng xuyên suốt 15 bài thực hành.

## Bắt đầu (thay cho bước "Fork kho" trong sổ tay)

Sổ tay ghi "Fork kho `hce-web3-starter`". Học kỳ này kho được phát dạng tệp nén, nên làm như sau:

1. Giải nén thư mục này vào máy, mở bằng Antigravity.
2. Đọc `AGENTS.md` trước khi yêu cầu công cụ AI sinh mã.
3. Sao chép `SPEC.md` và `AI_JOURNAL.md` cho từng bài.
4. Chỉ dùng ví thử nghiệm và mạng Sepolia; không dùng khóa ví có tiền thật.

Đưa lên GitHub (làm khi đã có tài khoản; cần trước khi nộp Lab 1):

```bash
git init -b main
git add .
git commit -m "chore: thiet lap moi truong lam viec"
git remote add origin https://github.com/<tai-khoan>/<ten-repo>.git   # repo tạo TRỐNG trên GitHub
git push -u origin main
```

Lab 8 (repo nhóm): một thành viên tạo repo trống mới, đưa nội dung thư mục này lên theo đúng các
lệnh trên, rồi mời các thành viên khác làm collaborator.

## Cấu trúc

- `contracts/training/`: hợp đồng mẫu dùng ở Lab 9, 10, 11 và 13
  (`TimeLockVault`, `VaultBuggy`, `ClassPoint`, `VulnerableBank`).
- `contracts/lab04/ClubTokens.sol`: ba token dùng cho Lab 4.
- `web/index.html`: giao diện mẫu dùng ở Lab 15.
- `prompt_templates.md`: mẫu câu lệnh có yêu cầu và tiêu chí kiểm chứng rõ ràng.

Các hợp đồng có chữ `Buggy`, `Vulnerable` hoặc cảnh báo trong mã đều chứa lỗi có chủ đích.

## Chạy hợp đồng

- Cách chính: mở Remix IDE (`https://remix.ethereum.org`), tạo tệp, dán mã. Remix tự tải thư viện
  `@openzeppelin/...`, không cần cài gì.
- Nếu Antigravity gạch đỏ dòng `import "@openzeppelin/..."`: đó là do máy chưa có thư viện, mã
  không sai. Muốn hết gạch đỏ thì cài Node.js rồi chạy `npm install` trong thư mục này (không bắt buộc).
