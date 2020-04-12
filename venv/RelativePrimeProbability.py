"""
The probability that two integers m and n picked at random are relatively prime is:

P((m,n) = 1) = 6/(pi^2)

To know more about Relatively prime, please visit:

https://mathworld.wolfram.com/RelativelyPrime.html

"""


import time, platform
from functools import reduce
from random import randint
from math import sqrt

def get_factors(num):
    factors_set = set(reduce(list.__add__,([i,int(num/i)] for i in range(1,int(num**0.5)+1) if num % i == 0)))
    factors_set.discard(1)
    return factors_set


def has_common_factors(num1,num2):
    return True if len(get_factors(num1).intersection(get_factors(num2))) > 0 else False

"""Count of random pairs having common factor"""
common_count = 0
"""Large number of pairs ensures more accurate value"""
num_of_pairs = 100000
min_range = 10
max_range = 1000

start_time = time.clock()
for n in range(0,num_of_pairs):
    if has_common_factors(randint(min_range,max_range),randint(min_range,max_range)):
        common_count+=1


probability = 1 - common_count/num_of_pairs
pi = sqrt(6/probability)
print("Running on platform "+str(platform.uname()))
print("Time taken: "+ str(time.clock() - start_time))
print("Pi: "+str(pi))