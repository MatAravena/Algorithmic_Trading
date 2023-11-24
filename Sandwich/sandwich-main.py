import time
import json
import requests
from web3 import Web3
from web3.middleware import geth_poa_middleware
from web3.exceptions import InvalidAddress
from eth_account import Account

# ABI provider
# const { abi: QuoterABI } = require('@uniswap/v3-periphery/artifacts/contracts/lens/QuoterV2.sol/QuoterV2.json');

# Ethereum node provider URL
provider_url = 'https://mainnet.infura.io/v3/dd903360661a41d2955caf3b929f775a'

# Uniswap contract addresses
router_address = '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D'
token_1_address = '0xTOKEN_1_ADDRESS' # Example token 1 address
token_2_address = '0xdAC17F958D2ee523a2206206994597C13D831ec7' # USDT

# MetaMask wallet private key and passphrase
wallet_private_key = 'YOUR_WALLET_PRIVATE_KEY'
# wallet_passphrase = 'YOUR_WALLET_PASSPHRASE'

# Initialize Web3 provider
web3 = Web3(Web3.HTTPProvider(provider_url))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Load the wallet
wallet = Account.from_key(wallet_private_key)

# Set the contract addresses
router_contract = web3.eth.contract(address=Web3.toChecksumAddress(router_address), abi=json.loads(UNISWAP_ROUTER_ABI))

# Specify the token and trade amounts
token_1_amount = web3.toWei(1, 'ether') # Amount of token 1 to trade
token_2_amount = web3.toWei(1, 'ether') # Amount of token 2 to trade
trade_slippage = 0.05                   # Slippage tolerance (5%)

# Function to execute the trade
def execute_sandwich_trade():

    # Get the latest token prices from Uniswap
    token_1_price = get_token_price(token_1_address)
    token_2_price = get_token_price(token_2_address)

    # Calculate the target prices
    buy_price = token_1_price - (token_2_price * (1 + trade_slippage))
    sell_price = token_1_price + (token_2_price * (1 - trade_slippage))

    # Simulate checking the market prices
    # Replace this with your own logic to fetch real-time market prices
    token_1_market_price = get_token_price(token_1_address)
    token_2_market_price = get_token_price(token_2_address)

    # Execute buy trade
    if token_1_market_price <= buy_price:
        print("Executing buy trade…")
        execute_uniswap_trade(token_2_address, token_2_amount, token_1_address, token_1_amount)
    # Execute sell trade
    elif token_1_market_price >= sell_price:
        print("Executing sell trade…")
        execute_uniswap_trade(token_1_address, token_1_amount, token_2_address, token_2_amount)

# Function to get the token price from Uniswap
def get_token_price(token_address):
    try:
        response = requests.get(f'https://api.coingecko.com/api/v3/simple/token_price/ethereum?contract_addresses={token_address}&vs_currencies=usd')
        data = response.json()
        token_price = data[token_address.lower()]['usd']
        return token_price
    except Exception as e:
        print(f"Error fetching token price: {e}")
        return None

# Function to execute the trade on Uniswap
def execute_uniswap_trade(from_token, from_amount, to_token, to_amount):

    try:
        # Approve the token transfer
        approve_tx = router_contract.functions.approve(
                Web3.toChecksumAddress(router_address), from_amount).buildTransaction({'from': wallet.address,
                'gas': 100000,
                'gasPrice': web3.toWei('5', 'gwei'),
                'nonce': web3.eth.getTransactionCount(wallet.address),
            })

        signed_approve_tx = web3.eth.account.sign_transaction(approve_tx, private_key=wallet.privateKey)
        approve_tx_hash = web3.eth.send_raw_transaction(signed_approve_tx.rawTransaction)
        web3.eth.wait_for_transaction_receipt(approve_tx_hash)

        # Execute the swap
        swap_tx = router_contract.functions.swapExactTokensForTokens(
        from_amount,
        to_amount,
        [from_token, to_token],
        wallet.address,
        int(time.time()) + 10000
        ).buildTransaction({
        'from': wallet.address,
        'gas': 200000,
        'gasPrice': web3.toWei('5', 'gwei'),
        'nonce': web3.eth.getTransactionCount(wallet.address)})
        signed_swap_tx = web3.eth.account.sign_transaction(swap_tx, private_key=wallet.privateKey)
        swap_tx_hash = web3.eth.send_raw_transaction(signed_swap_tx.rawTransaction)
        web3.eth.wait_for_transaction_receipt(swap_tx_hash)

        print("Trade executed successfully.")

    except InvalidAddress as e:
        print(f"Invalid contract address: {e}")
    except Exception as e:
        print(f"Error executing trade: {e}")

# Main loop
while True:
 execute_sandwich_trade()
 time.sleep(10) # Wait for 10 seconds before executing the next trade