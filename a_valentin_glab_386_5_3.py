import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 170, 190, 160, 300, 310, 320, 330])

# Example 1.1: Using predefined color names
plt.plot(x, y, marker='D', linestyle='dotted', color="blue")
plt.title("Title: Sports Watch Data")
plt.xlabel("Label: Average Pulse")
plt.ylabel("Label: Calorie Burnage")
plt.show()

# Example 1.2: Using RGB tuples
plt.plot(x, y, marker='D', linestyle='dotted', color=(0.1, 0.2, 0.5))
plt.title("Title: Sports Watch Data")
plt.xlabel("Label: Average Pulse")
plt.ylabel("Label: Calorie Burnage")
plt.show()

# Example 1.3: Using hex strings color code
plt.plot(x, y, marker='D', linestyle='dotted', color="#FF5733")
plt.title("Title: Sports Watch Data")
plt.xlabel("Label: Average Pulse")
plt.ylabel("Label: Calorie Burnage")
plt.show()

# Example 1.4: Changing Title and labels color
plt.plot(x, y, marker='D', linestyle='dotted', color="#FF5733")
plt.title("Title: Sports Watch Data", color="Blue")
plt.xlabel("Label: Average Pulse", color="green")
plt.ylabel("Label: Calorie Burnage", color="red")
plt.show()

# Example 1.5: World population graph
years = [1970, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030, 2035]
pops = [3.6, 4.0, 4.4, 4.8, 5.3, 5.7, 6.1, 6.5, 7.3, 7.3, 7.3, 7.4, 7.5]

plt.title("Title: World population graph", color="Blue")
plt.xlabel("Population growth by year", color="green")
plt.ylabel("Population in Billions", color="red")
plt.plot(years, pops)
plt.show()