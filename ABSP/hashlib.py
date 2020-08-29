
from cryptography.fernet import Fernet

message = 'This is 5'.encode()
print(message)
keyUTF = Fernet.generate_key()
key = keyUTF.decode()

print('key is %s ' % key)
print('keyUTF is %s ' % keyUTF)

#def encrypted_message(message):
#    encode_message = message.encode('this is 5')
#     f = Fernet(keyUTF)
#    encrypted_message = f.encrypt(encode_message)

#print('content is: %s' %encrypted_message)

f = Fernet(key)
encrypted = f.encrypt(message)
print(encrypted)

decrypted = f.decrypt(encrypted)
print(decrypted)
