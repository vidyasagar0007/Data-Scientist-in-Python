# import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  this is stright line @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# ====================================================================================
# x=np.array([1,2,3,4,5])
# y=np.array([2,4,6,8,10])
# =====================================================================================

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  this is zigzag line @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# ===================================================================================
# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
# ===================================================================================

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  this is zigzag line @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#=====================================================================================
# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
# x1=np.array([0,1,2,3,4,5])
# y1=np.array([0,1,0,1,0,1])
# plt.plot(x, y)
# plt.plot(x1,y1,color="blue",linestyle="dotted")
#=====================================================================================
#======================================================================================
# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
# plt.subplot(2,2,2)
# plt.plot(x,y,color="Red")
# plt.title("Priyanshu Line Graph")
# plt.xlabel("Aman-axis")
# plt.ylabel("Sachin-axis")
# x1=np.array([1,2,3,4,5,6,7,8,9,10])
# y1=np.array([0,1,0,1,0,1,0,1,0,1])
# plt.subplot(2,2,3)
# plt.plot(x1,y1,marker='*',linestyle='dashed',color="Blue")
# plt.title("Vidya Line Graph")
# plt.xlabel("Aman-axis")
# plt.ylabel("Sachin-axis")
# plt.grid()

#======================================================================================
month=['jan','feb','Mar','apr','may']
revenue=[12000,45000,56000,89000,65000]
plt.figure(figsize=(8,4))
plt.plot(month,revenue,color="green",marked='o',lineStyle="dashed")
plt.title("Month and Revenue Graph")
plt.xlabel("Months")
plt.ylabel("revenue")
plt.grid(True,linestyle=':',alpha=0.6)
# plt.savefig('renenue_trend.png',dp)
plt.show()
