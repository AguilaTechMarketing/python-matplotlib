import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 4, 200, 45, 67, 56, 98, 100])

# Example 1: Diamond marker with dashed line
plt.plot(ypoints, marker='D', linestyle='--')
plt.show()

# Example 2: Square marker with dashdot line
plt.plot(ypoints, marker='s', linestyle="dashdot")
plt.show()

# Example 3: Right Triangle marker
plt.plot(ypoints, marker='>')
plt.show()

# Example 4: Thin diamond marker with red face color and edge width
plt.plot(ypoints, marker='d', markerfacecolor='red', markeredgewidth="2")
plt.show()
