import matplotlib.pyplot as plt
import numpy as np 

# x = np.arange(-4,4,.1)
# x = np.linspace(-4,4,25)
x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)
# y = np.square(x)
y2 = np.cos(x)
# y2 = y+2
plt.grid(True)
plt.xlabel("sin X")
plt.ylabel("cos X")
plt.title("My Graph")
# plt.axis([0,5, 2, 11])
plt.plot(x, y, 'r-*', linewidth = 2, markersize = 7, label='Red') #r=red colour, - continous line, * is points
plt.plot(x, y2, 'b-o', linewidth = 2, markersize = 7, label='blue')
plt.legend(loc='lower left')#loc defines location
plt.show()
