from web3 import Web3
from scripts.helpful_scripts import get_account
from brownie import web3, network, interface, convert, LockDrop
from eth_utils import keccak

MY_ACC = "0xF8f8269488f73fab3935555FCDdD6035699deE25"
DEPTH = 5

GAS_LIMIT = 6000000

def view_storage_slots(_depth, _target):
    # print(f"\n")
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
    # deployment.withdraw({"from": player})
        
    view_storage_slots(DEPTH, deployment.address) 

    """ 

    Using the Development Testnet (ganache)

    In order to test the deposit withdraw functionality, we can utilise Ganache test chain
    such that we have multiple test accounts ready to use, plus we don't need test-ETH

    1.  set to ganache
    2.  using account[0]
    3.  --> here we use Ganache-CLI *or* Ganche-GUI

    """



