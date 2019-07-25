"""
To know more about the Madhava-Leibniz approach of estimating the value of pi, please visit:

https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
"""

import time
import platform


num_of_iterations = 400000
pi = 0

start_time = time.clock()
for i in range(num_of_iterations+1):
    denom = i * 2 + 1
    pi = (pi+(1/denom)) if i % 2 == 0 else (pi-(1/denom))

print("Time taken "+str(time.clock() - start_time))
print("Value of Pi: ")
print(pi*4)
print("Iterations "+str(num_of_iterations))
