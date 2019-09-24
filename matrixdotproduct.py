#Q.) Write a function which takes in a matrix and matrix of any size and return their dot product.
import numpy as np
def dotproduct(mat1,mat2):
  print('matrix1=\n',mat1)
  print('\nmatrix2=\n',mat2)
  pro=np.dot(mat1,mat2)
  print('Product = ',pro)
  
if __name__=="__main__":
  r1=int(input())
  c1=int(input())
  r2=int(input())
  c2=int(input())
  m1=[]
  m2=[]
  for i in range(r1):
    a=[]
    for j in range(c1):
      num=int(input())
      a.append(num)
    m1.append(a)
  mat1=np.array(m1)
  for i in range(r2):
    a=[]
    for j in range(c2):
      num=int(input())
      a.append(num)
    m2.append(a)
  mat2=np.array(m2)
  
  dotproduct(mat1,mat2)