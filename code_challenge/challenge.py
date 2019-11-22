########################################################
#
#            ......Authors......
#             First and Last Name 
#                 Affiliation
#                email address
#
#             First and Last Name 
#                 Affiliation
#                email address
#            ...................
#
#           Training #Coding4CLevels
#        Aurélie Jean (In Silico Veritas)
#         Alain Buzzacaro (OCTO Academy)
#
#                    2018
#
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
    reviewer_age = randint(18, 100)

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
### ADD CODE ###

# artificial time (would not exist in the real code)
now = datetime.datetime.now()
minute = now.minute

# ------------------ FOR THE SECOND PART

# initialization of the containers of count of reviewers
# for country of residence and for age
# ~> country of residence
# the values are organisaed such as [number of reveiws, sum of reviews]
country_count = { 
    'France':[0,0], 
    'Brazil': [0,0], 
    'Tunisia':[0,0], 
    'Argentina':[0,0],
    'Italy':[0,0],
    'Israel':[0,0],
    'Kenya':[0,0], 
    'Sweden':[0,0],
    'Japan':[0,0],
    'Russia':[0,0], 
    'Germany':[0,0],
    'Greece':[0,0],
    'USA':[0,0],
    'UK':[0,0]
     } 
# ~> age
age_count = { '18-30':[0,0], '31-40':[0,0], '41-50':[0,0], '51-':[0,0] }

# ---------------------------------------



value = 0
iteration = 1000

for element in range (iteration):
    review = reviews_generator()
    note = review[0]
    pays = review[1]
    country = country_count[pays]
    country[0] += 1
    country[1] += note
for country_name, score in country_count.items() :
    print (f"{country_name} : {score[1]/score[0]}")



value = 0
iteration = 2
for element in range (iteration):
    result = reviews_generator()
    value = result[0]+value
    print(value)
moyenne = value/iteration
print(moyenne)



iteration = 10000

for element in range (iteration):
    review = reviews_generator()
    note = review[0]
    age = review[2]
    if  age <31:
        age_count["18-30"][0] += 1
        age_count["18-30"][1] += note
    elif age <41:
        age_count["31-40"][0] += 1
        age_count["31-40"][1] += note
    elif age <51:
        age_count["41-50"][0] += 1
        age_count["41-50"][1] += note
    else:
        age_count["51-"][0] += 1
        age_count["51-"][1] += note
        

for category_age, score in age_count.items() :
    print (f"{category_age} : {score[1]/score[0]}")

# DO THE CALCULATION -----------------------------

# number of online reviews
### ADD CODE ###

# to get the time of execution
start_time = time.time()

# loop over the number of reviews
### ADD CODE ###

# ------------------------------------------------



# PRINT ON SCREEN --------------------------------
print('\n')

### ADD CODE ###

print('\n')

# ------------------------------------------------



# end of file

