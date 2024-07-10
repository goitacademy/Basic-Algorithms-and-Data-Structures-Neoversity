import hashlib

print(hash("Yaroslav"))
print(hash("Anatoliy"))
print(hash("Oleksandr"))
print(hash("Miko"))

hash_data = hashlib.sha256("Yaroslav".encode())
print(hash_data.hexdigest())