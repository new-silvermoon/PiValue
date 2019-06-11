# PiValue
This project contains a list of mathematical approaches expressed in terms of code, i order to calculate the value of Pi. This can be used to benchmark computer systems in order to meausure their floating point operation speeds.

1. <b>Mandelbrot approach</b>
The Mandelbrot set is the set of complex numbers c for which the function f(z)=z^{2}+c
does not diverge when iterated from z=0, i.e.,
for which the sequence f(0),f(f(0)) etc., remains bounded in absolute value.

---Calculating the value of Pi-----
The value lies within a Mandelbrot set if f(z) <= 2
Considering the equation f(z)=z^{2}+c, the value of c at the cusp of Mandelbrot set is 0.25
Now, if we add a slight increment (e) to the value and apply it to the above equation, eventually the value of f(z)
will exceed 2.

The number of Iterations required for f(z) to exceed the value of 2, will give us the value of Pi (Provided we place
the decimal point at the correct place)
