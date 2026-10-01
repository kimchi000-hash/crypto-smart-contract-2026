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