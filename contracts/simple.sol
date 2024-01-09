// SPDX-License-Identifier: MIT
pragma solidity 0.8.22;

/* 
    Simple contract to test contract verification
*/

contract Simple {
    address public owner;

    constructor()  {
        owner = msg.sender;
    }

    receive() external payable {}
}

