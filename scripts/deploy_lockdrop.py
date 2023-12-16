from web3 import Web3
from scripts.helpful_scripts import get_account
from brownie import web3, network, interface, convert, LockDrop
from eth_utils import keccak

MY_ACC = "0xF8f8269488f73fab3935555FCDdD6035699deE25"
DEPTH = 5

GAS_LIMIT = 6000000
TARGET = "0x40F2849C477ECE4BeeF6F8217dbD991e8Cf34998"


def view_storage_slots(_depth):
    print(f"\n")
    for i in range(_depth):
        store_value = web3.eth.get_storage_at(TARGET, i)
        store_value_hex = web3.toHex(store_value)
        print(f"storage slot {i}: {store_value_hex}")
    print(f"\n")


def main():

    player = get_account()
    target = interface.ILockDrop(TARGET)

    # deployment = LockDrop.deploy({"from": player})
    # print(f"\ndeployed at: {deployment}\n")

    # deployment.deposit({"from": player, "value": Web3.toWei(0.1, "ether")})
    # deployment.withdraw({"from": player})
    
    # target.withdraw({"from": player})
    
    view_storage_slots(DEPTH)



