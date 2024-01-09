from web3 import Web3
from scripts.helpful_scripts import get_account
from brownie import web3,interface, convert, Contract, Simple
from eth_utils import keccak

DEPTH = 5
GAS_LIMIT = 6000000


def main():

    player = get_account()
    simple = Simple.deploy({"from": player})#, publish_source=True)
    simple_address = simple.address
    
    print(f"\Simple contract deployment address = {simple_address}")  

