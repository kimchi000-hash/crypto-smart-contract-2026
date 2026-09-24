# Báo cáo Lab 2: Ví và giao dịch đầu tiên

## 1. Bảng đối chiếu thông tin giao dịch

| Trường | Giao dịch thành công | Giao dịch thất bại |
| :--- | :--- | :--- |
| **Mã băm giao dịch** | 0xc27d5ede709b8db72206ab6aedc3aaad14f3197813519efbcf69ebf3ee1c0ed2 | 0x3c47668df9440f721d4ebbfe5afa1a444f2ba5f744b54ecbdd9a338ad31d4ed6 |
| **Số tiền chuyển** | 0.1 Sepolia ETH | 0 ETH |
| **Phí giao dịch thực trả** | 0.000000002595648489 ETH | 
0.000054427662744246 ETH |
| **Trạng thái** | Confirmed / Success | Rejected (Insufficient funds) |
| **Nguyên nhân (nếu thất bại)** | Không có | Do ví chưa gửi tiền vào hợp đồng nên vi phạm điều kiện kiểm tra số dư (require) trong hàm collect/attack, dẫn đến EVM hủy giao dịch (Execution reverted) |

## 2. Trả lời câu hỏi nghiệp vụ
**Câu hỏi:** *Nếu bạn chuyển nhầm cho người lạ, có lấy lại được không? Vì sao?*

**Trả lời:**
1. Nếu bạn đã chuyển nhầm tài sản cho người lạ trên mạng blockchain, bạn hoàn toàn không thể tự ý lấy lại khoản tiền đó.
2. Tính chất bất biến (immutability) của blockchain quy định các giao dịch sau khi đã đóng gói vào khối và xác nhận thì không một cá nhân, tổ chức hay sàn giao dịch nào có thể can thiệp đảo ngược.
3. Cách duy nhất để lấy lại tiền là người nhận có thiện chí tự nguyện tạo một giao dịch mới để gửi trả lại cho bạn.