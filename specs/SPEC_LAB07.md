# SPEC — LAB 07: TÍNH CHI PHÍ VẬN HÀNH THỰC TẾ

## 1. Mục đích
Đóng vai trò chuyên viên phân tích nghiệp vụ / tài chính giải quyết bài toán kinh tế đo lường chi phí gas vận hành hệ thống on-chain (bài toán thẻ tích điểm CLB 1.000 giao dịch/tháng và hệ thống Bỏ phiếu bầu ban cán sự / Ban chủ nhiệm CLB phi tập trung cho 500 cử tri), so sánh Ethereum Layer 1 với Layer 2 để thẩm định và kết luận tính khả thi kinh doanh của sản phẩm Web3.

## 2. Đầu vào
- Định mức gas tham khảo cho các thao tác on-chain:
  - Ghi một biến mới vào Storage lâu dài: ~20.000 gas.
  - Cử tri thực hiện một lượt bỏ phiếu (`vote`): ~48.000 gas.
  - Đăng ký cử tri theo lô (`registerVoters` batch ~50 cử tri/lô): ~120.000 gas/lô.
  - Triển khai hợp đồng cỡ nhỏ (`Deploy SimpleVoting`): ~700.000 gas.
- Đơn giá gas mạng tham chiếu: 20 Gwei = 20 × 10^-9 ETH.
- Giá ETH tham chiếu: 1 ETH = 3.000 USD.
- Hệ số tối ưu chi phí của mạng Layer 2 (Base, Arbitrum): rẻ hơn xấp xỉ 100 lần so với Layer 1.

## 3. Quy tắc nghiệp vụ
- R1: Chi phí một giao dịch (đơn vị ETH) = `Lượng gas tiêu thụ × Đơn giá gas (Gwei) × 10^-9`.
- R2: Chi phí một giao dịch (đơn vị USD) = `Phí một giao dịch (ETH) × Giá ETH tham chiếu (USD)`.
- R3: Tính toán tổng chi phí hàng tháng cho bài toán cơ sở (1.000 lượt ghi tích điểm CLB) trên cả Layer 1 và Layer 2.
- R4: Áp dụng khung tính toán mở rộng cho ý tưởng đồ án nhóm (Kỳ bầu cử Ban chủ nhiệm CLB / Ban cán sự phi tập trung quy mô 500 cử tri).
- R5: Phân tích trách nhiệm chi trả và đánh giá mức độ chấp nhận của người dùng (sinh viên) cùng khả năng tài trợ của ngân sách CLB để đưa ra kết luận hạ tầng triển khai.

## 4. Đầu ra
- Tệp báo cáo `lab07.md` hoàn chỉnh gồm 4 phần:
  1. Cấu trúc chi phí cơ sở.
  2. Bảng tính chi phí vận hành cho 1.000 lượt ghi thẻ tích điểm CLB.
  3. Đánh giá tính khả thi và mô hình kinh tế giữa Layer 1 và Layer 2.
  4. Bảng tính mở rộng và kết luận tính khả thi cho đề tài Bỏ phiếu phi tập trung (`SimpleVoting`) của nhóm.
- Kết luận rõ ràng về lựa chọn nền tảng mạng triển khai (Layer 2) để đảm bảo mô hình có thể ứng dụng trong thực tế.

## 5. Trường hợp ngoại lệ
- E1: Nếu giá ETH biến động tăng vọt lên mức 5.000 USD thì chi phí vận hành trên L1 tăng tỷ lệ thuận (trên 60 triệu VNĐ cho một kỳ bầu cử), càng củng cố lý do bắt buộc phải chuyển sang Layer 2.
- E2: Nếu mạng Layer 1 rơi vào tình trạng tắc nghẽn khiến gas price tăng lên 100 Gwei thì chi phí giao dịch L1 tăng gấp 5 lần, làm tê liệt hoàn toàn khả năng tương tác của sinh viên.
- E3: Nếu ứng dụng áp dụng giải pháp Account Abstraction (ERC-4337 / Paymaster) thì CLB/Đoàn Hội có thể tài trợ toàn bộ phí gas trên Layer 2 để sinh viên được trải nghiệm bỏ phiếu hoàn toàn miễn phí (`Gasless transaction`).

## 6. Ngoài phạm vi
- Không viết và triển khai hợp đồng thông minh hoàn chỉnh trong buổi Lab 7 (nội dung kỹ thuật sẽ triển khai tại Lab 9).
- Không tính toán các yếu tố trượt giá thanh khoản hay chi phí cầu nối nạp/rút giữa các chuỗi (bridge fee).
