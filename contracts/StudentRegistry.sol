// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";

/// @title StudentRegistry
/// @notice Hop dong quan ly danh sach sinh vien tren Blockchain
contract StudentRegistry is Ownable {
    // 1. Dinh nghia cac loi tuy bien (Custom Errors)
    error ZeroAddress();
    error EmptyName();
    error StudentAlreadyExists(address wallet);
    error StudentNotFound(address wallet);

    // 2. Cau truc du lieu Student
    // Struct packing:
    // Slot 0: id (32 bytes)
    // Slot 1: name (32 bytes)
    // Slot 2: wallet (20 bytes) + isActive (1 byte) -> tong 21 bytes, ghep chung vao 1 storage slot
    struct Student {
        uint256 id;
        bytes32 name;
        address wallet;
        bool isActive;
    }

    // 3. Bien trang thai (State Variables)
    uint256 private s_nextStudentId;
    mapping(address => Student) public s_students;
    address[] public s_studentWallets;

    // 4. Su kien (Events)
    event StudentRegistered(
        uint256 indexed id,
        address indexed wallet,
        bytes32 name,
        uint256 timestamp
    );

    event StudentStatusUpdated(
        address indexed wallet,
        bool isActive,
        uint256 timestamp
    );

    event StudentNameUpdated(
        address indexed wallet,
        bytes32 oldName,
        bytes32 newName,
        uint256 timestamp
    );

    // 5. Ham khoi tao (Constructor)
    constructor() Ownable(msg.sender) {
        s_nextStudentId = 1;
    }

    // 6. Ham ghi (State-changing functions)

    /// @notice Dang ky sinh vien moi vao he thong
    /// @dev Kiem tra CEI va phat ra su kien sau khi cap nhat trang thai
    function registerStudent(address _wallet, bytes32 _name) external onlyOwner {
        // Checks
        if (_wallet == address(0)) {
            revert ZeroAddress();
        }
        if (_name == bytes32(0)) {
            revert EmptyName();
        }
        if (s_students[_wallet].wallet != address(0)) {
            revert StudentAlreadyExists(_wallet);
        }

        // Effects
        uint256 newId = s_nextStudentId;
        unchecked {
            ++s_nextStudentId;
        }

        s_students[_wallet] = Student({
            id: newId,
            name: _name,
            wallet: _wallet,
            isActive: true
        });

        s_studentWallets.push(_wallet);

        // Interactions (neu co) & Emit Event
        emit StudentRegistered(newId, _wallet, _name, block.timestamp);
    }

    /// @notice Cap nhat trang thai hoat dong cua sinh vien
    function setStudentStatus(address _wallet, bool _isActive) external onlyOwner {
        // Checks
        if (s_students[_wallet].wallet == address(0)) {
            revert StudentNotFound(_wallet);
        }

        // Effects
        s_students[_wallet].isActive = _isActive;

        // Emit Event
        emit StudentStatusUpdated(_wallet, _isActive, block.timestamp);
    }

    /// @notice Cap nhat ten sinh vien
    function updateStudentName(address _wallet, bytes32 _newName) external onlyOwner {
        // Checks
        if (s_students[_wallet].wallet == address(0)) {
            revert StudentNotFound(_wallet);
        }
        if (_newName == bytes32(0)) {
            revert EmptyName();
        }

        // Effects
        bytes32 oldName = s_students[_wallet].name;
        s_students[_wallet].name = _newName;

        // Emit Event
        emit StudentNameUpdated(_wallet, oldName, _newName, block.timestamp);
    }

    // 7. Ham doc (View functions)

    /// @notice Lay tong so luong sinh vien da dang ky
    function getStudentCount() external view returns (uint256) {
        return s_studentWallets.length;
    }

    /// @notice Lay thong tin chi tiet cua mot sinh vien theo dia chi vi
    function getStudent(address _wallet) external view returns (Student memory) {
        return s_students[_wallet];
    }

    /// @notice Lay toan bo danh sach dia chi vi cua sinh vien
    function getAllStudentWallets() external view returns (address[] memory) {
        return s_studentWallets;
    }
}
