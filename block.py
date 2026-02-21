import hashlib
import time


class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = ""
        self.merkle_root = self.calculate_merkle_root()

    def calculate_hash(self):
        block_string = (
            str(self.index) +
            str(self.timestamp) +
            str(self.merkle_root) +
            str(self.previous_hash) +
            str(self.nonce)
        )

        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        target = "0" * difficulty
        while True:
            self.hash = self.calculate_hash()
            if self.hash[:difficulty] == target:
                break
            self.nonce += 1

        print(f"Block {self.index} mined: {self.hash}")

    def calculate_merkle_root(self):
        tx_hashes = [tx.calculate_hash() for tx in self.transactions]

        if not tx_hashes:
            return None

        while len(tx_hashes) > 1:
            if len(tx_hashes) % 2 != 0:
                tx_hashes.append(tx_hashes[-1])

            new_level = []

            for i in range(0, len(tx_hashes), 2):
                combined = tx_hashes[i] + tx_hashes[i + 1]
                new_hash = hashlib.sha256(combined.encode()).hexdigest()
                new_level.append(new_hash)

            tx_hashes = new_level

        return tx_hashes[0]




"""


blockchain = [
    {
        "index": 0,
        "prev_hash": "000000...",
        "transactions": [tx1, tx2, tx3], # This is the "list" within the block
        "merkle_root": "a1b2c3...",
        "hash": "block_hash_0"
    },
    {
        "index": 1,
        "prev_hash": "block_hash_0", # Link to the previous block
        "transactions": [tx4, tx5, tx6],
        "merkle_root": "d4e5f6...",
        "hash": "block_hash_1"
    }
]


"""