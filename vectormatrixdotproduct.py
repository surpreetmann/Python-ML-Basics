#Q.) Write a function which takes in a matrix and vector of any size and return their dot product
import numpy as np
def dotproduct(mat,vec):
  print('matrix=\n',mat)
  print('\nvector=\n',vec)
  pro=np.dot(mat,vec)
  print('Product = ',pro)
  
if __name__=="__main__":
  r=int(input())
  c=int(input())
  n=int(input())
  m=[]
  v=[]
  for i in range(r):
    a=[]
    for j in range(c):
      num=int(input())
      a.append(num)
    m.append(a)
  mat=np.array(m)  
  for i in range(n):
    v.append(int(input()))
  vec=np.array(v) 
  dotproduct(mat,vec)