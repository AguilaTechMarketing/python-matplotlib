import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 170, 190, 160, 300, 310, 320, 330])

# Example 1: Styling Custom Fonts using Keyword Arguments
plt.plot(x, y, marker='D', linestyle='dotted', color="#FF5733")
plt.title("Title: Sports Watch Data", fontweight='bold', fontsize=30, color="green")
plt.xlabel("Label: Average Pulse", color='red', fontweight='bold', fontsize=20)
plt.ylabel("Label: Calorie Burnage", color='blue', fontfamily='monospace', fontweight="bold", fontsize=20)
plt.show()

# Example 2: Styling Custom Fonts using fontdict parameter
plt.plot(x, y, marker='D', linestyle='dotted', color="#FF5733")

title_font = { 'family': 'serif', 'color': 'green', 'weight': 'bold', 'size': 40 }
plt.title('Title: Sports Watch Data', fontdict=title_font)

label_font = { 'family': 'sans-serif', 'color': 'red', 'weight': 'normal', 'size': 20 }
plt.xlabel('X Label: Average Pulse', fontdict=label_font)
plt.ylabel('Y Label: Calorie Burnage', fontdict=label_font)
plt.show()
