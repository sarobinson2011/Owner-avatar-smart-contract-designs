from web3 import Web3
from scripts.helpful_scripts import get_account
from brownie import web3,interface, convert, Contract, LockDrop, RewardToken 
from eth_utils import keccak

MY_ACC = "0xF8f8269488f73fab3935555FCDdD6035699deE25"
SUPPLY = 1_000_000 * (10 ** 18)                          # supply = 1 million

DEPTH = 5
GAS_LIMIT = 6000000

def view_storage_slots(_depth, _target):
    print(f"\n")
    for i in range(_depth):
        store_value = web3.eth.get_storage_at(_target, i)
        store_value_hex = web3.toHex(store_value)
        print(f"storage slot {i}: {store_value_hex}")
    print(f"\n")


def main():

    player = get_account()
    lockdrop = LockDrop.deploy({"from": player})#, publish_source=True)
    lockdrop_address = lockdrop.address

    rwd_token = RewardToken.deploy(lockdrop_address, SUPPLY, {"from": player})#, publish_source=True)  
    rwd_token_address = rwd_token.address
    
    print(f"\nLockDrop deployment address = {lockdrop_address}")  
    print(f"\nReward Token deployment address = {rwd_token_address}")
    
    view_storage_slots(DEPTH, lockdrop_address) 



