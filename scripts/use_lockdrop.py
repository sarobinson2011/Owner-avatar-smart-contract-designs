from web3 import Web3
from scripts.helpful_scripts import get_account
from brownie import web3, network, interface, convert, LockDrop, Contract, RewardToken
from eth_utils import keccak

LOCKDROP = "0x59B9324f05a5d82F3Bf80969c11Dcd552082B96E"  # LockDrop deployed address
RWDTOKEN = "0x69c6867Aad379ceb6A8EBEF3f07275f97130Aa8E"  # RewardToken deployted address 
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

def check_token_balance(_address):
    contract_address = _address
    print(contract_address)


def main():

    player = get_account()
    target = interface.ILockDrop(LOCKDROP)
    
    # call deposit (0.1 ETH)
    # target.deposit({"from": player, "value": Web3.toWei(0.1, "ether")})

    # call withdraw
    # target.withdraw({"from": player})  

    view_storage_slots(DEPTH, LOCKDROP)

    check_token_balance(RWDTOKEN)

   



    """ handle emitted events from LockDrop """

    ## Load your contract and get the contract instance
    # contract = Contract.from_abi("LockDrop", deployment, LockDrop.abi)

    ## Listen for the event
    # def handle_event(event):
        # print(f"Sender: {event['args']['_sender']}, Value: {event['args']['_value']}")

    # contract.MyEvent.createFilter().listen(handle_event)

    """  ---------------------------------  """

