import time
import hashlib

n = 100000
key = b"STR"

print(hash(key))

print(hashlib.sha256(key).hexdigest())