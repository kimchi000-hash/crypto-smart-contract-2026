# Báo cáo Lab 4: Nhận diện hợp đồng có rủi ro

## 1. Bảng kết luận thẩm định rủi ro

| Hợp đồng | Kết luận | Tên hàm | Số dòng | Rủi ro cho người nắm giữ |
| :---: | :--- | :--- | :---: | :--- |
| **A** (`ClubTokenA`) | Sạch / Không rủi ro | Không có | — | Không có quyền đặc biệt nào; tổng cung cố định khi khởi tạo, không ai tạo thêm hay đóng băng được token. |
| **B** (`ClubTokenB`) | Có rủi ro cao | `mint` | Dòng 13–15 | Hàm có chỉ thị `onlyOwner` cho phép chủ sở hữu đúc thêm token tùy ý không có giới hạn trần (max supply), gây pha loãng nghiêm trọng giá trị token của người nắm giữ. |
| **C** (`ClubTokenC`) | Có rủi ro cao | `setRestricted` kết hợp `_update` | Dòng 13–15 và Dòng 17–20 | Chủ sở hữu có thể tùy tiện gắn cờ hạn chế địa chỉ ví bất kỳ (`restricted[user] = true`); hàm `_update` chặn chiều chuyển đi (`require(!restricted[from])`), khiến người mua bị giam vốn (mua vào được nhưng không bán ra được). |

---

## 2. Nhận xét và bài học nghiệp vụ

* **Bản chất kỹ thuật và quản trị:**  
  Cả hai hàm rủi ro ở Hợp đồng B và C đều có modifier `onlyOwner` và chú thích có vẻ chính đáng ("phục vụ khuyến mại", "bảo vệ cộng đồng"). Mã nguồn hoàn toàn hợp lệ về cú pháp Solidity, không báo lỗi biên dịch. Rủi ro ở đây xuất phát từ **thiết kế quản trị tập trung tuyệt đối**, đặt trọn niềm tin vào một cá nhân nắm giữ Private Key.
* **Góc độ thẩm định chuyên viên (BA / Risk Auditor):**  
  Chuyên viên thẩm định không chỉ đọc chú thích dự án mà phải đặt câu hỏi: *Quyền lực tối đa mà chủ sở hữu có thể thực hiện là gì? Nếu chủ dự án gian lận (Rug Pull) hoặc bị lộ Private Key thì người dùng gánh chịu hậu quả tới đâu?*
* **Giải pháp khắc phục đề xuất:**
  * **Với Hợp đồng B:** Khai báo trần tổng cung bất biến `MAX_SUPPLY = 2_000_000 * 10**18` và thêm điều kiện ràng buộc trong hàm `mint`: `require(totalSupply() + amount <= MAX_SUPPLY, "Vuot tran tong cung");`.
  * **Với Hợp đồng C:** Thêm cơ chế giới hạn thời gian tự động giải tỏa (Timelock), phát ra sự kiện `event Restricted(address indexed user, bool status)` để cộng đồng giám sát On-chain, và quy định cơ chế phân xử phi tập trung (Multi-sig) thay vì một ví đơn lẻ quyết định.
