// SPDX-License-Identifier: MIT
pragma solidity 0.8.22;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

/* 
    Reward (RWD) token contract
*/

contract RewardToken is ERC20 {
    address public owner;

    constructor(address _address, uint256 _supply) ERC20("Reward", "RWD") {
        owner = msg.sender;
        _mint(_address, _supply);       
    }
}

