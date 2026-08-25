import matplotlib
import matplotlib.pyplot as plt
import numpy as np
#===========================================================

# x=np.array([1,2,3,4,5])
# y=np.array([2,4,6,8,10])
# plt.plot(x,y)
#===========================================================

# x=np.array([1,2,3,4,5])
# y=np.array([0,1,0,1,0])
# plt.plot(x,y)

# a,b,c=1,2,3
# x=2
# y=a* x**2 + b*x +c

# x=np.linspace(-4,4,100)
# #================================================================
plt.title("Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
x=np.array([10,15,20,25,30])
y=np.array([20,25,30,35,40])
plt.plot(x,y,linestyle="dotted")
plt.show()



