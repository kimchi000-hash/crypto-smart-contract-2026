# SPEC — LAB 02: VÍ VÀ GIAO DỊCH ĐẦU TIÊN

## 1. Mục đích
Thực hiện giao dịch chuyển ETH thử nghiệm, phân biệt tài khoản cá nhân (EOA) với tài khoản hợp đồng (CA), đối chiếu thực tế cách thức trừ phí gas trên chuỗi và giải thích bản chất bất biến của blockchain.

## 2. Đầu vào
- Địa chỉ ví người nhận (`to`), dạng chuỗi 42 ký tự hex bắt đầu bằng `0x`.
- Số lượng ETH chuyển giao dịch (`value`), ví dụ `0.01` hoặc `0.1` Sepolia ETH.
- Mức phí gas tối đa ví gửi cho phép sử dụng (`gasLimit`), mặc định 21.000 gas cho giao dịch chuyển ETH chuẩn giữa hai ví EOA.
- Đơn giá gas mạng (`gasPrice` / `maxFeePerGas`), tính theo đơn vị Gwei tại thời điểm thực hiện.

## 3. Quy tắc nghiệp vụ
- R1: Giao dịch chuyển ETH đơn thuần giữa hai tài khoản cá nhân (EOA sang EOA) tiêu thụ mức gas cố định là 21.000 gas.
- R2: Số tiền thực tế trừ khỏi ví người gửi = Giá trị chuyển (`Value`) + Phí giao dịch thực tế (`TxFee` = `gasUsed × gasPrice`).
- R3: Giao dịch tương tác với tài khoản hợp đồng (Contract Account - CA) tiêu thụ lượng gas thay đổi phụ thuộc vào mức độ phức tạp của logic nghiệp vụ và số lượng ô nhớ Storage được ghi mới.
- R4: Phí giao dịch (gas) luôn phải thanh toán bằng đồng tiền gốc của mạng lưới (ETH), không được khấu trừ trực tiếp vào số tiền chuyển.

## 4. Đầu ra
- Mã băm giao dịch (TxHash) được đóng gói vào khối và xác thực thành công trên Sepolia Etherscan.
- Bảng đối chiếu giao dịch thành công và giao dịch thất bại có chủ đích trong tệp `lab02.md`.
- Đoạn phân tích 3 câu trả lời câu hỏi nghiệp vụ về tính bất biến và khả năng thu hồi tài sản khi chuyển nhầm ví.

## 5. Trường hợp ngoại lệ
- E1: Nếu số dư ví không đủ để thanh toán cả số tiền chuyển kèm phí gas dự kiến (`balance < value + gasLimit × gasPrice`) thì giao diện ví MetaMask từ chối ký gửi (báo lỗi `Insufficient funds`).
- E2: Nếu người gửi gõ nhầm một ký tự trong địa chỉ ví đích dẫn đến sai mã kiểm tra (checksum) thì giao diện ví MetaMask chặn gửi ngay lập tức để bảo vệ người dùng.
- E3: Nếu người gửi đặt mức Gas Price quá thấp so với giá sàn của mạng thì giao dịch bị rơi vào trạng thái kẹt (`Pending` kéo dài), buộc phải gửi giao dịch tăng phí (`Speed Up`) hoặc hủy (`Cancel`) cùng số `nonce`.

## 6. Ngoài phạm vi
- Không thực hiện hoán đổi token qua các sàn giao dịch phi tập trung (DEX).
- Không chuyển các loại tài sản theo tiêu chuẩn token ERC-20 hoặc NFT ERC-721.
- Không thể hoàn tiền hay đảo ngược giao dịch khi đã được các validator đóng gói vào khối on-chain.
