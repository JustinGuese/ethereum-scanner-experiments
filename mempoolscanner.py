# from web3.auto import w3
from web3 import Web3
# w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/7fe18b1164b0476dbb9a0b1d8af0d8ea"))
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
# https://ethereumnodes.com/
# w3 = Web3(Web3.HTTPProvider("https://nodes.mewapi.io/rpc/eth"))

connected = w3.isConnected()
print("connected?", connected)

pending_transactions_filter= w3.eth.filter('pending')
pending_transactions= pending_transactions_filter.get_new_entries()
print("pending_transactions", pending_transactions)