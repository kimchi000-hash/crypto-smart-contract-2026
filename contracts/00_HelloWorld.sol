// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;

/// @title Hello World Smart Contract with Access Control
/// @notice Hợp đồng mở rộng có phân quyền chỉ Owner mới được thay đổi nội dung
contract HelloWorld {
    // Định nghĩa lỗi tùy chỉnh để tiết kiệm gas
    error NotOwner();

    // 1. Biến trạng thái (State Variables)
    address public immutable i_owner;
    string private s_greeting;
    uint256 public s_updateCount;

    // 2. Sự kiện (Events)
    event GreetingChanged(
        address indexed updater,
        string oldGreeting,
        string newGreeting,
        uint256 timestamp
    );

    // 3. Hàm khởi tạo (Lưu địa chỉ người deploy vào i_owner)
    constructor(string memory _initialGreeting) {
        i_owner = msg.sender;
        s_greeting = _initialGreeting;
        s_updateCount = 0;
    }

    // 4. Hàm Ghi - có kiểm tra điều kiện quyền Owner
    function setGreeting(string calldata _newGreeting) external {
        if (msg.sender != i_owner) {
            revert NotOwner();
        }

        string memory oldGreeting = s_greeting;
        s_greeting = _newGreeting;
        unchecked {
            ++s_updateCount;
        }
        emit GreetingChanged(msg.sender, oldGreeting, _newGreeting, block.timestamp);
    }

    // 5. Hàm Đọc
    function getGreeting() external view returns (string memory) {
        return s_greeting;
    }
}