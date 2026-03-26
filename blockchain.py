from block import Block
from transaction import Transaction


class Blockchain:
    def __init__(self):
        self.difficulty = 4
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []

    def create_genesis_block(self):
        genesis_block = Block(0, [], "0")
        genesis_block.mine_block(self.difficulty)
        return genesis_block

    def get_latest_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction):
        if not transaction.is_valid():
            print("Transaction rejected")
            return False
        self.pending_transactions.append(transaction)
        return True

    def mine_pending_transactions(self, miner_address):
        if not self.pending_transactions:
            print("No transactions to mine")
            return False

        # Coinbase transaction (mining reward)
        reward_tx = Transaction("SYSTEM", miner_address, 6.25)

        block_transactions = [reward_tx] + self.pending_transactions

        new_block = Block(
            len(self.chain),
            block_transactions,
            self.get_latest_block().hash
        )

        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.pending_transactions.clear()
        return new_block



    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # 1️⃣ Recalculate the hash and compare with stored hash
            if current_block.hash != current_block.calculate_hash():
                print(f"Block {i} has been tampered with!")
                return False

            # 2️⃣ Check if the previous_hash matches previous block's hash
            if current_block.previous_hash != previous_block.hash:
                print(f"Block {i} is not properly linked!")
                return False

                # 3️⃣ verify proof of work
            if not current_block.hash.startswith("0" * self.difficulty):
                print(f"Block {i} was not properly mined!")
                return False

            #verify merkle root
            if current_block.merkle_root != current_block.calculate_merkle_root():
                print(f"Block {i} has invalid merkle root!")
                return False

            for tx in current_block.transactions:
                if not tx.is_valid():
                    print("Invalid transaction detected!")
                    return False

        return True



