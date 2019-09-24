#function with 2elements .plot all the values of function which are same for diff arguments x1 and x2
#2d plotting
import numpy as np
import matplotlib.pyplot as plt
def f(x1,x2):
  return((x1-1)**2+(x2-2)**2)

x1=np.linspace(-10,10,300)
x2=np.linspace(-10,10,300)
x1,x2=np.meshgrid(x1,x2)  
z=f(x1,x2)
plt.contour(x1,x2,z,20)
plt.annotate('',xy=[-2.5,2.5],xytext=[2.5,-10],arrowprops={'arrowstyle':'->','color':'r','lw':1},va='center',ha='center')