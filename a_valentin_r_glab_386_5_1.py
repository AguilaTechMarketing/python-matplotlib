import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

# Example 1: Dashdot Line style
plt.plot(xpoints, ypoints, linestyle="dashdot")
plt.show()


# Example 2: Dotted Line style
plt.plot(xpoints, ypoints, linestyle=":")
plt.show()

# Example 3: Dash Line style
plt.plot(xpoints, ypoints, linestyle="--")
plt.show()

# Example 4: Dash Line style
plt.plot(xpoints, ypoints, linestyle="-")
plt.show()

