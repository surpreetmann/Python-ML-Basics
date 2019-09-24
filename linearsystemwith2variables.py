#Q.) Write a function that takes as input a linear system with 2 equations and gives the solutions.
import numpy as np
def solve(A,B):
  #gauss elimination
  i=0
  AB=A
  for x in AB:
    x.append(B[i])
    i=i+1  
  Ab=np.array(AB)
  print('AB =\n',Ab)
  mul=int(Ab[1,0]/Ab[0,0])
  Ab[1,:]=Ab[1,:]-mul*Ab[0,:]
  #back substitutuion
  x=[0]*2
  x[1]=int(Ab[1,2]/Ab[1,1])
  x[0]=int((Ab[0,2]-Ab[0,1]*x[1])/Ab[0,0])
  return x

if __name__=="__main__":
  A=[]
  B=[]
  for i in range(2):
    a=[]
    for j in range(2):
      num=int(input())
      a.append(num)
    A.append(a)  
  for i in range(2):
    a=[]
    B.append(int(input())) 
  print('A =\n',np.array(A))
  print('B =\n',np.array(B))
  X=solve(A,B)
  print('X =\n ',np.array(X))