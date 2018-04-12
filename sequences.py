###########################################################################
#   Author:  William Harrell                                              #
#      PID:  99S370102                                                    #
#    Class:  PH412, Spring, 2018                                          #
#  Helpers:                                                               #
#                                                                         #
#  Program:  sequences.py                                                 #
# Due Date:  April 12, 2018                                               #
#                                                                         #
# Language:  Python 3.6                                                   #
#      IDE:  VS Code                                                      #
#                                                                         #
#  Purpose:  Demonstrate some math sequences                              #
#                                                                         #
#   "Bugs":  Fibonacci breaks down at around n = 30                       #
###########################################################################
def partial_sum(n, i, expression):
    '''return the partial sum of the expression to the nth iteration, with n starting at i'''
    if n == i:
        return eval(expression)
    return eval(expression) + partial_sum(n - 1, i, expression)

def fibonacci(n):
    '''return the nth fibonacci number'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_sequence(n):
    '''return a list of the fibonacci sequence up to the nth element'''
    sequence = []
    for i in range(0, n+1):
        sequence.append(fibonacci(i))
    return sequence