#plotting histogram
import numpy as np
import matplotlib.pyplot as plt
import time

x = np.random.uniform(0,1,1000) 
y=np.random.normal(0,1,1000) #(mean,std. deviation, )
z=np.random.normal(10,20,1000)

res = plt.hist(z,bins=20)