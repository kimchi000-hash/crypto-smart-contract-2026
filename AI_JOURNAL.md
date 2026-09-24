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

---

## Lần 2 - Lab 3B: Truy vết dòng tiền vụ hack Bybit (Follow the Money)
**Prompt:**  
"Bạn là chuyên viên phân tích on-chain. Dưới đây là dữ liệu tôi copy từ Etherscan của một giao dịch Ethereum (tx hash: 0xb61413c495fdad6114a7aa863a00b2e3c28945979a10885b12b30316ea9f072c). Hãy: 1. Giải thích vì sao 'Value' = 0 ETH nhưng vẫn có 401.346 ETH được chuyển. 2. Phân biệt ví 'From', ví 'To' và ví nhận tiền cuối cùng — ví nào là của nạn nhân, ví nào là của kẻ tấn công? Nêu lý do. Chỉ trả lời dựa trên dữ liệu tôi cung cấp. Nếu không có trong dữ liệu, nói là không có."

**AI trả về:**  
* Giải thích chính xác cơ chế Internal Transaction: giá trị Value hiển thị 0 ETH vì đây là lời gọi hợp đồng ngoài (top-level call), số tiền 401.346 ETH thực sự di chuyển trong `Internal Txns` thông qua cơ chế `DELEGATECALL` sang bản cài đặt độc hại được kích hoạt trên ví đa chữ ký Gnosis Safe của Bybit.
* Phân định đúng: Ví From là EOA kẻ tấn công ký lệnh khởi tạo; ví To là ví lạnh Bybit (Safe proxy contract); ví nhận tiền cuối cùng là ví hacker (Hop 0: `0x4766...`).

**Đánh giá:** [Đạt] Phân tích kỹ thuật chính xác khi được cung cấp dữ liệu đầu vào cụ thể.

**Chỗ sai / Thiếu sót ban đầu:**  
Khi hỏi chung về vụ hack mà không giới hạn dữ liệu Etherscan, LLM có xu hướng tự suy đoán ("ảo giác" / hallucination) rằng Bybit bị lộ private key hoặc ví nóng bị xâm nhập, đồng thời tự đưa ra số dư hiện tại của ví hacker mà không kiểm chứng thời gian thực. Ngoài ra, LLM dễ nhầm lẫn giữa giờ hệ thống địa phương và giờ chuẩn UTC nếu prompt không chỉ định rõ.

**Cách sửa / Hoàn thiện:**  
Ép AI làm việc trực tiếp trên dữ liệu thật lấy từ tab Overview & Internal Txns của Etherscan và API Blockscout (`curl` lấy số dư và danh sách transaction). Đối chiếu chéo mã băm giao dịch (TxHash) thực tế trên Etherscan để đảm bảo tính xác thực 100%.

**Ai phát hiện:** Sinh viên kiểm chứng và đối chiếu on-chain.