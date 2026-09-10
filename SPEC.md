# SPEC
HelloWorld Smart Contract

## 1. Mục đích
Hệ thống lưu trữ và cập nhật thông điệp chào mừng trên blockchain cho người dùng.

## 2. Đầu vào
- _initialGreeting: chuỗi ký tự (string), do người triển khai hợp đồng cung cấp lúc khởi tạo.
- _newGreeting: chuỗi ký tự (string), do chủ sở hữu hợp đồng (Owner) cung cấp khi cập nhật.

## 3. Quy tắc nghiệp vụ
- R1: Bất kỳ ai cũng có thể đọc thông điệp chào mừng hiện tại mà không tốn phí.
- R2: Chỉ chủ sở hữu (i_owner) mới có quyền cập nhật thông điệp mới.
- R3: Mỗi lần cập nhật thành công, biến đếm s_updateCount phải tăng thêm 1 đơn vị và phát ra sự kiện GreetingChanged.

## 4. Đầu ra
- Chuỗi thông điệp s_greeting hiển thị công khai.
- Số lần cập nhật s_updateCount.
- Sự kiện GreetingChanged được ghi vào log giao dịch.

## 5. Trường hợp ngoại lệ
- Nếu người gọi không phải chủ sở hữu gọi hàm cập nhật: hệ thống từ chối giao dịch với lỗi tùy biến NotOwner().
- Nếu người dùng nạp ETH vào hợp đồng: hệ thống từ chối vì không có hàm nhận tiền payable.

## 6. Ngoài phạm vi
- Không thu phí người dùng khi cập nhật lời chào ngoài phí gas của mạng.
- Không hỗ trợ xóa thông điệp đã lưu.