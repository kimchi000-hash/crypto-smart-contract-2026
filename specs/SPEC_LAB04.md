# SPEC — LAB 04: NHẬN DIỆN HỢP ĐỒNG CÓ RỦI RO

## 1. Mục đích
Đóng vai trò chuyên viên thẩm định rủi ro tài sản số rà soát mã nguồn 3 hợp đồng mẫu trong `contracts/lab04/ClubTokens.sol` để phát hiện và chỉ ra các điều khoản bất lợi, nguy cơ lừa đảo (honeypot hoặc rugpull) cho nhà đầu tư kèm trích dẫn số dòng cụ thể làm bằng chứng.

## 2. Đầu vào
- Mã nguồn Solidity của 3 hợp đồng token: `ClubTokenA`, `ClubTokenB`, `ClubTokenC` trong thư mục `contracts/lab04/ClubTokens.sol`.
- Mẫu câu lệnh chuẩn (prompt template) dành cho chuyên viên thẩm định có ràng buộc chống AI suy đoán/ảo giác.

## 3. Quy tắc nghiệp vụ
- R1: Mọi kết luận thẩm định rủi ro bắt buộc phải trích dẫn chính xác tên hàm, số dòng và rủi ro cụ thể cho người nắm giữ token.
- R2: Nhận diện cơ chế lạm phát vô hạn tại Hợp đồng B: hàm `mint` có điều kiện `onlyOwner` không có trần cung ứng (`MAX_SUPPLY`), cho phép chủ sở hữu tự ý tạo thêm token làm pha loãng nghiêm trọng giá trị tài sản của người nắm giữ.
- R3: Nhận diện cơ chế khóa thanh khoản (Honeypot) tại Hợp đồng C: hàm `setRestricted` kết hợp logic ghi đè trong `_update` cho phép chủ sở hữu chặn quyền chuyển nhượng của ví bất kỳ (cho phép mua vào nhưng cấm bán ra).
- R4: Đối chiếu quy trình thẩm định thủ công độc lập (15 phút đầu) với kết quả rà soát từ công cụ AI để ghi nhận sự khác biệt.

## 4. Đầu ra
- Bảng kết luận thẩm định rủi ro hoàn chỉnh trong tệp `lab04.md` gồm các cột: Hợp đồng, Địa chỉ Sepolia, Kết luận, Tên hàm, Số dòng vi phạm, Rủi ro cho người nắm giữ.
- Mục nhật ký làm việc trong `AI_JOURNAL.md` đối chiếu rõ 3 khía cạnh: Đọc thủ công tìm ra gì, AI tìm thêm được gì, AI có nói sai chỗ nào không.

## 5. Trường hợp ngoại lệ
- E1: Nếu hợp đồng chuẩn sạch (Hợp đồng A) tuân thủ đúng chuẩn ERC-20 và không có quyền quản trị đặc biệt thì hệ thống phải kết luận an toàn, không được tự bịa ra lỗ hổng.
- E2: Nếu mã nguồn hợp đồng bị làm rối (obfuscated) hoặc che giấu qua các hàm kế thừa lồng nhau thì chuyên viên phải truy ngược đến logic thực thi cuối cùng trong `_update`.
- E3: Nếu công cụ AI tự suy đoán và liệt kê các lỗ hổng bảo mật không tồn tại trong code (như lỗi tái nhập reentrancy hay flash loan) thì sinh viên phải đối chiếu mã nguồn thực tế để bác bỏ.

## 6. Ngoài phạm vi
- Không viết kịch bản khai thác tấn công (exploit script).
- Không can thiệp sửa đổi hay tái triển khai mã nguồn của các hợp đồng token mẫu.
