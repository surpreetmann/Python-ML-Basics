# Write a function that finds out the square root of any number for some given an initial guess, using Newton-Raphson iteration.
import numpy as np
a=float(input())
x=int(input())
h=(x*x-a)/(2*x)
while abs(h)>=0.001:
  h=(x*x-a)/(2*x)
  x=x-h
print("square root of ",a,"is=",x)  
  