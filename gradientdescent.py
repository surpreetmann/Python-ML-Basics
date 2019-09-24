def J(w):
  return w[0]**2+w[1]**2+4

def grad(m):
  w=[]
  w.append(m[0]*2)
  w.append(m[1]*2)
  return w

def graddes(w,a):
  acc=0.00001
  n=[]
  r=[]
  while True:
    r=grad(w)
    r1=J(w)
    w[0]=w[0]-a*r[0]
    w[1]=w[1]-a*r[1]
    r2=J(w)
    if (r2-r1<acc):
      print('hoga')                                                                     
      break
  n.append(w[0])
  n.append(w[1])
  return n

if __name__=="__main__":
  w1=int(input())
  w2=int(input())
  #Jval=J(w1,w2)
  #w=grad(w1,w2)
  w=[]
  w.append(w1)
  w.append(w2)
  a=float(input())
  n=graddes(w,a)
  #no=np.array(n)
  print('\nw1=',int(n[0]))
  print('w2=',int(n[1]))