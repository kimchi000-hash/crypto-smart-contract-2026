# NHẬT KÝ LÀM VIỆC VỚI AI

## Lần 1 - Lab 4: Nhận diện hợp đồng có rủi ro
**Prompt:**  
"Bạn là chuyên viên thẩm định rủi ro tài sản số. Dưới đây là mã nguồn một hợp đồng token. Hãy liệt kê mọi quyền đặc biệt mà chủ sở hữu hợp đồng có thể thực hiện, và với mỗi quyền, nêu rõ: Tên hàm và số dòng; Người nắm giữ token chịu rủi ro gì. Chỉ trả lời dựa trên mã nguồn tôi cung cấp. Nếu không tìm thấy, nói là không tìm thấy. [dán mã nguồn ClubTokenA, ClubTokenB, ClubTokenC]"

**AI trả về:**  
* Hợp đồng A: Không tìm thấy quyền đặc biệt nào.
* Hợp đồng B: Chỉ ra hàm `mint()` tại dòng 12-14, rủi ro pha loãng token do không có trần cung cấp (`MAX_SUPPLY`).
* Hợp đồng C: Chỉ ra hàm `setRestricted()` và hàm ghi đè `_update()` tại dòng 12-19, rủi ro người dùng bị đưa vào danh sách đen khiến token không thể chuyển nhượng.

**Đánh giá:** [Đạt] Dùng được.

**Chỗ sai / Thiếu sót ban đầu:**  
Khi đọc lướt qua mã nguồn, sinh viên dễ bị đánh lừa bởi chú thích hợp lý của nhà phát triển (ví dụ `mint` để khuyến mại hoặc `restricted` để bảo vệ cộng đồng). AI hỗ trợ bóc tách trực tiếp logic thực thi của mã mà không bị chi phối bởi các dòng chú thích (comment).

**Cách sửa / Hoàn thiện:**  
Sinh viên đối chiếu số dòng thực tế trong mã nguồn Phụ lục I với kết quả AI đưa ra, bổ sung phân tích tác động tài chính đối với nhà đầu tư.

**Ai phát hiện:** Sinh viên phát hiện và đối chiếu.