// SPDX-License-Identifier: MIT
pragma solidity 0.8.22;

import "./tokencontract.sol";

contract LockDrop {
    address public owner;

    struct TimedDeposit {
        uint256 amount;
        uint256 timestamp;
        uint256 reward;
    }

    mapping (address => TimedDeposit) public balances;   
    event NewDeposit(address indexed _user, uint256 _amount);
    event NewWithdraw(address indexed _user, uint256 _amount);

    constructor() {
        owner = msg.sender;
    }

    function deposit() external payable {
        balances[msg.sender] = TimedDeposit(
            {
                amount: msg.value, 
                timestamp: block.timestamp,
                reward: 0  // zero for now
            }
        );
        emit NewDeposit(msg.sender, msg.value);
    } 
    
    function withdraw() external {
        require(balances[msg.sender].amount > 0, "You have no balance to withdraw...");
        require(block.timestamp >= balances[msg.sender].timestamp + 5 minutes, "Time lock not expired...");
        uint256 tempAmount = balances[msg.sender].amount;
        balances[msg.sender].amount = 0;
        balances[msg.sender].timestamp = 0;
        balances[msg.sender].reward = 0;
        payable(msg.sender).transfer(tempAmount);
        tempAmount = 0;
        emit NewWithdraw(msg.sender, tempAmount);
    }
} 

