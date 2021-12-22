import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]
mycolors = ["#219ebc", "#023047", "#ffb703", "#fb8500"]

plt.pie(y, labels=mylabels, explode=myexplode, shadow=True, colors=mycolors)
plt.legend(title = "Four Fruits:")
plt.show()
