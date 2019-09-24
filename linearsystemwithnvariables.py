#Q.) Write code to take as input coefficients of a s systems of linear equation and output the solution for systems of arbitarary size.
import numpy as np
def solve(A,B,n):
  #gauss elimination
  i=0
  AB=A
  for x in AB:
    x.append(B[i])
    i=i+1  
  Ab=np.array(AB)
  print('AB =\n',Ab)
  for k in range(0,n-1):
    for i in range(k+1,n):
      if Ab[i,k]!=0:
        mul=int(Ab[i,k]/Ab[k,k])
        Ab[i,k+1:n]=Ab[i,k+1:n]-mul*Ab[i,k+1:n] 
  #back substitutuion
  x=[0]*n
  for i in range(n-1,-1,-1):
    x[i]=int((Ab[i,n]-np.dot(Ab[i,i+1:n],x[i+1:n]))/Ab[i,i])
  return x

if __name__=="__main__":
  A=[]
  B=[]
  n=int(input())
  for i in range(n):
    a=[]
    for j in range(n):
      num=int(input())
      a.append(num)
    A.append(a)  
  for i in range(n):
    a=[]
    B.append(int(input())) 
  print('A =\n',np.array(A))
  print('B =\n',np.array(B))
  X=solve(A,B,n)
  print('X =\n ',np.array(X))