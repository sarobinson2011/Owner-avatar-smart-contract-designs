from web3 import Web3
from scripts.helpful_scripts import get_account
from brownie import web3, network, interface, convert, LockDrop
from eth_utils import keccak

MY_ACC = "0xF8f8269488f73fab3935555FCDdD6035699deE25"
DEPTH = 5

GAS_LIMIT = 6000000

def view_storage_slots(_depth, _target):
    for i in range(_depth):
        store_value = web3.eth.get_storage_at(_target, i)
        store_value_hex = web3.toHex(store_value)
        print(f"storage slot {i}: {store_value_hex}")
    print(f"\n")


def main():

    player = get_account()
    deployment = LockDrop.deploy({"from": player})
    # target = interface.ILockDrop(deployment)
    
    deployment.deposit({"from": player, "value": Web3.toWei(0.1, "ether")})
    # target.withdraw({"from": player})    
    view_storage_slots(DEPTH, deployment.address) 

    """ 

    2. From brownie import Contract, project

    # Load your contract and get the contract instance
        contract_address = "0x123..."  # Replace with your contract's address
        contract = Contract.from_abi("MyContract", contract_address, MyContract.abi)

    # Listen for the event
        def handle_event(event):
            print(f"Sender: {event['args']['_sender']}, Value: {event['args']['_value']}")

        contract.MyEvent.createFilter().listen(handle_event)














    """




  