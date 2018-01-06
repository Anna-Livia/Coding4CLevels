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
#                2018
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

# -----------------------------------
# GLOBAL VARIABLES 
# -----------------------------------

# ..........................................................................
# countries a container of all countries from which the reviewer could
# come from. 
# ..........................................................................
countries = ['France', 'Brazil', 'Tunisia', 'Argentina', 'Italy', 'Israel', \
             'Kenya', 'Sweden', 'Japan', 'Russia', 'Germany', 'Greece', 'USA', 'UK']

# -----------------------------------
# FUNCTIONS 
# -----------------------------------

# ..........................................................................
# reviews_generator a function that generates a random set of parameters 
# for a review.
#
# ~> how to call the function:  my_review = review_generator() 
# ~> example of result: [1, 'Italy', 35] 
#    that is read [review, country of residence of reviewer, age of reviewer]
# ..........................................................................
def reviews_generator() :
    # review container -> review number [0:5], country and age
    review = []
    # get arithmetic review
    review_value = randint(0,5)
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

# artificial time (would not exist in the real code)
now = datetime.datetime.now()
minute = now.minute

# ------------------ FOR THE SECOND PART
# initialization of the containers of count of reviewers
# for country of residence and for age
# ~> country of residence
country_count = { 'France':0.0, 'Brazil': 0.0, 'Tunisia':0.0, 'Argentina':0.0, \
                  'Italy':0.0, 'Israel':0.0, 'Kenya':0.0, 'Sweden':0.0, \
                  'Japan':0.0, 'Russia':0.0, 'Germany':0.0, 'Greece':0.0, \
                  'USA':0.0, 'UK':0.0 } 
# ~> age
age_count = { '18-30':0.0, '31-40':0.0, '41-50':0.0, '51-':0.0 }
# ---------------------------------------

# number of online reviews
NumberOfReviews = 10000

# to get the time of execution
start_time = time.time()

# loop over the number of reviews
for x in range(NumberOfReviews):
    # get review 
    review = reviews_generator()
    # value, country of residence and age
    review_value = review[0] # first element in the container
    reviewer_country = review[1] # second element in the container
    reviewer_age = review[2] # third element in the container

    # check the country of residence and add it to the count container
    country_count[reviewer_country] += 1     
    # check the age and add it to the count container
    if reviewer_age < 31 :
        age_count['18-30'] += 1    
    elif reviewer_age < 41 :
        age_count['31-40'] += 1    
    elif reviewer_age < 51 :
        age_count['41-50'] += 1    
    else :
        age_count['51-'] += 1    

    # update the number of reviews
    NumberReviews = NumberReviews + 1
    # compute the sum
    Sum = Sum + review_value
    # compute the average
    average = Sum / NumberReviews

# PRINT ON SCREEN --------------------------------
# ~> print the average
print("\n")
print("------> The average is %f" %average)
print("\n")

# ~> print the execution time
print("------> execution time : %s seconds" % (time.time() - start_time))

print('\n')

# ~> print the age count
print("------> Ages of the reviewers:")
print(age_count)

print('\n')

# ~> print the country count
print("------> Countries of residence of the reviewers:")
print(country_count)

print('\n')

# end of file

