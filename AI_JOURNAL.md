# NHẬT KÝ LÀM VIỆC VỚI AI (LAB 01 — LAB 07)
**Học phần:** Tiền điện tử & Hợp đồng thông minh (ECO2432)  
**Sinh viên:** Nguyễn Thị Kim Chi — MSSV: 23K4300025  
**Quy chuẩn áp dụng:** Mẫu B.3 và Thang đánh giá B.5 — Sổ tay thực hành ECO2432 (2026)

---

## LAB 01 — CHUẨN BỊ MÔI TRƯỜNG & QUY ƯỚC AGENTS.MD

### Lần 1
- **Prompt:**  
  *"Giải thích ngắn gọn: blockchain khác cơ sở dữ liệu thông thường ở điểm nào?"*
- **AI trả về:**  
  Liệt kê các tính chất lý thuyết chung: phi tập trung, mạng ngang hàng P2P, cơ chế đồng thuận PoW/PoS, mã hóa khóa công khai.
- **Đánh giá:** ✅ Dùng được
- **Chỗ sai / Hạn chế:**  
  Câu trả lời mang tính hàn lâm, dàn trải và chưa gắn trực tiếp với góc độ kế toán/nghiệp vụ tài chính (bản chất sổ cái phân tán không thể tẩy xóa) và cơ chế tính phí gas khi ghi dữ liệu.
- **Cách sửa:**  
  Sinh viên yêu cầu AI tóm tắt cô đọng thành 3 gạch đầu dòng nhấn mạnh vào tính bất biến (Immutability) và chi phí ghi dữ liệu; đồng thời tự bổ sung dòng quy ước vào cuối `AGENTS.md`: `// Chú thích trong mã viết bằng tiếng Việt không dấu.`
- **Ai phát hiện:** Sinh viên phát hiện và định hướng lại.

---

## LAB 02 — VÍ VÀ GIAO DỊCH ĐẦU TIÊN

### Lần 1
- **Prompt:**  
  *"Khi một giao dịch chuyển ETH hoặc gọi hợp đồng bị thất bại (Execution reverted hoặc Out of Gas) thì ví gửi có bị trừ phí gas không? Khoản phí đó trừ vào đâu?"*
- **AI trả về:**  
  AI giải thích giao dịch thất bại vẫn bị trừ phí gas do mạng lưới đã tiêu hao tài nguyên tính toán của máy ảo EVM. Tuy nhiên, AI lại diễn đạt: *"khoản phí gas được khấu trừ trực tiếp vào số tiền người gửi định chuyển"*.
- **Đánh giá:** ⚠️ Phải sửa
- **Chỗ sai:**  
  Sai lầm nghiêm trọng về quy tắc kế toán blockchain: Phí giao dịch (gas) luôn luôn được trừ thẳng vào số dư đồng tiền gốc (ETH) của ví gửi, hoàn toàn độc lập với giá trị chuyển (`Value`). Nếu giao dịch thất bại, giá trị chuyển được giữ nguyên trong ví, chỉ có phí gas thực tế (`TxFee = gasUsed × gasPrice`) bị trừ mất.
- **Cách sửa:**  
  Sinh viên đối chiếu số dư thực tế trên ví MetaMask và Sepolia Etherscan sau khi giao dịch thất bại, bác bỏ giải thích sai của AI và chuẩn hóa lại công thức trong `lab02.md`: `Số tiền thực trừ = 0 ETH chuyển + TxFee`.
- **Ai phát hiện:** Sinh viên phát hiện.

---

## LAB 03 & 3B — ĐỌC GIAO DỊCH ETHERSCAN & TRUY VẾT DÒNG TIỀN BYBIT

### Lần 1 (Lab 3: Phân tích hợp đồng USDT & Proxy)
- **Prompt:**  
  *"Kiểm tra hợp đồng Tether USD 0xdAC17F958D2ee523a2206206994597C13D831ec7 trên Etherscan. Hợp đồng có mã nguồn đã xác thực không? Có hàm nào cho phép khóa tài khoản người khác không?"*
