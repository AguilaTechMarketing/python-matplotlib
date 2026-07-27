import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 170, 190, 160, 300, 310, 320, 330])

# Example 1: Adding grid lines by using grid() function
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y, marker='D', linestyle='dotted', color="blue")
plt.grid()
plt.show()

# Example 2: Change grid color
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y, marker='D', linestyle='dotted', color="blue")
plt.grid(color="red")
plt.show()

# Example 3: Grid lines above points
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y, marker='D', linestyle='dotted', color="blue")
plt.grid(color="red")
plt.gca().set_axisbelow(False)
plt.show()

# Example 4: Grid lines style
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y, marker='D', linestyle='dotted', color="blue")
plt.grid(color="red", linestyle="dashed")
plt.show()

# Example 5: Grid Lines transparency
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y, marker='D', linestyle='dotted', color="blue")
plt.grid(color="red", linestyle="dashed", alpha=0.25)
plt.show()

# Example 6: Change background color inside the plot area
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y, marker='D', linestyle='dotted', color="blue")
plt.grid(color="red")
plt.gca().set_axisbelow(True)
plt.gca().set_facecolor('lightyellow')
plt.show()