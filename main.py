from blockchain import Blockchain
from block import Block
from transaction import Transactionday

my_blockchain = Blockchain()

# Add some blocks
my_blockchain.add_block(Block(1, "Alice pays Bob 5 BTC", ""))
my_blockchain.add_block(Block(2, "Bob pays Charlie 2 BTC", ""))
block_3 = Block(3, "Otis pays Nuel 10btc", "")
my_blockchain.add_block(block_3)

# my_blockchain.chain[1].transactions = "Alice pays Bob 500 BTC"
# print("Is blockchain valid?", my_blockchain.is_chain_valid())
# my_blockchain.chain[1].hash = my_blockchain.chain[1].calculate_hash()


for block in my_blockchain.chain:
    print("Index:", block.index)
    print("Transactions:", block.transactions)
    print("Hash:", block.hash)
    print("Previous Hash:", block.previous_hash)
    print("Nonce:", block.nonce)
    print("-" * 50)


# block_4 = Block(4, "Ez pays Uvie 31 BTC", "")
# my_blockchain.add_block(block_4)














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



# latest_block = my_blockchain.get_latest_block()
# print(latest_block.transactions)

#block_4 = Block(4, "Peter sent 2.5btc to Paul")





"""
"""