from web3 import Web3
from scripts.helpful_scripts import get_account
from brownie import web3, network, interface, convert, LockDrop
from eth_utils import keccak

GAS_LIMIT = 6000000
TARGET = "0x40F2849C477ECE4BeeF6F8217dbD991e8Cf34998"


def main():

    player = get_account()
    target = interface.ILockDrop(TARGET)

    # deployment = LockDrop.deploy({"from": player})
    # print(f"\ndeployed at: {deployment}\n")

    # deployment.deposit({"from": player, "value": Web3.toWei(0.1, "ether")})
    # deployment.withdraw({"from": player})
    
    target.withdraw({"from": player})
    
