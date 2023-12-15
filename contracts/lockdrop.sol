// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*
Title:  LockDrop 
1. time-lock deposit/with contract
2. with an auto airdrop (on withdraw) for every unit time locked
*/

contract LockDrop {
    address public owner;

    struct timedDeposit {
        uint256 amount;
        uint256 timestamp;
        uint256 reward;
    }

    mapping (address => timedDeposit) public balance;   // individual account balance

    constructor() {
        owner = msg.sender;
    }

    function deposit() external payable {
        balance[msg.sender] = timedDeposit(
            {
                amount: msg.value, 
                timestamp: block.timestamp,
                reward: 0  // zero for now
            }
        );
    } 
    
    function withdraw() external {
        require(balance[msg.sender].amount > 0, "No way in here...");
        require(block.timestamp >= balance[msg.sender].timestamp + 10 days, "Time lock not expired");
        uint256 amount = balance[msg.sender].amount;
        balance[msg.sender].amount = 0;
        balance[msg.sender].timestamp = 0;
        payable(msg.sender).transfer(amount);
    }
}