- **AI trả về:**  
  Chỉ ra chính xác hợp đồng đã verified, có hàm `addBlackList(address _evilUser)` trong tab Write Contract. Tuy nhiên, AI lại khẳng định USDT là hợp đồng Proxy chuẩn ERC-1967 và hướng dẫn mở tab *Read as Proxy*.
- **Đánh giá:** ⚠️ Phải sửa
- **Chỗ sai:**  
  AI nhầm lẫn giữa cấu trúc Proxy của USDC (`0xA0b8...` - dùng chuẩn EIP-1967) với USDT (`0xdAC1...`). Hợp đồng USDT trên Ethereum Mainnet hiển thị trực tiếp toàn bộ hàm nghiệp vụ trong tab Read/Write Contract mà không cần chuyển sang tab con Proxy.
- **Cách sửa:**  
  Sinh viên truy cập trực tiếp Etherscan, kiểm chứng giao diện thực tế của hợp đồng USDT để đính chính vào báo cáo `forensics.md`.
- **Ai phát hiện:** Sinh viên phát hiện.

### Lần 2 (Lab 3B: Phân tích giao dịch gốc vụ hack Bybit 401.346 ETH)
- **Prompt:**  
  *"Bạn là chuyên viên phân tích on-chain. Dưới đây là dữ liệu tôi copy từ Etherscan của một giao dịch Ethereum (tx hash: 0xb61413c495fdad6114a7aa863a00b2e3c28945979a10885b12b30316ea9f072c). Hãy: 1. Giải thích vì sao 'Value' = 0 ETH nhưng vẫn có 401.346 ETH được chuyển. 2. Phân biệt ví 'From', ví 'To' và ví nhận tiền cuối cùng — ví nào là của nạn nhân, ví nào là của kẻ tấn công? Nêu lý do. Chỉ trả lời dựa trên dữ liệu tôi cung cấp. Nếu không có trong dữ liệu, nói là không có."*
- **AI trả về:**  
  Giải thích chính xác cơ chế Internal Transaction: giá trị Value hiển thị 0 ETH vì đây là lời gọi ngoài (top-level call), số tiền 401.346 ETH thực sự di chuyển trong `Internal Txns` qua lệnh `DELEGATECALL` sang bản cài đặt độc hại trên ví đa chữ ký Gnosis Safe của Bybit. Phân định đúng ví From là EOA của hacker, ví To là ví lạnh Bybit (Safe proxy), ví nhận cuối cùng là ví hacker (Hop 0: `0x4766...`).
- **Đánh giá:** ✅ Dùng được
- **Chỗ sai ban đầu của AI (nếu không ràng buộc dữ liệu):**  
  Khi hỏi tự do không dán dữ liệu Etherscan, AI tự suy đoán ("ảo giác") rằng Bybit bị lộ khóa riêng tư (private key) của ví nóng (hot wallet), đồng thời bịa số dư ví hacker hiện tại.
- **Cách sửa:**  
  Ràng buộc chặt prompt chỉ dựa trên dữ liệu thực tế trích xuất từ Etherscan và API Blockscout, đối chiếu chéo TxHash để đảm bảo độ tin cậy 100% trong `trace.md`.
- **Ai phát hiện:** Sinh viên phát hiện và kiểm chứng on-chain.

---

## LAB 04 — NHẬN DIỆN HỢP ĐỒNG CÓ RỦI RO

### Lần 1
- **Prompt:**  
  *"Bạn là chuyên viên thẩm định rủi ro tài sản số. Dưới đây là mã nguồn một hợp đồng token. Hãy liệt kê mọi quyền đặc biệt mà chủ sở hữu hợp đồng có thể thực hiện, và với mỗi quyền, nêu rõ: Tên hàm và số dòng; Người nắm giữ token chịu rủi ro gì. Chỉ trả lời dựa trên mã nguồn tôi cung cấp. Nếu không tìm thấy, nói là không tìm thấy. [dán mã nguồn ClubTokenA, ClubTokenB, ClubTokenC]"*
