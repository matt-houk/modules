###########################################################################
#   Author:  Matthew Houk                                                 #
#      PID:  380131                                                       #
#    Class:  PH412, Spring, 2018                                          #
#  Helpers:  Documentation                                                #
#                                                                         #
#  Program:  Encryption module                                            #
# Due Date:  April 11, 2018                                               #
#                                                                         #
# Language:  Python 3.5.2                                                 #
#      IDE:  VIM                                                          #
#                                                                         #
#  Purpose:  Encrypt a string using a caesar cipher like approach         #
#                                                                         #
#   "Bugs":  No major problems                                            #
###########################################################################

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
        
