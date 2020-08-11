# Machin-like https://en.wikipedia.org/wiki/Machin-like_formula


import decimal
import time
import platform
import math

start_time = time.clock()

# Calculating upto 100 digits

pi = 4 * ((4 * math.atan(1/5) ) - math.atan(1/239))

print("Running on platform "+str(platform.uname()))
print("Value of Pi: " + str(pi))
print("Time taken : "+str(time.clock() - start_time))

def machin_like_formula(a_list,b_list,c_list):

    assert len(a_list) == len(b_list) and len(b_list) == len(c_list), "Length of all the three list should match"

    sum = 0
    for i in range(len(1,a_list)):
        sum += c_list[i] * math.atan(a_list[i]/b_list[i])

    pi = (4 / c_list[0]) * sum


