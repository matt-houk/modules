#running the pythag module - chase

print('\n Testing pythag.py \n')

import pythag

print(pythag.hypotenuse(3, 4))

print(pythag.leg(4, 5))

# int2word module - Adam

print('\n Testing int2word.py \n')

from int2word import wordify

for i in range(0, 11):
    print(wordify(i))

for i in range(110, 122):
    print(wordify(i))

for i in range(999999990, 1000000000):
    print(wordify(i))


# Running the encryption module:

print('\n Testing encryption.py \n')

from encryption import encryptblock, decryptblock

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

# Running the sequences module - william

print('\n Testing sequences.py \n')

import sequences

print("Partial sum of 1/10**n to 5th element:", sequences.partial_sum(5, 0, "1/10**n"))
print("5th Fibonacci number:", sequences.fibonacci(5))
print(sequences.fibonacci_sequence(10))
