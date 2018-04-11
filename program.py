#running the pythag module

import pythag

print(pythag.hypotenuse(3, 4))

print(pythag.leg(4, 5))

# int2word module - Adam
from int2word import wordify

for i in range(0, 11):
    print(wordify(i))

for i in range(110, 122):
    print(wordify(i))

for i in range(999999990, 1000000000):
    print(wordify(i))

for i in range(0, 1000000000):
    print(wordify(i))

# Running the encryption module:
string = 'Hello World!'
print(string)
encrypted = encryptblock(string)
print(encrypted)
decrypted = decryptblock(encrypted)
print(decrypted)
if decrypted == string:
    print("The string was properly encrypted and decrypted")
    
string = 'Caesarish Cipher'
print(string)
encrypted = encryptblock(string)
print(encrypted)
decrypted = decryptblock(encrypted)
print(decrypted)
if decrypted == string:
    print("The string was properly encrypted and decrypted")
