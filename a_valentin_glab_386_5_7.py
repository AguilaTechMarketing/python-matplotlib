import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 170, 190, 160, 300, 310, 320, 330])

# Example 1: Default Parameters
fig = plt.figure()
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y, marker='D', linestyle='dotted', color="blue")
plt.grid(color="red")
plt.savefig("gfgfg")
plt.show()

# Example 2: Custom Size
fig = plt.figure(figsize=(9, 10))
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y, marker='D', linestyle='dotted', color="blue")
plt.grid(color="red")
plt.show()

# Example 3: Figure with 72 DPI
plt.figure(figsize=(6, 6), dpi=72)
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y, marker='D', linestyle='dotted', color="blue")
plt.grid(color="red")
plt.show()

# Example 4: Increasing DPI (e.g., dpi=144)
plt.figure(figsize=(3, 3), dpi=144)
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y, marker='D', linestyle='dotted', color="blue")
plt.grid(color="red")
plt.show()