import hashlib
import json

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = None
        self.txid = self.calculate_hash()

    def to_dict(self):
        return {
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount
        }

    def calculate_hash(self):
        tx_string = json.dumps(self.to_dict(), sort_keys=True)
        return hashlib.sha256(tx_string.encode()).hexdigest()

    def sign_transaction(self, private_key):
        tx_data = (self.calculate_hash() + private_key)
        self.signature = hashlib.sha256(tx_data.encode()).hexdigest()

    def is_valid(self):
        if self.sender == "SYSTEM":
            return True

        if not self.signature:
            print("No signature!")
            return False

        return True


# transaction = Transaction("u", "v", 12)
# print(transaction.sender)