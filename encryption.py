offset = 3

def encryptchar(char):
    global offset
    newchar = chr(ord(char)+offset)
    return newchar

def decryptchar(char):
    global offset
    oldchar = chr(ord(char)-offset)
    return oldchar

def encryptblock(block):
    newblock = ''
    for char in block:
        newblock += encryptchar(char)
    return newblock

def decryptblock(block):
    oldblock = ''
    for char in block:
        oldblock += decryptchar(char)
    return oldblock
        
