from web3 import Web3

#Defining the sender and receiver addresses
sender_address = '0xcef6153C2B046Fcc6b5356a87017254793FCd16e'
receiver_address = '0x8575E996330a60820FDC5f5aA343EE7668803faa'

#Connecting to the Ethereum network (Local Ganache Network)
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

#Set the sender's private key
private_key = '7f2053122c5f0edf10dee62ed4f5c9ad4f221f5541f721b1e48ea3ae341842e5'

#Create the transaction object
transaction = {
    'to': receiver_address,
    'value': w3.toWei(20, 'ether'),
    'gas': 2000000,
    'gasPrice': w3.toWei('50', 'gwei'),
    'nonce': w3.eth.getTransactionCount(sender_address)
}

#Sign the transaction
signed_transaction = w3.eth.account.signTransaction(transaction, private_key)

#Send the transaction
tx_hash = w3.eth.sendRawTransaction(signed_transaction.rawTransaction)

#Get the transaction receipt
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

# print the transaction receipt
print(tx_receipt)