- **AI trả về:**  
  - Hợp đồng A: Không tìm thấy quyền đặc biệt nào.
  - Hợp đồng B: Chỉ ra hàm `mint()` tại dòng 12-14, rủi ro pha loãng token do không có trần cung cấp (`MAX_SUPPLY`).
  - Hợp đồng C: Chỉ ra hàm `setRestricted()` và hàm ghi đè `_update()` tại dòng 12-19, rủi ro người dùng bị đưa vào danh sách đen khiến token không thể chuyển nhượng.
- **Đánh giá:** ✅ Dùng được
- **So sánh đọc thủ công và AI hỗ trợ:**  
  - *Đọc thủ công tìm ra gì:* Sinh viên đọc 15 phút ban đầu nhận thấy hợp đồng B có hàm `mint()` cho phép tạo thêm token và hợp đồng C có biến/mapping liên quan đến hạn chế chuyển nhượng, nhưng dễ bị phân tâm bởi các đoạn comment mang tính ngụy biện (ví dụ: chú thích phục vụ khuyến mại hoặc bảo vệ cộng đồng).
  - *AI tìm thêm được gì:* AI trích xuất chính xác dòng lệnh thực thi (hàm `mint` dòng 12-14 ở Contract B và hàm `setRestricted` kết hợp `_update` dòng 12-19 ở Contract C); chỉ rõ mô hình bẫy thanh khoản (honeypot: cho mua nhưng cấm bán) và nguy cơ lạm phát vô hạn.
  - *AI có nói sai chỗ nào không:* Nếu bỏ câu chốt chặn *"Chỉ trả lời dựa trên mã nguồn tôi cung cấp"*, AI có xu hướng bịa thêm các lỗi bảo mật phổ biến như reentrancy hoặc flash loan dù mã nguồn không có. Khi dùng prompt chuẩn, AI đã tập trung đúng phạm vi mã được cung cấp.
- **Cách sửa:**  
  Sinh viên đối chiếu số dòng thực tế trong mã nguồn `contracts/lab04/ClubTokens.sol` với kết quả AI đưa ra, bổ sung phân tích tác động tài chính vào bảng `lab04.md`.
- **Ai phát hiện:** Sinh viên tự đọc phát hiện trước, sau đó dùng AI để rà soát chi tiết số dòng và củng cố lập luận.

---

## LAB 05 — VIẾT ĐẶC TẢ CHO CÔNG CỤ PHÂN TÍCH DÒNG TIỀN

### Lần 1
- **Prompt:**  
  *"Xây dựng một công cụ nhận vào địa chỉ ví Ethereum, trả về báo cáo dòng tiền vào và ra của ví đó trong 90 ngày gần nhất, kèm biểu đồ số dư theo thời gian."*
- **AI trả về:**  
  AI lập tức viết ngay một kịch bản mã nguồn Python hoàn chỉnh dùng thư viện `web3.py` và `matplotlib`.
- **Đánh giá:** ❌ Sai, bỏ
- **Chỗ sai:**  
  AI vi phạm nghiêm trọng yêu cầu và phương pháp sư phạm của Buổi 5: *"KHÔNG VIẾT MÃ NGUỒN TRONG BUỔI NÀY"*. AI có xu hướng nhảy cóc vào sinh mã khi chưa có bản đặc tả nghiệp vụ (SPEC), dẫn đến việc mã nguồn tự suy đoán sai các quy tắc nghiệp vụ (bỏ qua phí gas của failed tx, không phân trang, không xử lý ngoại lệ rỗng).
