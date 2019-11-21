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
#          Training #Coding4CLevels
#
#                2017-2018

#         Edited by Anna-Livia Gomart
#                    2019
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


print("\n----------------------------")
print("        WARMUP 1")
print("----------------------------")
# ------------------------------------------------------
# Warmup 1 : The types in Python
# ------------------------------------------------------
my_variable = "Hello"
print(my_variable)
print(type(my_variable))

my_variable = 4
print(my_variable)
print(type(my_variable))

my_variable = 4.0
print(my_variable)
print(type(my_variable))

my_variable = [3, 4, 2, 0, 1]
print(my_variable)
print(type(my_variable))

my_variable = {
    "eggs": 3,
    "milk": 4,
    "butter": 2,
}
print(my_variable)
print(type(my_variable))


print("\n----------------------------")
print("        WARMUP 2a")
print("----------------------------")
# ------------------------------------------------------
# Warmup 2a : Hello World!
# write a code that prints the sentence "Hello World!"
# on your screen
# ------------------------------------------------------
print("Hello World!")


print("----------------------------")
print("        WARMUP 2b")
print("----------------------------")
# ------------------------------------------------------
# Warmup 2b : Hello World! x 3 times
# write a code that prints 3 times on 3 different lines
# the sentence "Hello World!" on your screen
# ------------------------------------------------------
print("Hello World!")
print("Hello World!")
print("Hello World!")

print("----------------------------")
print("        WARMUP 3")
print("----------------------------")
# ------------------------------------------------------
# Warmup 3 : Hello World! x 100 times
# write a code that prints 100 times on 100 different
# lines the sentence "Hello World!" on your screen
# ------------------------------------------------------
for i in range(100) :
    print("Hello World!")


print("----------------------------")
print("        WARMUP 4")
print("----------------------------")
# ------------------------------------------------------
# Warmup 4 : Incrementing in Python
# ------------------------------------------------------
# initialization of the variable roll_call
roll_call = 0

all_students = 32 # total number of students
# loop over all the students
for i in range(all_students):
    roll_call += 1
    # roll_call = roll_call + 1
    print(roll_call)


print("\n----------------------------")
print("        WARMUP 5")
print("----------------------------")
# ------------------------------------------------------
# Warmup 5 : if loop
# ------------------------------------------------------
names = ["Alain", "Emmanuelle", "Naomie", "Loubna", "John", "Said", "Catherine"]
for name in names:
    # if the name has more than 6 characters
    if len(name) > 6:
        print(f"the name : {name} has more than 6 characters")
    else :
        print(f"the name : {name} has less than 7 characters")


print("\n----------------------------")
print("        WARMUP 6")
print("----------------------------")
# ------------------------------------------------------
# Warmup 6 : Lists in Python
# ------------------------------------------------------
my_list = [7, 349, 2, 45, 2, 83, 1, 8, 930]
first_value = my_list[0]
print(first_value)
third_value = my_list[2]
print(third_value)
last_value = my_list[len(my_list)-1]
print(last_value)
last_value_short = my_list[-1]
print(last_value_short)


print("\n----------------------------")
print("        WARMUP 7")
print("----------------------------")
# ------------------------------------------------------
# Warmup 7 : Dictionnaries in Python
# ------------------------------------------------------
groceries = {"eggs" : 12, "bananas" : 4, "tomatoes" : 10}

number_of_eggs = groceries["eggs"]
print(number_of_eggs)

total = groceries["eggs"] + groceries["bananas"] + groceries["tomatoes"]
print(total)

total = 0
for value in groceries.values():
    total += value
print(total)

print("\n----------------------------")
print("        WARMUP 8")
print("----------------------------")
# ------------------------------------------------------
# Warmup 8 : Use of functions
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
print(f"my result is : {my_result}")

# end of file
