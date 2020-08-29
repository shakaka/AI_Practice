import hashlib
#from cryptography import fernet
from cryptography.fernet import Fernet
message = "total item is 9".encode()  # .encode() is used to turn the string to bytes
print(message)

key = Fernet.generate_key()  # Store this key or get if you already have it
f = Fernet(key)
encrypted = f.encrypt(message)
print(encrypted)

decrypted = f.decrypt(encrypted)
#message == decrypted
print(decrypted)
