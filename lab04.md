# Báo cáo Lab 4: Nhận diện hợp đồng có rủi ro

## 1. Bảng kết luận thẩm định rủi ro

| Hợp đồng | Địa chỉ Sepolia (nếu có) | Kết luận | Tên hàm | Số dòng vi phạm | Rủi ro cho người nắm giữ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **A** (`ClubTokenA`) | *(Chờ GV cấp)* | Bình thường / Sạch | Không có | Không có | Không có rủi ro; tổng cung cố định, không có quyền quản trị đặc biệt can thiệp số dư. |
| **B** (`ClubTokenB`) | *(Chờ GV cấp)* | Có rủi ro cao | `mint` | Dòng 12-14 | Chủ sở hữu có thể tự ý tạo thêm token vô hạn không có giới hạn trần, gây pha loãng nghiêm trọng giá trị token của người nắm giữ. |
| **C** (`ClubTokenC`) | *(Chờ GV cấp)* | Có rủi ro cao | `setRestricted` kết hợp `_update` | Dòng 12-19 | Chủ sở hữu có quyền tùy tiện gắn cờ hạn chế địa chỉ ví bất kỳ; người mua có thể bị khóa chiều chuyển đi (mua được nhưng không bán ra được). |

## 2. Nhận xét và bài học nghiệp vụ
* **Về mặt kỹ thuật:** Cả hai hàm rủi ro đều có chỉ thị `onlyOwner` và chú thích có vẻ hợp lý (phục vụ khuyến mại, bảo vệ cộng đồng). Điều này cho thấy mã nguồn không bị lỗi cú pháp, mà chứa đựng rủi ro thiết kế quản trị tập trung.
* **Góc độ thẩm định rủi ro:** Chuyên viên thẩm định cần đánh giá quyền lực tối đa mà chủ sở hữu có thể thực hiện và hậu quả khi quyền đó bị lạm dụng hoặc khi chủ sở hữu bị lộ khóa riêng tư (private key).