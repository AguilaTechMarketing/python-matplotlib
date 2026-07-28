import pandas as pd
import matplotlib.pyplot as plt

# Example 1: Reading Data from CSVs
try:
    df = pd.read_csv('employee.csv')
except Exception:
    df = pd.read_csv('employee.csv', on_bad_lines='skip')

# Example 2: Viewing or Explore your Data
print("--- First 5 rows (.head()) ---")
print(df.head())

print("\n--- First 10 rows (.head(10)) ---")
print(df.head(10))

print("\n--- Last 2 rows (.tail(2)) ---")
print(df.tail(2))

# Getting Information About your Data
print("\n--- DataFrame Info (.info()) ---")
print(df.info())

print("\n--- DataFrame Shape (.shape) ---")
print(df.shape)

# Example: Creating visualization for the CSV file (Line Graph of Salary by Age)
df = df.sort_values(by='Age')

plt.figure(figsize=(10, 6))
plt.plot(df['Age'], df['Salary'], marker='o', linestyle='-')
plt.title('Line Graph of Salary by Age')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.grid(True)
plt.show()