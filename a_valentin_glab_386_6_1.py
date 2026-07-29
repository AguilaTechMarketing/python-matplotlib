import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Example 1: Creating Simple Scatter Plots
x1 = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y1 = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

plt.grid()
plt.scatter(x1, y1, color="red", s=90)
plt.show()

# Example 2: Change the size of the dots
sizes2 = np.array([20, 50, 100, 200, 500, 1000, 60, 90, 10, 300, 600, 800, 75])
plt.scatter(x1, y1, color="red", s=sizes2)
plt.show()

# Example 3: Adjust the transparency of the dots
plt.scatter(x1, y1, s=sizes2, color="red", alpha=0.5)
plt.show()

# Example 4: Combine Color Size and Alpha
x4 = np.random.randint(100, size=(100))
y4 = np.random.randint(100, size=(100))
colors4 = np.random.randint(100, size=(100))
sizes4 = 10 * np.random.randint(100, size=(100))

plt.scatter(x4, y4, c=colors4, s=sizes4, alpha=0.5, cmap='nipy_spectral')
plt.colorbar()
plt.show()

# Example 5: Compare two Plots (Age Groups)
AgeGroupOne = range(40, 70, 1)
Purchase1 = np.abs(np.random.randn(30) * 20)
plt.scatter(AgeGroupOne, Purchase1, s=200, alpha=0.6, label='40-69 years old')
plt.scatter(AgeGroupOne, Purchase1, color='#88c999')

AgeGroupTwo = range(20, 40, 1)
Purchase2 = np.abs(np.random.randn(20) * 40)
plt.scatter(AgeGroupTwo, Purchase2, s=200, alpha=0.6, label='20-39 years old')
plt.scatter(AgeGroupTwo, Purchase2, color='#88c984')

plt.legend()
plt.xlabel("Age")
plt.ylabel("Average purchase per weekend")
plt.show()

# Example 6: Randomly generated data points for Scatter Plot Visualization
rng = np.random.RandomState(0)
x6 = rng.randn(100)
y6 = rng.randn(100)
colors6 = rng.rand(100)
sizes6 = 1000 * rng.rand(100)

plt.scatter(x6, y6, c=colors6, s=sizes6, alpha=0.3)
plt.title("Scatter chart")
plt.xlabel("Random data for x")
plt.ylabel("Random data for y")
plt.colorbar()
plt.show()

# Example 7: Real Time Data analysis and Data Visualization (Housing Prices)
housing_df = pd.read_csv("https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv")

plt.figure(figsize=(12, 8))
plt.scatter(
    x=housing_df['longitude'],
    y=housing_df['latitude'],
    alpha=0.4,
    s=housing_df['population'] / 100,
    c=housing_df['median_house_value'],
    cmap=plt.get_cmap('jet')
)
plt.colorbar(label='Median House Value')
plt.legend(['Population'])
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Housing Data Scatter Plot')
plt.show()