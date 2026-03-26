from blockchain import Blockchain
from transaction import Transaction

my_blockchain = Blockchain()


def create_transaction(sender, recipient, amount, private_key):
    tx = Transaction(sender, recipient, amount)
    tx.sign_transaction(private_key)
    return tx


# create transactions
tx1 = create_transaction("otis", "chatgpt", 2, "otis_private_key")
tx2 = create_transaction("chatgpt", "chat_not_gpt", 0.5, "chatgpt_private_key")
tx3 = create_transaction("chat_not_gpt", "Otis", 1, "chat_not_gpt_private_key")

my_blockchain.add_transaction(tx1)
my_blockchain.add_transaction(tx2)
my_blockchain.add_transaction(tx3)

print(my_blockchain.pending_transactions)

my_blockchain.mine_pending_transactions("bcq1234567891")

block1 = my_blockchain.chain[1]
print(block1.transactions[1].txid)





















# my_blockchain.chain[1].transactions = "Alice pays Bob 500 BTC"
# print("Is blockchain valid?", my_blockchain.is_chain_valid())
# my_blockchain.chain[1].hash = my_blockchain.chain[1].calculate_hash()


# for block in my_blockchain.chain:
#     print("Index:", block.index)
#     print("Transactions:", block.transactions)
#     print("Hash:", block.hash)
#     print("Previous Hash:", block.previous_hash)
#     print("Nonce:", block.nonce)
#     print("-" * 50)














"""
# Print the chain
for block in my_blockchain.chain:
    print("Index:", block.index)
    print("Transactions:", block.transactions)
    print("Hash:", block.hash)
    print("Previous Hash:", block.previous_hash)
    print("-" * 50)


my_blockchain.chain[1].transactions = "Alice pays Bob 500 BTC"

my_blockchain.chain[1].hash = my_blockchain.chain[1].calculate_hash()

print("Is blockchain valid?", my_blockchain.is_chain_valid())

"""






"""
"""