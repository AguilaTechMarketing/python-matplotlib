import matplotlib.pyplot as plt
import numpy as np

# Example 1: Simple 1x2 subplot layout using plt.subplot()
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
plt.subplot(1, 2, 1)
plt.plot(x1, y1)
plt.title("plot 1")

x2 = np.array([0, 1, 2, 3])
y2 = np.array([10, 20, 30, 40])
plt.subplot(1, 2, 2)
plt.plot(x2, y2)
plt.title("plot 2")
plt.show()

# Example 2: Vertical stack of two subplots using plt.subplots(2, 1)
x_ex2 = [1, 2, 3, 4, 5]
y1_ex2 = [2, 3, 5, 7, 11]
y2_ex2 = [1, 4, 9, 16, 25]

fig, axs = plt.subplots(2, 1)
axs[0].plot(x_ex2, y1_ex2)
axs[0].set_title('Plot 1')
axs[0].set_xlabel('X-axis')
axs[0].set_ylabel('Y-axis')

axs[1].plot(x_ex2, y2_ex2)
axs[1].set_title('Plot 2')
axs[1].set_xlabel('X-axis')
axs[1].set_ylabel('Y-axis')

plt.tight_layout()
plt.show()

# Example 3: Creating a 2x2 Subplots Grid
x_ex3 = np.linspace(0, 2 * np.pi, 100)
y1_ex3 = np.sin(x_ex3)
y2_ex3 = np.cos(x_ex3)
y3_ex3 = np.tan(x_ex3)
y4_ex3 = np.exp(x_ex3)

fig, axes = plt.subplots(2, 2)
axes[0, 0].plot(x_ex3, y1_ex3)
axes[0, 0].set_title('Sin Function')

axes[0, 1].plot(x_ex3, y2_ex3)
axes[0, 1].set_title('Cos Function')

axes[1, 0].plot(x_ex3, y3_ex3)
axes[1, 0].set_title('Tan Function')

axes[1, 1].plot(x_ex3, y4_ex3)
axes[1, 1].set_title('Exponential Function')

plt.tight_layout()
plt.show()

# Example 4: Creating a Vertical Stack of Three Subplots
fig, axes = plt.subplots(3, 1)
axes[0].plot(x_ex3, y1_ex3)
axes[0].set_title('Sin Function')

axes[1].plot(x_ex3, y2_ex3)
axes[1].set_title('Cos Function')

axes[2].plot(x_ex3, y3_ex3)
axes[2].set_title('Tan Function')

plt.tight_layout()
plt.show()

# Example 5: Sharing Axes between Subplots in a 2x2 Grid
fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        if i == 0:
            axes[i, j].plot(x_ex3, y1_ex3)
            axes[i, j].set_title('Sin Function')
        else:
            axes[i, j].plot(x_ex3, y2_ex3)
            axes[i, j].set_title('Cos Function')

plt.tight_layout()
plt.show()