- **Cách sửa:**  
  Sinh viên hủy bỏ toàn bộ đoạn mã do AI tự sinh; yêu cầu AI quay trở lại vai trò Chuyên viên Phân tích Nghiệp vụ (BA) và xây dựng tài liệu `SPEC.md` theo chuẩn Mục B.2 gồm đủ 6 phần: Mục đích, Đầu vào, Quy tắc R1-R7, Đầu ra, Ngoại lệ E1-E3 và Ngoài phạm vi.
- **Ai phát hiện:** Sinh viên phát hiện và chấn chỉnh quy trình.

---

## LAB 06 — SINH MÃ BẰNG AI VÀ KIỂM TRA KẾT QUẢ

### Lần 1 (Lỗi nghiệp vụ tính phí giao dịch thất bại)
- **Prompt:**  
  *"Đọc tệp SPEC.md trong dự án và viết chương trình Python thực hiện đúng đặc tả đó. Tuân thủ các quy ước trong AGENTS.md."*
- **AI trả về:**  
  Sinh kịch bản `analyze_cashflow.py` kết nối Etherscan API và vẽ biểu đồ `cashflow_90days.png`.
- **Đánh giá:** ⚠️ Phải sửa
- **Chỗ sai:**  
  AI sử dụng lệnh `continue` bỏ qua toàn bộ các giao dịch có `isError == '1'`. Điều này dẫn đến việc bỏ qua khoản phí gas mà ví gửi phải trả cho mạng lưới, vi phạm trực tiếp Quy tắc R4 trong `SPEC.md` và làm sai lệch nghiêm trọng số dư lũy kế cuối kỳ.
- **Cách sửa:**  
  Sinh viên bổ sung logic: Khi `isError == '1'` và ví đang xét là người gửi (`from == target`), giá trị chuyển bằng 0 nhưng vẫn phải trừ phí gas thực tế `TxFee = (gasUsed × gasPrice) / 10^18` vào dòng tiền ra.
- **Ai phát hiện:** Sinh viên phát hiện khi đối chiếu với Quy tắc R4.

### Lần 2 (Lỗi thiếu cơ chế phân trang)
- **Prompt:**  
  *"Kiểm tra lại cơ chế kéo dữ liệu lịch sử giao dịch khi số lượng giao dịch của ví vượt quá giới hạn một trang API."*
- **AI trả về:**  
  Mã nguồn ban đầu chỉ gửi 1 HTTP GET request duy nhất với tham số mặc định `page=1, offset=10000`.
- **Đánh giá:** ⚠️ Phải sửa
- **Chỗ sai:**  
  Thiếu vòng lặp phân trang tự động (Pagination) khi số lượng giao dịch vượt ngưỡng hạn mức một lần gọi (vi phạm trường hợp ngoại lệ E3 trong `SPEC.md`). Nếu ví có trên 10.000 giao dịch, chương trình sẽ làm mất toàn bộ các giao dịch ở các trang sau.
- **Cách sửa:**  
  Sinh viên chỉ đạo viết vòng lặp `while True`, tự động tăng biến `page += 1` sau mỗi lần nhận đủ dữ liệu và dừng lại khi kết quả trả về mảng rỗng.
- **Ai phát hiện:** Sinh viên phát hiện.

### Lần 3 (Lỗi sử dụng phiên bản API cũ đã ngừng hỗ trợ)
- **Prompt:**  
  *"Rà soát lại endpoint kết nối API Etherscan trong mã nguồn xem đã đúng chuẩn hiện hành chưa."*
- **AI trả về:**  
  AI vẫn giữ endpoint truyền thống: `https://api.etherscan.io/api`.
- **Đánh giá:** ⚠️ Phải sửa
- **Chỗ sai:**  
  Do dữ liệu huấn luyện cũ, AI sử dụng API V1 cũ. Etherscan hiện đã chuyển đổi sang cổng API V2 hợp nhất (`https://api.etherscan.io/v2/api`) yêu cầu bắt buộc phải truyền thêm tham số `chainid` (ví dụ: `chainid=1` cho Ethereum Mainnet). Endpoint cũ có nguy cơ bị từ chối phục vụ hoặc giới hạn lưu lượng ngặt nghèo.
