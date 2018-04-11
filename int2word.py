###########################################################################
#   Author:  Adam Cogdell                                                 #
#      PID:  99S370051                                                    #
#    Class:  PH412, Spring, 2018                                          #
#  Helpers:  Documentation                                                #
#                                                                         #
#  Program:  int2word module                                              #
# Due Date:  April 11, 2018                                               #
#                                                                         #
# Language:  Python 3.6                                                   #
#      IDE:  Visual Studio Code                                           #
#                                                                         #
#  Purpose:  Convert integers to strings of the numbers                   #
#                                                                         #
#   "Bugs":  No major problems                                            #
###########################################################################

# plus plus
def pp(x):
    return x+1

# minus minus
def mm(x):
    return x-1

def onth(x, y):
    if (x == 0 and y):
        return "zero"
    elif (x == 1):
        return "one"
    elif (x == 2):
        return "two"
    elif (x == 3):
        return "three"
    elif (x == 4):
        return "four"
    elif (x == 5):
        return "five"
    elif (x == 6):
        return "six"
    elif (x == 7):
        return "seven"
    elif (x == 8):
        return "eight"
    elif (x == 9):
        return "nine"
    return ""

def onth2(x):
    if (x == 0):
        return "ten"
    if (x == 1):
        return "eleven"
    if (x == 2):
        return "twelve"
    if (x == 3):
        return "thirteen"
    if (x == 4):
        return "fourteen"
    if (x == 5):
        return "fifteen"
    if (x == 6):
        return "sixteen"
    if (x == 7):
        return "seventeen"
    if (x == 8):
        return "eighteen"
    if (x == 9):
        return "nineteen"
    return ""

def secondth(x):
    if (x == 2):
        return "twenty"
    if (x == 3):
        return "thirty"
    if (x == 4):
        return "fourty"
    if (x == 5):
        return "fifty"
    if (x == 6):
        return "sixety"
    if (x == 7):
        return "seventy"
    if (x == 8):
        return "eighty"
    if (x == 9):
        return "ninety"
    return ""

def thirdth(x):
    return onth(x, 0)

def wordify(x, y=1):
    if (x%10 == x and y):
        return onth(x, 1)
    
    if (x%10 == x):
        return onth(x, 0)

    if (x%10 == x-10):
        return onth2(x%10)
    
    if (x%10 == x-x//10*10 and x//10 < 10 and x%10 == 0):
        return secondth(x//10)

    if (x%10 == x-x//10*10 and x//10 < 10):
        return secondth(x//10)+"-"+onth(x%10, 0)
    
    if (x%10 == x-x//10*10 and x//100 < 10):
        return thirdth(x//100)+" hundred "+wordify(x%100, 0)
    
    if (x%10 == x-x//10*10 and x//1000 < 1000):
        return wordify(x//1000, 0)+" thousand "+wordify(x%1000, 0)
    
    if (x%10 == x-x//10*10 and x//1000000 < 1000000):
        return wordify(x//1000000, 0)+" million "+wordify(x%1000000, 0)
    
    return ""

