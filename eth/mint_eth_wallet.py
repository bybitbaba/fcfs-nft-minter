# ethmint_eth_wallet.py - ETH FCFS Minter (MetaMask Connect)
from web3 import Web3
import json
import time
from dotenv import load_dotenv
import os

load_dotenv()

# CONFIG (Testnet first)
RPC_URL = httpseth-goerli.g.alchemy.comv2demo  # Change to mainnet later
CONTRACT_ADDRESS = input(Enter Contract Address )  # e.g., 0x...
MINT_FUNCTION = input(Enter Mint Function Name (e.g., mint) )
AMOUNT = 1
GAS_LIMIT = 300000
MAX_RETRIES = 50

w3 = Web3(Web3.HTTPProvider(RPC_URL))

# Load ABI from file or input
ABI = json.loads(input(Paste ABI JSON ))  # Or load from config.json

contract = w3.eth.contract(address=Web3.to_checksum_address(CONTRACT_ADDRESS), abi=ABI)

def get_wallet_address()
    print(Open MetaMask  Copy Address  Paste here)
    return input(Your MetaMask Address )

def build_and_sign_tx()
    user_address = get_wallet_address()
    nonce = w3.eth.get_transaction_count(user_address)
    func = contract.functions[MINT_FUNCTION](AMOUNT)
    tx = func.build_transaction({
        'chainId' 5,  # Goerli (1 for Mainnet)
        'gas' GAS_LIMIT,
        'maxFeePerGas' w3.to_wei('20', 'gwei'),
        'maxPriorityFeePerGas' w3.to_wei('1', 'gwei'),
        'nonce' nonce,
        'value' w3.to_wei(0.01, 'ether')  # Mint price
    })

    # Output for MetaMask Sign this TX
    print(n=== META MASK TX TO SIGN ===)
    print(json.dumps(tx, indent=2))
    print(1. MetaMask  Advanced  Sign TX)
    print(2. Or use Etherscan Write Contract httpsgoerli.etherscan.ioaddress + CONTRACT_ADDRESS + #writeContract)
    print(================================)

def fcfs_monitor()
    print(FCFS Mode Monitoring for live mint...)
    start_time = input(Enter Sale Start Time (YYYY-MM-DD HHMM) )
    import datetime
    target = datetime.datetime.strptime(start_time, %Y-%m-%d %H%M)
    while datetime.datetime.now()  target
        time.sleep(1)
        print(Waiting..., datetime.datetime.now().strftime(%H%M%S))
    print(LIVE! Building TX...)
    for _ in range(MAX_RETRIES)
        build_and_sign_tx()
        time.sleep(0.5)  # Fast retry

if __name__ == __main__
    fcfs_monitor()