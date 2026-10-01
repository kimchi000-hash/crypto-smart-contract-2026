# SPEC — CÔNG CỤ PHÂN TÍCH DÒNG TIỀN VÍ ON-CHAIN (90 NGÀY)

## 1. Mục đích
Hệ thống này giúp chuyên viên phân tích nghiệp vụ và tuân thủ (AML) theo dõi, tổng hợp toàn bộ dòng tiền ETH vào/ra và biến động số dư theo thời gian của một ví chỉ định trên blockchain Ethereum.

## 2. Đầu vào
- Một địa chỉ ví Ethereum, dạng chuỗi 42 ký tự bắt đầu bằng `0x`.
- Khóa API của Etherscan (`ETHERSCAN_API_KEY`), đọc trực tiếp từ biến môi trường (tệp `.env`).
- Số ngày cần phân tích: mặc định là 90 ngày tính từ thời điểm chạy báo cáo.

## 3. Quy tắc nghiệp vụ
- R1: Giao dịch có trường `to` trùng địa chỉ đang xét được tính là **dòng tiền vào (IN)**.
- R2: Giao dịch có trường `from` trùng địa chỉ đang xét được tính là **dòng tiền ra (OUT)**.
- R3: Với giao dịch đi ra (OUT), số tiền thực trừ khỏi ví = **giá trị chuyển (Value) + phí giao dịch thực tế (TxFee)**.
- R4: Giao dịch có trạng thái thất bại (Failed) vẫn bị trừ phí gas mạng, do đó phí giao dịch vẫn phải được tính vào dòng tiền ra.
- R5: Mọi số liệu tiền tệ lấy về ở đơn vị `wei` phải được quy đổi sang `ETH` (chia cho 10^18) trước khi xử lý và hiển thị.
- R6: Dữ liệu giao dịch phải được sắp xếp theo trình tự thời gian tăng dần (`timeStamp`).
- R7: Bổ sung cảnh báo gian lận/rửa tiền nếu xuất hiện các giao dịch thử nghiệm (Test Txn <= 0.01 ETH) hoặc giao dịch tròn tiền đột biến.

## 4. Đầu ra
- Bảng dữ liệu sạch gồm các cột: Thời gian (Datetime UTC), Loại giao dịch (IN/OUT), Số tiền ETH, Phí giao dịch (ETH), Số dư lũy kế.
- Một biểu đồ đường (Line Chart): trục hoành (X) là thời gian, trục tung (Y) là số dư ETH lũy kế.
- Ba con số tổng hợp: Tổng ETH vào, Tổng ETH ra, Số dư cuối kỳ.

## 5. Trường hợp ngoại lệ
- E1: Nếu API trả về danh sách rỗng -> In thông báo `"Vi khong co giao dich trong ky"` và dừng xử lý, không báo lỗi hệ thống.
- E2: Nếu API trả về mã lỗi (sai API Key, hết hạn mức rate-limit) -> In mã lỗi rõ ràng và dừng lại, không tiếp tục tính toán.
- E3: Nếu ví có nhiều hơn 10.000 giao dịch (vượt hạn mức 1 lần gọi API) -> Hệ thống phải tự động phân trang (Pagination) để kéo đủ toàn bộ giao dịch trước khi phân tích.

## 6. Ngoài phạm vi
- Không phân tích giao dịch của các loại token ERC-20 / ERC-721 (chỉ tập trung ETH gốc).
- Không thực hiện quy đổi giá trị sang tiền pháp định (VND hoặc USD).

---

## 7. Nhận xét kiểm tra chéo (Peer Review từ nhóm bạn)
- **Nhóm rà soát chéo:** Nhóm bạn bàn bên (Nhóm Đồ án Ký quỹ thương mại)
- **Các điểm mơ hồ được chỉ ra và cách làm rõ:**
  1. *Điểm mơ hồ 1:* Trong mục 3, quy tắc R1 (`to`) và R2 (`from`) chưa nói rõ trường hợp ví tự gửi cho chính mình (`from == to == target`). Nếu áp dụng máy móc cả R1 và R2 sẽ bị tính trùng hai lần dòng tiền.
     - *Cách giải quyết:* Đã làm rõ trong logic xử lý: Nếu ví tự chuyển cho chính mình, giá trị chuyển ròng bằng 0 (không ghi nhận biến động tăng giảm tiền gửi), nhưng tài khoản vẫn bị trừ khoản phí gas thực tế phát sinh (`TxFee`) và ghi nhận vào dòng tiền ra (`OUT`).
  2. *Điểm mơ hồ 2:* Khái niệm "90 ngày gần nhất" ở Mục 2 chưa xác định rõ mốc tính từ đầu ngày theo giờ Việt Nam hay theo giờ hệ thống blockchain (UTC).
     - *Cách giải quyết:* Chuẩn hóa mốc thời gian phân tích: `start_timestamp = current_timestamp - (90 * 86.400 giây)` tính theo chuẩn Unix Timestamp (UTC) để đồng bộ tuyệt đối với dữ liệu khối của Ethereum và API Etherscan.
- **Kết luận:** Đặc tả đã được rà soát kỹ lưỡng, đủ rõ ràng và chặt chẽ để chuyển giao cho công cụ AI sinh mã mà không phát sinh hiểu nhầm về mặt nghiệp vụ.
