// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract LockDrop {
    address public owner;

    struct timedDeposit {
        uint256 amount;
        uint256 timestamp;
        uint256 reward;
    }

    mapping (address => timedDeposit) public balances;   
    event newDeposit(address indexed _user, uint256 _amount);

    constructor() {
        owner = msg.sender;
    }    

    function deposit() external payable {
        balances[msg.sender] = timedDeposit(
            {
                amount: msg.value, 
                timestamp: block.timestamp,
                reward: 0  // zero for now
            }
        );
        emit newDeposit(msg.sender, msg.value);
    } 
    
    function withdraw() external {
        require(balances[msg.sender].amount > 0, "You have no balance to withdraw...");
        require(block.timestamp >= balances[msg.sender].timestamp + 5 minutes, "Time lock not expired");
        uint256 amount = balances[msg.sender].amount;
        balances[msg.sender].amount = 0;
        balances[msg.sender].timestamp = 0;
        payable(msg.sender).transfer(amount);
    }
}

