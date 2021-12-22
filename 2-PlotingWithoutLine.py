import sys
import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])


plt.plot(xpoints, ypoints, 'o')
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
