import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,2,0.1)
ytaylor=1+x+0.5*x**2+0.6*x**3+1.2*x**4
plt.plot(x,ytaylor,'b--') 
plt.show()