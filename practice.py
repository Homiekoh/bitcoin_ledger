# import hashlib
# import time
#
# # my_list = ["banana", "orange", "apple", "cherry"]
# #
# # for i in range(len(my_list)):
# #     print(my_list[i])
#
# class Block:
#     def __init__(self, index, transaction, previous_hash):
#         self.index = index
#         self.time = time.time()
#         self.transaction = transaction
#         self.previous_hash = previous_hash
#         self.nonce = 0
#         self.hash = self.calculate_hash()
#
#     def calculate_hash(self):
#         string_count = (
#                 str(self.index) +
#                         str(self.transaction) +
#                         str(self.previous_hash) +
#                         str(self.nonce) +
#                         str(self.time))
#         hashlib.sha256(string_count.encode()).hexdigest()
#
#
#         return string_count


target = "0" * 4
print(target)