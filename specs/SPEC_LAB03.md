# SPEC — LAB 03 & 3B: ĐỌC GIAO DỊCH & ĐIỀU TRA DÒNG TIỀN ON-CHAIN

## 1. Mục đích
Đóng vai trò chuyên viên phòng chống rửa tiền (AML) và điều tra on-chain để mổ xẻ 10 trường dữ liệu cốt lõi của giao dịch trên Etherscan, truy vết dòng tiền 401.346 ETH bị đánh cắp trong sự cố ví lạnh Bybit qua các trạm trung gian (Hop 0 đến Hop 2), trích xuất thông điệp nhúng trong blockchain và phân biệt bản chất định danh tài sản số.

## 2. Đầu vào
- Mã băm giao dịch gốc (TxHash) vụ hack trên Ethereum Mainnet: `0xb61413c495fdad6114a7aa863a00b2e3c28945979a10885b12b30316ea9f072c`.
- Địa chỉ ví lạnh Safe của nạn nhân (Bybit) và địa chỉ ví của kẻ tấn công (Hacker Hop 0).
- Dữ liệu thô từ Etherscan (tab Overview, Internal Transactions, Contract Source Code, Logs) và API Blockscout.

## 3. Quy tắc nghiệp vụ
- R1: Giao dịch gốc hiển thị trường `Value = 0 ETH` vì toàn bộ 401.346 ETH thực tế được chuyển thông qua các lệnh gọi nội bộ (`Internal Transactions` kích hoạt bằng lệnh `DELEGATECALL` sang implementation contract độc hại).
- R2: Lập bảng phân tích và bóc tách các mốc giao dịch phân tán tiền có giá trị tròn đúng 10.000 ETH (kỹ thuật phân tầng - Layering trong quy trình rửa tiền).
- R3: Giải mã thông điệp ẩn giấu trong trường `Input Data` (Hex format) của các giao dịch tống tiền hoặc giao tiếp on-chain sang bảng mã UTF-8.
- R4: Đối chiếu và giải thích đủ 10 trường dữ liệu chuẩn của giao dịch cá nhân theo mẫu báo cáo Etherscan.

## 4. Đầu ra
- Tệp báo cáo `forensics.md` hoàn chỉnh đủ 10 trường kỹ thuật của giao dịch và phân tích hợp đồng USDT (đọc hàm `totalSupply()`, quyền hạn chế `addBlackList`).
- Tệp báo cáo `trace.md` ghi nhận đủ 4 trạm điều tra, sơ đồ dòng tiền từ Bybit tới Hop 3, và khuyến nghị nghiệp vụ tuân thủ (AML) cho sàn giao dịch.
- Đoạn lập luận phân biệt bản chất Vô danh (Anonymous) và Bút danh/Giả danh (Pseudonymous) của mạng Ethereum.

## 5. Trường hợp ngoại lệ
- E1: Nếu trường `Input Data` chứa mã bytecode thực thi của hàm chứ không phải chuỗi văn bản thì công cụ giải mã UTF-8 trả về ký tự không đọc được, buộc chuyên viên phải đối chiếu ABI để giải mã tham số.
- E2: Nếu dòng tiền bị đưa vào các giải pháp trộn tiền (như Tornado Cash) hoặc các cầu nối cross-chain (như THORChain) thì chuỗi truy vết trực tiếp trên Ethereum bị đứt gãy.
- E3: Nếu dữ liệu API bên thứ ba (như Blockscout) bị sai lệch hoặc hiển thị chưa kịp đồng bộ số dư thì chuyên viên phải đối chiếu chéo trực tiếp trên Etherscan.

## 6. Ngoài phạm vi
- Không thực hiện các hành động can thiệp đóng băng hay thu hồi tài sản on-chain của hacker.
- Không phân tích chi tiết lỗ hổng phía giao diện web (UI/Frontend spoofing) ngoài phạm vi hợp đồng thông minh.
