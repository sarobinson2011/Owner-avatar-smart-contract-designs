// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

/* 
    Reward (RWD) token contract
*/

contract RewardToken is ERC20 {
    address public owner;

    constructor() ERC20("Reward", "RWD") {
        owner = msg.sender;
        _mint(address(this), 100000);       
    }
}

