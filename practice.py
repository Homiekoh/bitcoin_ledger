import json
from bitcoin.rpc import RawProxy
from decimal import Decimal

p = RawProxy()

#check block info
blockchain_info = p.getblockchaininfo()
print(f"Total number of blocks: {blockchain_info["blocks"]}")

#check prune height
current_prune_height = blockchain_info['pruneheight']
print(f"Prune height: {current_prune_height}")


block_height = 938020
block_hash = p.getblockhash(block_height)
print(f"Block Hash: {block_hash}")
block = p.getblock(block_hash, 2)
transactions = block["tx"]

tx_1 = transactions[1]
tx_value = 0

for transaction in transactions:
    outputs = transaction["vout"]
    for output in outputs:
        tx_value += output["value"]




#print(transactions[1]["vout"])

print(f"Total Value in block: {tx_value}")


def decimal_default(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

data = json.dumps(tx_1, indent=4, default=decimal_default)

with open("btc_transaction.txt", "w") as file:
    file.write(data)





"""
#Using json and Decimal in decimal module to make the file look more readable


def decimal_default(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

tx_1 = {'txid': 'b6505e9e29b3b35aff88d975523e09813f05b0ffb39da80302c51991122b05d1', 'hash': '31214270c67cd3ef147b02144c96528f7e62c665dab5c39151703f1b15f9f9a8', 'version': 1, 'size': 478, 'vsize': 451, 'weight': 1804, 'locktime': 0, 'vin': [{'coinbase': '0324500e20202020204d696e656420627920536563706f6f6c202020209b006307ba7322b2fabe6d6d1a9e3f4dd46e31fc66c8f7d3c731ee3ac35ea523fd3ed2a1bd171d737c731c7310000000000000000000bd790617b00000000000', 'txinwitness': ['0000000000000000000000000000000000000000000000000000000000000000'], 'sequence': 4294967295}], 'vout': [{'value': Decimal('0.00000546'), 'n': 0, 'scriptPubKey': {'asm': 'OP_HASH160 8ee90177614ecde53314fd67c46162f315852a07 OP_EQUAL', 'desc': 'addr(3Eif1JfqeMERRsQHtvGEacNN9hhuvnsfe9)#lvfz5kkj', 'hex': 'a9148ee90177614ecde53314fd67c46162f315852a0787', 'address': '3Eif1JfqeMERRsQHtvGEacNN9hhuvnsfe9', 'type': 'scripthash'}}, {'value': Decimal('3.13048806'), 'n': 1, 'scriptPubKey': {'asm': 'OP_HASH160 6582f2551e2a47e1ae8b03fb666401ed7c4552ef OP_EQUAL', 'desc': 'addr(3Awm3FNpmwrbvAFVThRUFqgpbVuqWisni9)#j8r6vh28', 'hex': 'a9146582f2551e2a47e1ae8b03fb666401ed7c4552ef87', 'address': '3Awm3FNpmwrbvAFVThRUFqgpbVuqWisni9', 'type': 'scripthash'}}, {'value': Decimal('0E-8'), 'n': 2, 'scriptPubKey': {'asm': 'OP_RETURN aa21a9eddf8160967de885aa1774015f8ee0523a9aab8eee8b6f52c9c87385f5af3a8ec3', 'desc': 'raw(6a24aa21a9eddf8160967de885aa1774015f8ee0523a9aab8eee8b6f52c9c87385f5af3a8ec3)#5fh5pauj', 'hex': '6a24aa21a9eddf8160967de885aa1774015f8ee0523a9aab8eee8b6f52c9c87385f5af3a8ec3', 'type': 'nulldata'}}, {'value': Decimal('0E-8'), 'n': 3, 'scriptPubKey': {'asm': 'OP_RETURN 434f524501a21cbd3caa4fe89bccd1d716c92ce4533e4d4733942c01262fa046fdb8ba0dfce3753405c74aed0e', 'desc': 'raw(6a2d434f524501a21cbd3caa4fe89bccd1d716c92ce4533e4d4733942c01262fa046fdb8ba0dfce3753405c74aed0e)#29u7wlam', 'hex': '6a2d434f524501a21cbd3caa4fe89bccd1d716c92ce4533e4d4733942c01262fa046fdb8ba0dfce3753405c74aed0e', 'type': 'nulldata'}}, {'value': Decimal('0E-8'), 'n': 4, 'scriptPubKey': {'asm': 'OP_RETURN 455853415401000d130f0e0e0b041f120013', 'desc': 'raw(6a12455853415401000d130f0e0e0b041f120013)#39a8xnqr', 'hex': '6a12455853415401000d130f0e0e0b041f120013', 'type': 'nulldata'}}, {'value': Decimal('0E-8'), 'n': 5, 'scriptPubKey': {'asm': 'OP_RETURN 73797357c8ea6193f31c8b29e5e62e7a7510eee7d6013d4735db4fb1d228261f2c43e8bc772100', 'desc': 'raw(6a2773797357c8ea6193f31c8b29e5e62e7a7510eee7d6013d4735db4fb1d228261f2c43e8bc772100)#g262p8vn', 'hex': '6a2773797357c8ea6193f31c8b29e5e62e7a7510eee7d6013d4735db4fb1d228261f2c43e8bc772100', 'type': 'nulldata'}}, {'value': Decimal('0E-8'), 'n': 6, 'scriptPubKey': {'asm': 'OP_RETURN 52534b424c4f434b3ac79a4a8e16d76fa91e2572427696ea863d96f268ccd4a0baea9d741500829c7c', 'desc': 'raw(6a2952534b424c4f434b3ac79a4a8e16d76fa91e2572427696ea863d96f268ccd4a0baea9d741500829c7c)#ktunumfz', 'hex': '6a2952534b424c4f434b3ac79a4a8e16d76fa91e2572427696ea863d96f268ccd4a0baea9d741500829c7c', 'type': 'nulldata'}}], 'hex': '010000000001010000000000000000000000000000000000000000000000000000000000000000ffffffff5d0324500e20202020204d696e656420627920536563706f6f6c202020209b006307ba7322b2fabe6d6d1a9e3f4dd46e31fc66c8f7d3c731ee3ac35ea523fd3ed2a1bd171d737c731c7310000000000000000000bd790617b00000000000ffffffff07220200000000000017a9148ee90177614ecde53314fd67c46162f315852a0787e6bea8120000000017a9146582f2551e2a47e1ae8b03fb666401ed7c4552ef870000000000000000266a24aa21a9eddf8160967de885aa1774015f8ee0523a9aab8eee8b6f52c9c87385f5af3a8ec300000000000000002f6a2d434f524501a21cbd3caa4fe89bccd1d716c92ce4533e4d4733942c01262fa046fdb8ba0dfce3753405c74aed0e0000000000000000146a12455853415401000d130f0e0e0b041f1200130000000000000000296a2773797357c8ea6193f31c8b29e5e62e7a7510eee7d6013d4735db4fb1d228261f2c43e8bc77210000000000000000002b6a2952534b424c4f434b3ac79a4a8e16d76fa91e2572427696ea863d96f268ccd4a0baea9d741500829c7c0120000000000000000000000000000000000000000000000000000000000000000000000000'}

formatted_json = json.dumps(tx_1, indent=4, default=decimal_default)
print(formatted_json)

"""



"""
verbosity 2, already decode's the tx raw hash
"""




"""
#coinbase block

938037
937673
Block Hash: 00000000000000000000d8d015bb517e40383d856d519f7811637387976307db
{
    "txid": "b6505e9e29b3b35aff88d975523e09813f05b0ffb39da80302c51991122b05d1",
    "hash": "31214270c67cd3ef147b02144c96528f7e62c665dab5c39151703f1b15f9f9a8",
    "version": 1,
    "size": 478,
    "vsize": 451,
    "weight": 1804,
    "locktime": 0,
    "vin": [
        {
            "coinbase": "0324500e20202020204d696e656420627920536563706f6f6c202020209b006307ba7322b2fabe6d6d1a9e3f4dd46e31fc66c8f7d3c731ee3ac35ea523fd3ed2a1bd171d737c731c7310000000000000000000bd790617b00000000000",
            "txinwitness": [
                "0000000000000000000000000000000000000000000000000000000000000000"
            ],
            "sequence": 4294967295
        }
    ],
    "vout": [
        {
            "value": "0.00000546",
            "n": 0,
            "scriptPubKey": {
                "asm": "OP_HASH160 8ee90177614ecde53314fd67c46162f315852a07 OP_EQUAL",
                "desc": "addr(3Eif1JfqeMERRsQHtvGEacNN9hhuvnsfe9)#lvfz5kkj",
                "hex": "a9148ee90177614ecde53314fd67c46162f315852a0787",
                "address": "3Eif1JfqeMERRsQHtvGEacNN9hhuvnsfe9",
                "type": "scripthash"
            }
        },
        {
            "value": "3.13048806",
            "n": 1,
            "scriptPubKey": {
                "asm": "OP_HASH160 6582f2551e2a47e1ae8b03fb666401ed7c4552ef OP_EQUAL",
                "desc": "addr(3Awm3FNpmwrbvAFVThRUFqgpbVuqWisni9)#j8r6vh28",
                "hex": "a9146582f2551e2a47e1ae8b03fb666401ed7c4552ef87",
                "address": "3Awm3FNpmwrbvAFVThRUFqgpbVuqWisni9",
                "type": "scripthash"
            }
        },
        {
            "value": "0E-8",
            "n": 2,
            "scriptPubKey": {
                "asm": "OP_RETURN aa21a9eddf8160967de885aa1774015f8ee0523a9aab8eee8b6f52c9c87385f5af3a8ec3",
                "desc": "raw(6a24aa21a9eddf8160967de885aa1774015f8ee0523a9aab8eee8b6f52c9c87385f5af3a8ec3)#5fh5pauj",
                "hex": "6a24aa21a9eddf8160967de885aa1774015f8ee0523a9aab8eee8b6f52c9c87385f5af3a8ec3",
                "type": "nulldata"
            }
        },
        {
            "value": "0E-8",
            "n": 3,
            "scriptPubKey": {
                "asm": "OP_RETURN 434f524501a21cbd3caa4fe89bccd1d716c92ce4533e4d4733942c01262fa046fdb8ba0dfce3753405c74aed0e",
                "desc": "raw(6a2d434f524501a21cbd3caa4fe89bccd1d716c92ce4533e4d4733942c01262fa046fdb8ba0dfce3753405c74aed0e)#29u7wlam",
                "hex": "6a2d434f524501a21cbd3caa4fe89bccd1d716c92ce4533e4d4733942c01262fa046fdb8ba0dfce3753405c74aed0e",
                "type": "nulldata"
            }
        },
        {
            "value": "0E-8",
            "n": 4,
            "scriptPubKey": {
                "asm": "OP_RETURN 455853415401000d130f0e0e0b041f120013",
                "desc": "raw(6a12455853415401000d130f0e0e0b041f120013)#39a8xnqr",
                "hex": "6a12455853415401000d130f0e0e0b041f120013",
                "type": "nulldata"
            }
        },
        {
            "value": "0E-8",
            "n": 5,
            "scriptPubKey": {
                "asm": "OP_RETURN 73797357c8ea6193f31c8b29e5e62e7a7510eee7d6013d4735db4fb1d228261f2c43e8bc772100",
                "desc": "raw(6a2773797357c8ea6193f31c8b29e5e62e7a7510eee7d6013d4735db4fb1d228261f2c43e8bc772100)#g262p8vn",
                "hex": "6a2773797357c8ea6193f31c8b29e5e62e7a7510eee7d6013d4735db4fb1d228261f2c43e8bc772100",
                "type": "nulldata"
            }
        },
        {
            "value": "0E-8",
            "n": 6,
            "scriptPubKey": {
                "asm": "OP_RETURN 52534b424c4f434b3ac79a4a8e16d76fa91e2572427696ea863d96f268ccd4a0baea9d741500829c7c",
                "desc": "raw(6a2952534b424c4f434b3ac79a4a8e16d76fa91e2572427696ea863d96f268ccd4a0baea9d741500829c7c)#ktunumfz",
                "hex": "6a2952534b424c4f434b3ac79a4a8e16d76fa91e2572427696ea863d96f268ccd4a0baea9d741500829c7c",
                "type": "nulldata"
            }
        }
    ],
    "hex": "010000000001010000000000000000000000000000000000000000000000000000000000000000ffffffff5d0324500e20202020204d696e656420627920536563706f6f6c202020209b006307ba7322b2fabe6d6d1a9e3f4dd46e31fc66c8f7d3c731ee3ac35ea523fd3ed2a1bd171d737c731c7310000000000000000000bd790617b00000000000ffffffff07220200000000000017a9148ee90177614ecde53314fd67c46162f315852a0787e6bea8120000000017a9146582f2551e2a47e1ae8b03fb666401ed7c4552ef870000000000000000266a24aa21a9eddf8160967de885aa1774015f8ee0523a9aab8eee8b6f52c9c87385f5af3a8ec300000000000000002f6a2d434f524501a21cbd3caa4fe89bccd1d716c92ce4533e4d4733942c01262fa046fdb8ba0dfce3753405c74aed0e0000000000000000146a12455853415401000d130f0e0e0b041f1200130000000000000000296a2773797357c8ea6193f31c8b29e5e62e7a7510eee7d6013d4735db4fb1d228261f2c43e8bc77210000000000000000002b6a2952534b424c4f434b3ac79a4a8e16d76fa91e2572427696ea863d96f268ccd4a0baea9d741500829c7c0120000000000000000000000000000000000000000000000000000000000000000000000000"
}

"""

