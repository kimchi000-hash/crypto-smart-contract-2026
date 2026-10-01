# BÁO CÁO LAB 7 — TÍNH CHI PHÍ VẬN HÀNH THỰC TẾ

## 1. Cấu trúc chi phí cơ sở
- Thao tác: Ghi dữ liệu tích điểm mới vào Storage (~20.000 gas/lượt).
- Đơn giá gas: 20 Gwei = 20 * 10^-9 ETH.
- Giá tham chiếu: 1 ETH = 3.000 USD.
- Tần suất: 1.000 giao dịch/tháng.

## 2. Bảng tính chi phí vận hành

| Chỉ số | Mạng chính (Layer 1) | Mạng mở rộng (Layer 2 - rẻ hơn 100 lần) |
| :--- | :--- | :--- |
| **Gas tiêu thụ / lượt** | 20.000 gas | 20.000 gas |
| **Phí 1 giao dịch (ETH)** | 0.0004 ETH | 0.000004 ETH |
| **Phí 1 giao dịch (USD)** | 1.2 USD (~30.000 VNĐ) | 0.012 USD (~300 VNĐ) |
| **Tổng chi phí 1.000 lượt** | **1.200 USD/tháng (~30.000.000 VNĐ)** | **12 USD/tháng (~300.000 VNĐ)** |

## 3. Đánh giá tính khả thi và Mô hình kinh tế
- **Trách nhiệm chi trả:** Trên Layer 1, câu lạc bộ không đủ kinh phí tài trợ 1.200 USD/tháng; sinh viên cũng không chấp nhận trả 30.000 VNĐ chỉ để nhận một lượt tích điểm. Trên Layer 2, chi phí 12 USD/tháng nằm trong ngân sách vận hành của CLB.
- **Kết luận:** Mô hình không có tính khả thi trên Ethereum L1 vì chi phí giao dịch vượt xa giá trị kinh tế mang lại. Ứng dụng bắt buộc phải triển khai trên giải pháp Layer 2 (như Base hoặc Arbitrum) để đảm bảo trải nghiệm người dùng và bài toán chi phí.

---

## 4. Mở rộng cho ý tưởng đồ án nhóm (Bước 3 — Đề tài Bỏ phiếu phi tập trung)

### 4.1. Bài toán và giả định quy mô
- **Ý tưởng đề tài:** Hệ thống Bỏ phiếu bầu cử Ban chủ nhiệm CLB / Ban cán sự phi tập trung (`SimpleVoting`).
- **Quy mô giả định cho 1 kỳ bầu cử:**
  - Số lượng ứng viên: 5 người.
  - Số lượng cử tri (sinh viên CLB): 500 sinh viên hợp lệ.
  - Tần suất tổ chức: 1 kỳ bầu cử / học kỳ (hoặc theo năm học).
- **Các thao tác on-chain trong 1 kỳ bầu cử:**
  1. *Triển khai hợp đồng (`Deploy SimpleVoting`):* Tạo danh sách ứng viên ban đầu và mốc thời gian khóa (1 lần duy nhất) ~ 700.000 gas.
  2. *Đăng ký cử tri theo lô (`registerVoters`):* Admin đăng ký danh sách ví sinh viên đủ tư cách bầu cử (chia 10 lô, mỗi lô 50 cử tri, ~120.000 gas/lô) = 1.200.000 gas.
  3. *Thao tác cử tri bỏ phiếu (`vote`):* Cử tri chọn ứng viên, hợp đồng cập nhật `hasVoted[msg.sender] = true` (ghi Storage mới), tăng `voteCount` của ứng viên và phát event `Voted` ~ 48.000 gas / lượt vote.
  4. *Kiểm phiếu và xem kết quả (`getResults`, `candidateCount`):* Hàm `view`, đọc dữ liệu công khai trên node, **chi phí gas = 0 (hoàn toàn miễn phí)**.

### 4.2. Bảng ước tính chi phí cho 1 kỳ bầu cử (500 cử tri)

| Hạng mục thao tác | Lượng gas tiêu thụ | Chi phí Ethereum L1 (Gas 20 Gwei, ETH = $3.000) | Chi phí Layer 2 (Base/Arbitrum - rẻ hơn 100 lần) |
| :--- | :--- | :--- | :--- |
| **Triển khai hợp đồng (1 lần)** | 700.000 gas | 0.014 ETH ($42.00 ≈ 1.050.000 VNĐ) | 0.00014 ETH ($0.42 ≈ 10.500 VNĐ) |
| **Đăng ký 500 cử tri (10 lô)** | 1.200.000 gas | 0.024 ETH ($72.00 ≈ 1.800.000 VNĐ) | 0.00024 ETH ($0.72 ≈ 18.000 VNĐ) |
| **1 cử tri thực hiện bỏ phiếu** | 48.000 gas | 0.00096 ETH ($2.88 ≈ 72.000 VNĐ) | 0.0000096 ETH ($0.0288 ≈ 720 VNĐ) |
| **Toàn bộ 500 cử tri bỏ phiếu** | 24.000.000 gas | 0.48 ETH ($1.440.00 ≈ 36.000.000 VNĐ) | 0.0048 ETH ($14.40 ≈ 360.000 VNĐ) |
| **Tổng chi phí trọn gói kỳ bầu cử** | **25.900.000 gas** | **0.518 ETH ($1.554.00 ≈ 38.850.000 VNĐ)** | **0.00518 ETH ($15.54 ≈ 388.500 VNĐ)** |

### 4.3. Đánh giá tính khả thi và Quyết định mô hình kinh tế
- **Trên mạng chính Ethereum (Layer 1):**
  - Chi phí gần 39.000.000 VNĐ cho một cuộc bầu cử nội bộ là hoàn toàn phi lý và bất khả thi đối với ngân sách sinh viên/nhà trường.
  - Nếu bắt sinh viên tự trả phí gas (~72.000 VNĐ/lượt vote), tỷ lệ tham gia sẽ bằng 0 vì rào cản tài chính quá lớn.
- **Trên mạng mở rộng (Layer 2 - Base hoặc Arbitrum):**
  - Chi phí 1 lượt bỏ phiếu chỉ khoảng 720 VNĐ, tổng ngân sách cho toàn bộ cuộc bầu cử chỉ khoảng ~388.500 VNĐ ($15.54).
  - Ban chủ nhiệm CLB / Đoàn trường hoàn toàn có thể trích từ quỹ hoạt động thường niên để tài trợ gas thông qua cơ chế Paymaster (ERC-4337 / Account Abstraction), giúp sinh viên được bỏ phiếu với trải nghiệm không mất phí (Gasless transaction).
- **Kết luận thiết kế sản phẩm:** Đồ án nhóm bắt buộc triển khai trên mạng Layer 2 (hoặc Sepolia testnet phục vụ thử nghiệm). Giải pháp L2 vừa đảm bảo bài toán chi phí thực tế cho môi trường đại học, vừa giữ trọn vẹn các giá trị cốt lõi của Web3: danh sách cử tri minh bạch, mỗi người chỉ được bỏ 1 phiếu, và kết quả kiểm phiếu không thể bị can thiệp hay sửa đổi.