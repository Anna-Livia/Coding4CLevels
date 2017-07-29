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
#           Training Code4CLevels
#
#                   2017
#
########################################################

# python libraries
# for random integer
from random import randint
# for time
import datetime
import time

# -----------------------------------
# GLOBAL VARIABLES 
# -----------------------------------
countries = ['France', 'UK', 'Italy', 'Portugal', 'Sweden', 'Germany', \
             'Greece', 'USA', 'Mexico', 'Canada', 'Brazil', 'Japan', 'Australia',\
             'India', 'China', 'Tunisia', 'Russia', 'Irland', 'Kenya']



# -----------------------------------
# FUNCTIONS 
# -----------------------------------

def reviews_generator(bound1, bound2) :
    # review container -> review number [0:5], country and age
    review = []
    # get arithmetic review
    review_value = randint(bound1, bound2)
    # get country
    reviewer_country = countries[ randint(0, len(countries)-1) ]
    # get age (between 16 and 100 years old)
    reviewer_age = randint(16, 100)
 
    # append parameters to the review container
    review.append(review_value)
    review.append(reviewer_country)
    review.append(reviewer_age)

    # end of function, return the review
    return review

# -----------------------------------
# END OF FUNCTIONS 
# -----------------------------------

# -----------------------------------
# MAIN CODE 
# -----------------------------------

# storage
Sum = 0.0
NumberReviews = 0
average = 0.0

# artificial time (would not exist in the code)
now = datetime.datetime.now()
minute = now.minute

# number of online reviews
NumberOfReviews = 10000
# loop over a certain number of reviews
for x in range(NumberOfReviews):
    # get review 
    review = reviews_generator(0,5)
    review_value = review[0] # first element in the container
    print("review = %d" %review_value)
    # update the number of reviews
    NumberReviews = NumberReviews + 1
    # compute the sum
    Sum = Sum + review_value
    # compute the average
    average = Sum / NumberReviews
    # update time
    now = datetime.datetime.now()
    minute = now.minute

# to get the time of execution
start_time = time.time()

#print the average on screen
print ("\n")
print ("Sum = %d and Number of Reviews = %d" %(Sum, NumberReviews))
print ("--------------> The average is %d" %average)
print ("\n")

print("--- %s seconds ---" % (time.time() - start_time))

# end of file

