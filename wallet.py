import hashlib
import ecdsa


class Wallet:

    def __init__(self):

        # private key
        self.private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)

        # public key
        self.public_key = self.private_key.get_verifying_key()

        # bitcoin-style address
        self.address = self.generate_address()

    def generate_address(self):

        pubkey_bytes = self.public_key.to_string()
        print(f"This is string of public key: {pubkey_bytes}")

        sha = hashlib.sha256(pubkey_bytes).digest()

        ripemd = hashlib.new("ripemd160")
        ripemd.update(sha)

        return ripemd.hexdigest()

my_wallet = Wallet()

print(f"Private Key: {my_wallet.private_key}")

print(f"Public Key: {my_wallet.public_key}")

print(f"Address: {my_wallet.address}")


