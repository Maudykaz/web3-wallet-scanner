import json
import requests
from web3 import Web3
from tabulate import tabulate

RPC = "https://rpc.ankr.com/eth"
w3 = Web3(Web3.HTTPProvider(RPC))

def load_wallets(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f if line.strip().startswith("0x")]

def get_eth_balance(address):
    balance_wei = w3.eth.get_balance(address)
    return w3.fromWei(balance_wei, 'ether')

def get_ens_name(address):
    try:
        return w3.ens.name(address) or "-"
    except:
        return "-"

def main():
    wallets = load_wallets("wallets.txt")
    results = []

    for addr in wallets:
        balance = get_eth_balance(addr)
        ens = get_ens_name(addr)
        results.append([addr, f"{balance:.4f} ETH", ens])

    print(tabulate(results, headers=["Address", "Balance", "ENS Name"]))

if __name__ == "__main__":
    main()
