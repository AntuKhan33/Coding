import hashlib
from nid import information

# encode the string as UTF-8 bytes
encoded_data = information.encode('utf-8')

# create and initialize a new SHA-3 hash object with 512-bit digest size
sha3_hash = hashlib.sha3_512()

# update the hash object with the encoded data
sha3_hash.update(encoded_data)
# get the hexadecimal representation of the hashed data
hashed_data = sha3_hash.hexdigest()

print("Your hashed Data is ",hashed_data)
