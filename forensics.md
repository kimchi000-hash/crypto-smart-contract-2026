# Báo cáo Lab 3: Đọc giao dịch và hợp đồng trên Etherscan

## 1. Mổ xẻ giao dịch cá nhân (Giao dịch từ Lab 2)
* Mã băm giao dịch (TxHash): 0xc27d5ede709b8db72206ab6aedc3aaad14f3197813519efbcf69ebf3ee1c0ed2

| Trường | Giá trị trong giao dịch | Ý nghĩa kỹ thuật | Vì sao người làm nghiệp vụ cần |
| :--- | :--- | :--- | :--- |
| **Status** | Success | Trạng thái thành công hay thất bại của giao dịch | Giao dịch thất bại vẫn bị trừ phí gas, ảnh hưởng trực tiếp đến hạch toán chi phí |
| **Block** | 11673504 | Số thứ tự của khối chứa giao dịch đã được xác thực | Xác định thời điểm chính thức ghi nhận giao dịch vào sổ cái |
| **Timestamp** | Sep-10-2026 02:33:36 PM UTC+07 | Thời gian giao dịch được đào vào khối | Làm mốc thời gian ghi nhận doanh thu, công nợ hoặc chi phí theo kỳ kế toán |
| **From / To** | From: 0xf8242815A45Aa13006a841b02677fB5853d96350 To: 0xFB6DB8dc3ff4C62B92C9935bE86057beCCAd7E07 | Địa chỉ ví gửi và địa chỉ ví nhận | Đối tượng cần kiểm tra tuân thủ, xác minh danh tính và truy vết dòng tiền (AML/KYC) |
| **Value** | 0.1 ETH | Số lượng tài sản cơ sở được chuyển giao dịch | Ghi nhận giá trị tài sản chuyển dịch trong giao dịch |
| **Transaction Fee** | 0.000000002595648489 ETH | Chi phí thực tế người gửi phải trả cho thợ đào/trình xác thực | Khoản chi phí vận hành cần được hạch toán riêng biệt với giá trị chuyển |
| **Gas Price** | 2.595648489 Gwei | Đơn giá cho mỗi đơn vị gas tại thời điểm xử lý | Giải thích nguyên nhân biến động chi phí giữa các thời điểm mạng nghẽn hoặc thông thoáng |
| **Nonce** | 33 | Số thứ tự tăng dần của giao dịch do ví gửi phát đi | Đối chiếu tránh giao dịch bị trùng lặp, phát hiện giao dịch bị kẹt hoặc bị thay thế |

---

## 2. Đọc và phân tích hợp đồng thực tế (Tether USD - USDT)
* Địa chỉ hợp đồng: `0xdAC17F958D2ee523a2206206994597C13D831ec7`

### Trả lời câu hỏi nghiệp vụ:
1. **Hợp đồng bạn xem có công bố mã nguồn đã xác thực không?**
   * Có. Hợp đồng USDT trên Etherscan hiển thị nhãn **Contract Source Code Verified** với dấu tick xanh. Điều này chứng minh mã nguồn Solidity công khai đã được trình biên dịch đối chiếu khớp chính xác với mã máy bytecode đang thực thi.

2. **Tổng cung của đồng đó là bao nhiêu? Đọc ra từ hàm nào?**
   * Được đọc từ hàm **`totalSupply()`** trong tab *Read Contract*. 
   * Giá trị đọc được thể hiện tổng lượng token phát hành (chia cho 10^6 do USDT sử dụng 6 decimals).

3. **Trong tab Write Contract, có hàm nào cho phép một địa chỉ đặc biệt đóng băng tài khoản người khác không? Nếu có, tên hàm là gì?**
   * Có. Hợp đồng USDT có hàm **`addBlackList(address _evilUser)`** trong tab *Write Contract*.
   * Hàm này cho phép chủ sở hữu hợp đồng (`owner`) đưa bất kỳ địa chỉ ví nào vào danh sách hạn chế, chặn hoàn toàn khả năng chuyển nhận USDT của địa chỉ đó.