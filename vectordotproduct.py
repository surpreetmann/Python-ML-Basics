#Q.) Write a function which takes in as input two vectors of any size and returns as output their dot product.
import numpy as np
def dotproduct(arr1,arr2):
  pro=np.dot(arr1,arr2)
  print('arr1=',arr1)
  print('\narr2=',arr2)
  print("Product is:\n", pro)  

if __name__=="__main__":
  matrix1 = []
  matrix2 =[]
  r=int(input())
  for i in range(r):                
    matrix1.append(int(input())) 
  for i in range(r):         
    matrix2.append(int(input()))
  a=np.array(matrix1)
  b=np.array(matrix2)
  dotproduct(a,b)