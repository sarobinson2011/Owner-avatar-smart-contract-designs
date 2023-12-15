from scripts.helpful_scripts import get_account
from brownie import web3, network, interface, convert, LockDrop
from eth_utils import keccak

GAS_LIMIT = 6000000


def main():

    player = get_account()
    deployment = LockDrop.deploy({"from": player})
    print(f"\ndeployed at: {deployment}\n")


