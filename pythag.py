###########################################################################
#   Author:  Chase Overpeck                                               #
#      PID:  99s380241                                                    #
#    Class:  PH412, Spring, 2018                                          #
#  Helpers:  n/a                                                          #
#                                                                         #
#  Program:  Modules Assignment                                           #
# Due Date:  April 12, 2018                                               #
#                                                                         #
# Language:  Python 2.7                                                   #
#      IDE:  Trinket                                                      #
#                                                                         #
#  Purpose:  Module for finding hypotenuse and a leg of a right triangle  #
#            using pythagorean theorem                                    #
#                                                                         #
#   "Bugs":  No major problems                                            #
###########################################################################

def hypotenuse(a, b):
    c = (a**2 + b**2)**0.5
    return c
def leg(a, c):
    b = (c**2 - a**2)**0.5
    return b
