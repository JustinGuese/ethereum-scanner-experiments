# from web3.auto import w3
from web3 import Web3, eth
from pprint import pprint
import json

w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/7fe18b1164b0476dbb9a0b1d8af0d8ea"))
# w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
# https://ethereumnodes.com/
# w3 = Web3(Web3.HTTPProvider("https://nodes.mewapi.io/rpc/eth"))

connected = w3.isConnected()
print("connected?", connected)

pending_transactions_filter= w3.eth.filter('latest')
pending_transactions= pending_transactions_filter.get_all_entries()
pending_transactions = [dict(d) for d in pending_transactions]
transactions = [dict(w3.eth.get_transaction(txnHash["transactionHash"])) for txnHash in pending_transactions]
# convert hexbytes to str
for txn in transactions:
    for key,val in txn.items():
        if str(type(val)) == "<class 'hexbytes.main.HexBytes'>":
            txn[key] = val.decode('utf-8')
            print("fixed: ", txn[key])
# pprint(transactions)
with open("latest_transactions.json", "w") as file:
    json.dump(transactions, file, indent = 4,default = str)