from web3 import Web3
from scripts.helpful_scripts import get_account
from brownie import web3, network, interface, convert, LockDrop, Contract, RewardToken
from eth_utils import keccak

LOCKDROP = "0x63eBB10d1625ED42a72f5D7DD3F3F1459bec0116"  # LockDrop deployed address
# LOCKDROP = "0x865e4C42f2Ca3b1ae1bd074e3B385732a32859bc"  # sepolia deployment
RWDTOKEN = "0xE01788f3b8135e3C4BdcdD08F480A7aC5FDD1854"  # RewardToken deployed address 
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

def check_token_balance():
    lockdrop_contract = Contract.from_explorer(LOCKDROP)
    reward_token_contract = Contract.from_explorer(RWDTOKEN)
    rwd_balance = reward_token_contract.balanceOf(LOCKDROP)
    print(f"\nRWD token balance of LockDrop contract: {rwd_balance}")
    

def main():

    player = get_account()
    target = interface.ILockDrop(LOCKDROP)
    
    # call deposit (0.1 ETH)
    # target.deposit({"from": player, "value": Web3.toWei(0.1, "ether")})

    # call withdraw
    # target.withdraw({"from": player})  

    view_storage_slots(DEPTH, LOCKDROP)
    # check_token_balance()



   



    """ handle emitted events from LockDrop """

    ## Load your contract and get the contract instance
    # contract = Contract.from_abi("LockDrop", deployment, LockDrop.abi)

    ## Listen for the event
    # def handle_event(event):
        # print(f"Sender: {event['args']['_sender']}, Value: {event['args']['_value']}")

    # contract.MyEvent.createFilter().listen(handle_event)

    """  ---------------------------------  """

