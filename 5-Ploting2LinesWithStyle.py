import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1 , linewidth = '5' , ls = '--' , c = "r")
plt.plot(y2 , linewidth = '5' , ls = ':' , c = 'b')

plt.show()