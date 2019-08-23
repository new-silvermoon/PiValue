"""
To learn more about Euler Convergence, please visit the below link

http://mathworld.wolfram.com/ConvergenceImprovement.html
"""

import time
import platform
import decimal

def getFcatorial(n):

    if n== 0:
        return 1
    factorial = 1
    for i in range(1,n+1):
        factorial*=i

    return factorial

val = decimal.Decimal('0.0')
start_time = time.clock()
num_of_iterations = 2000

for i in range(0,num_of_iterations+1):
    val += decimal.Decimal(((pow(2,i) * (pow(getFcatorial(i),2))) / (getFcatorial(2*i + 1))))

pi = decimal.Decimal(2*val)

print("Running on platform "+str(platform.uname()))
print("Time taken: "+ str(time.clock() - start_time))
print("Pi value: "+str(pi))
print("Number of iterations "+str(num_of_iterations))

