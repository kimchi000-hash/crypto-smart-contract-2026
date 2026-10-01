# SPEC — LAB 06: SINH MÃ BẰNG AI VÀ KIỂM TRA KẾT QUẢ

## 1. Mục đích
Ứng dụng công cụ AI để sinh mã kịch bản Python từ đặc tả `SPEC.md`, tuân thủ các quy ước phát triển trong `AGENTS.md`, thực thi kiểm thử trên dữ liệu blockchain thực tế và thực hiện quy trình audit mã nguồn để phát hiện, xử lý tối thiểu 2 lỗi do AI sinh ra.

## 2. Đầu vào
- Tài liệu đặc tả yêu cầu kỹ thuật `SPEC.md`.
- Khóa API Etherscan (`ETHERSCAN_API_KEY`) đọc từ biến môi trường thông qua tệp `.env`.
- Địa chỉ ví Ethereum mục tiêu cần quét và phân tích dữ liệu dòng tiền trong 90 ngày gần nhất.

## 3. Quy tắc nghiệp vụ
- R1: Khóa API Etherscan phải được nạp thông qua thư viện `dotenv` từ tệp `.env`, tuyệt đối không ghi cứng (hardcode) chuỗi API key vào mã nguồn vì lý do an toàn thông tin.
- R2: Tự động phân trang (Pagination) bằng cách tăng biến `page` khi số lượng giao dịch vượt ngưỡng hạn mức một lần gọi API (1.000 hoặc 10.000 tx) để thu thập trọn vẹn 100% dữ liệu lịch sử.
- R3: Phí gas của các giao dịch thất bại (`isError == '1'`) vẫn phải được tính vào dòng tiền ra (`OUT`) theo công thức `TxFee = (gasUsed × gasPrice) / 10^18`.
- R4: Quy đổi toàn bộ giá trị từ `wei` sang `ETH` (chia cho 10^18) trước khi xử lý tính toán số dư lũy kế và hiển thị.
- R5: Xuất biểu đồ đường `cashflow_90days.png` thể hiện trực quan biến động số dư lũy kế theo thời gian UTC.
- R6: Toàn bộ chú thích trong mã nguồn phải viết bằng tiếng Việt không dấu theo đúng quy định tại `AGENTS.md`.

## 4. Đầu ra
- Kịch bản Python hoàn chỉnh `analyze_cashflow.py` chạy ổn định, không phát sinh lỗi ngoại lệ chưa xử lý.
- Tệp ảnh biểu đồ đường `cashflow_90days.png` trực quan hóa biến động số dư ví trong 90 ngày.
- Nhật ký kiểm thử trong `AI_JOURNAL.md` ghi nhận tối thiểu 2 lỗi do AI sinh ra kèm phân tích cách sửa và xác nhận cột `"Ai phát hiện: Sinh viên phát hiện"`.

## 5. Trường hợp ngoại lệ
- E1: Nếu người dùng cấu hình sai API key hoặc hết hạn ngạch truy vấn (rate-limit) thì chương trình in thông báo lỗi rõ ràng và dừng xử lý an toàn, không để crash đột ngột.
- E2: Nếu địa chỉ ví không có bất kỳ giao dịch nào trong 90 ngày thì in thông báo `"Vi khong co giao dich trong ky"` và kết thúc bình thường, không báo lỗi hệ thống.
- E3: Nếu mã AI sinh ra sử dụng endpoint API v1 cũ đã ngừng hỗ trợ thì sinh viên phải đối chiếu tài liệu chính thức của Etherscan và chuyển đổi sang endpoint Etherscan API V2 (`https://api.etherscan.io/v2/api`).

## 6. Ngoài phạm vi
- Không phân tích các giao dịch hợp đồng thông minh chuyển token chuẩn ERC-20 hoặc NFT ERC-721.
- Không thực hiện quy đổi giá trị sang các loại tiền pháp định (USD, VND).
