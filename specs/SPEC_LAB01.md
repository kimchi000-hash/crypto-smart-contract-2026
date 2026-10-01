# SPEC — LAB 01: CHUẨN BỊ MÔI TRƯỜNG & CONTRACT ĐẦU TIÊN

## 1. Mục đích
Thiết lập môi trường làm việc chuẩn với Antigravity IDE, cấu hình quy ước AI trong `AGENTS.md`, tạo và quản lý ví MetaMask trên mạng thử nghiệm Sepolia, và triển khai thành công hợp đồng thông minh đầu tiên (`HelloWorld.sol`).

## 2. Đầu vào
- Chuỗi ký tự khởi tạo (`_initGreeting` string, ví dụ: `"Xin chao Web3 ECO2432"`).
- Tài khoản ví cá nhân EOA trên mạng Ethereum Sepolia có sẵn số dư Sepolia ETH để chi trả phí gas mạng.
- Địa chỉ ví công khai gồm 42 ký tự hex bắt đầu bằng `0x`.

## 3. Quy tắc nghiệp vụ
- R1: Mọi người dùng mạng đều có thể gọi biến trạng thái public `greeting` để đọc nội dung lưu trữ mà không mất phí gas (hàm đọc `view`, chi phí 0 gas).
- R2: Bất kỳ ai gọi hàm `setGreeting(string memory _newGreeting)` đều cập nhật được chuỗi mới vào Storage của hợp đồng và người gọi phải trả phí gas mạng cho EVM.
- R3: Toàn bộ chú thích trong mã nguồn Solidity và tài liệu kỹ thuật phải tuân thủ viết bằng tiếng Việt không dấu theo quy ước tại `AGENTS.md`.

## 4. Đầu ra
- Giá trị chuỗi `greeting` hiển thị chính xác trên giao diện Remix Console / Remix VM.
- Mã băm giao dịch (TxHash) ghi nhận lượt triển khai hợp đồng thành công trên mạng Sepolia Etherscan.
- Ảnh chụp màn hình không gian làm việc Antigravity IDE đang mở đúng kho mã nguồn.

## 5. Trường hợp ngoại lệ
- E1: Nếu chuỗi nhập vào rỗng (`""`) thì hệ thống vẫn cho phép ghi nhận (do hợp đồng chưa cài đặt kiểm tra độ dài chuỗi) nhưng cảnh báo không có nội dung hiển thị.
- E2: Nếu số dư Sepolia ETH của ví gửi bằng 0 thì giao dịch gửi lên mạng bị từ chối ngay tại MetaMask do không đủ tiền trả phí gas.
- E3: Nếu mất kết nối daemon `remixd` cục bộ thì trình duyệt không đồng bộ được mã nguồn từ máy tính lên Remix IDE, buộc phải dùng phương thức sao chép - dán thủ công.

## 6. Ngoài phạm vi
- Không phân quyền người sửa (chưa tích hợp mẫu quản trị `Ownable`, bất kỳ ai cũng có thể thay đổi lời chào).
- Không thu phí dịch vụ tương tác (không yêu cầu thanh toán kèm `payable`).
- Không hỗ trợ chuyển hay lưu trữ ETH trong hợp đồng.
