#running the pythag module

import pythag

print(pythag.hypotenuse( ))

print(pythag.leg( ))

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
