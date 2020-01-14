import time
import hashlib

n = 100000
key = b"object"

print(hash(key))

print(hashlib.sha256(key).hexdigest())

print(int(hashlib.sha256(key).hexdigest(), 16) % 8)