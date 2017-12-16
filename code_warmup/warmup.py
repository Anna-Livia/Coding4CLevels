########################################################
#
#            ......Authors......
#             Aurelie Jean, PhD 
#      In Silico Veritas, LLC (NYC, USA)
#         aurelie@silicoveritas.com
#
#             Alain Buzzacaro
#        OCTO Academy (Paris, France)
#            abuzzacaro@octo.com 
#            ...................
#
#          Training Coding4CLevels
#
#                2017-2018
#
########################################################

# ---------------------
# python libraries
# ---------------------
# ~> to generate random integer number
from random import randint
# ~> to track time duration and date
import datetime
import time

# ------------------------------------------------------
# Exercice 1 : Hello World!
# write a code that prints the sentence "Hello World!" 
# on your screen
# ------------------------------------------------------
print("Hello World!")

# ------------------------------------------------------
# Exercice 2 : Hello World! x 3 times
# write a code that prints 3 times on 3 different lines
# the sentence "Hello World!" on your screen
# ------------------------------------------------------
print("Hello World! \n ")
print("Hello World! \n ")
print("Hello World!")

# ------------------------------------------------------
# Exercice 3 : Hello World! x 100 times
# write a code that prints 100 times on 100 different 
# lines the sentence "Hello World!" on your screen
# ------------------------------------------------------
for i in range(100) :
    prin("Hello World! \n ")

# ------------------------------------------------------
# Exercice 4 : Use of functions
# call the function operation to compute the operation
# on a=32.4 and b=4.7, and print the result
# on the screen
# ------------------------------------------------------
def operation(a,b):
    # operation to execute on a and b
    result = (2. * a + 11. * b)/2.5
    # return the output result
    return result

a = 32.4
b = 4.7
my_result = operation(a,b)
print("my result is :")
print(my_result) 


# TO BE CONTINUED

# end of file

