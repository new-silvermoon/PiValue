"""
To know more about Liu Hui method visit

https://en.wikipedia.org/wiki/Liu_Hui%27s_%CF%80_algorithm
"""

import math

init = math.sqrt(2+1)

for i in range(1,8):
    init = math.sqrt(2+init)

pi = 768 * math.sqrt(2-init)

print("Value of Pi: "+str(pi))