- **Cách sửa:**  
  Sinh viên mở tài liệu chính thức Etherscan Developer APIs, yêu cầu AI cập nhật toàn bộ URL sang `https://api.etherscan.io/v2/api` và bổ sung tham số `chain_id` trong mọi request.
- **Ai phát hiện:** Sinh viên đối chiếu tài liệu chính thức và phát hiện.

---

## LAB 07 — TÍNH CHI PHÍ VẬN HÀNH THỰC TẾ

### Lần 1 (Lỗi tính nhầm lũy thừa đơn vị Gwei / ETH)
- **Prompt:**  
  *"Tính chi phí vận hành hàng tháng cho 1.000 giao dịch ghi Storage (20.000 gas/lượt) trên Ethereum L1 với đơn giá gas 20 Gwei và giá ETH 3.000 USD."*
- **AI trả về:**  
  AI đưa ra kết quả tính toán chi phí 1 tháng là **12.000 USD** (thay vì 1.200 USD).
- **Đánh giá:** ❌ Sai, bỏ
- **Chỗ sai:**  
  AI thực hiện sai phép đổi đơn vị lũy thừa: lấy `20.000 × 20 Gwei = 400.000 Gwei` rồi đổi sang ETH bằng cách nhân `10^-8` thay vì `10^-9`. Điều này dẫn đến phí 1 giao dịch bị đội lên gấp 10 lần (`0.004 ETH` thay vì `0.0004 ETH`), làm sai lệch toàn bộ bức tranh tài chính của sản phẩm.
- **Cách sửa:**  
  Sinh viên áp dụng đúng công thức tại Phụ lục L.1 của Sổ tay:  
  `Phí 1 tx (ETH) = 20.000 × 20 × 10^-9 = 0.0004 ETH`.  
  `Phí 1 tx (USD) = 0.0004 × 3.000 = 1.2 USD`.  
  `Tổng 1.000 tx = 1.200 USD/tháng (~30.000.000 VNĐ)`.  
  Sinh viên yêu cầu AI cập nhật lại toàn bộ bảng tính trong `lab07.md`.
- **Ai phát hiện:** Sinh viên phát hiện.

### Lần 2 (Bỏ sót chi phí cố định khi mở rộng sang đề tài nhóm)
- **Prompt:**  
  *"Áp dụng khung tính toán chi phí cho đề tài đồ án nhóm: Hệ thống Bỏ phiếu bầu Ban chủ nhiệm CLB / Ban cán sự phi tập trung quy mô 500 cử tri."*
- **AI trả về:**  
  AI chỉ nhân đơn thuần 500 cử tri với chi phí của hàm `vote()` (~48.000 gas/lượt).
- **Đánh giá:** ⚠️ Phải sửa
- **Chỗ sai:**  
  Bỏ sót hai hạng mục chi phí on-chain cố định ban đầu cực kỳ quan trọng:
  1. Chi phí triển khai hợp đồng (`Deploy SimpleVoting`): ~700.000 gas.
  2. Chi phí đăng ký danh sách 500 cử tri hợp lệ theo lô (`registerVoters` batch 10 lô): ~1.200.000 gas.
  Nếu bỏ sót, tổng chi phí dự toán của dự án sẽ bị thiếu hụt khoảng 1.900.000 gas (~114 USD trên L1).
- **Cách sửa:**  
  Sinh viên bổ sung đầy đủ 4 hạng mục (Deploy, Batch Register, Vote, Read Results) vào Bảng ước tính chi phí tại Mục 4 của `lab07.md`, hoàn thiện bài toán tài chính toàn diện cho đồ án.
- **Ai phát hiện:** Sinh viên phát hiện.