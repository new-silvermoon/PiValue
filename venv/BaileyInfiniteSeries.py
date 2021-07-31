"""
In 1997, David H. Bailey, Peter Borwein and Simon Plouffe published a paper (Bailey, 1997) on a new formula for π as an infinite series:

{\displaystyle \pi =\sum _{k=0}^{\infty }{\frac {1}{16^{k}}}\left({\frac {4}{8k+1}}-{\frac {2}{8k+4}}-{\frac {1}{8k+5}}-{\frac {1}{8k+6}}\right).} {\displaystyle \pi =\sum _{k=0}^{\infty }{\frac {1}{16^{k}}}\left({\frac {4}{8k+1}}-{\frac {2}{8k+4}}-{\frac {1}{8k+5}}-{\frac {1}{8k+6}}\right).}
"""

import time
import decimal


start_time = time.clock()
num_of_iterations = 100
pi = decimal.Decimal('0.0')

for i in range(num_of_iterations+1):
    pi += decimal.Decimal((1/16**i)*((4/(8*i+1)) - (2/(8*i+4)) -(1/(8*i+5)) - (1/(8*i+6))))

end_time = time.clock() - start_time
print("Time taken "+str(end_time))
print("The value of pi "+str(pi))