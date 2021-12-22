import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

# fmt
plt.plot(ypoints, 'p:c' , ms = 20 , mec = 'm' , mfc = 'k')
plt.text(0.7, 4, r'Waleed Soliman')
plt.show()