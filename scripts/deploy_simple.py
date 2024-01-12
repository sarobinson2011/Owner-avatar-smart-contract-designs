from web3 import Web3
from scripts.helpful_scripts import get_account
from brownie import web3,interface, convert, Contract, SimpleToken
from eth_utils import keccak

GAS_LIMIT = 6000000


def main():

    player = get_account()
    simple = SimpleToken.deploy({"from": player})#, publish_source=True)
    simple_address = simple.address
    print(f"\nLockDrop deployment address = {simple_address}")
    
      
    
