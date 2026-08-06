import pandas as pd
import matplotlib.pyplot as plt

# =====================================================================
# SECTION ONE
# =====================================================================

# 1. Read Data from the woocommerce-product-export.csv file
# Ensure the CSV file is in the same directory as your Python script/notebook
try:
    df = pd.read_csv("woocommerce-product-export.csv")
except FileNotFoundError:
    print("Error: Please make sure 'woocommerce-product-export.csv' is in the same folder.")

# 2. Show a concise summary of the columns using the info() method
print("--- DataFrame Info ---")
df.info()
print("\n")

# 3. Show a summary of statistics pertaining to the columns
print("--- Summary Statistics ---")
print(df.describe())
print("\n")

# 4. Print the first five rows by default
print("--- First Five Rows ---")
print(df.head())
print("\n")

# 5. Print the last five rows by default
print("--- Last Five Rows ---")
print(df.tail())
print("\n")

# 6. Print the "total_profit" and "month_number" columns only
print("--- Total Profit and Month Number Columns ---")
print(df[['total_profit', 'month_number']])
print("\n")

# 7. Read the total profit of all months and show it using the Bar plot
plt.figure(figsize=(8, 5))
plt.bar(df['month_number'], df['total_profit'])
plt.xlabel('Month number')
plt.ylabel('Total profit')
plt.title('Company profit per month')
plt.show() # Make sure to screenshot this for your Word Doc!

# 8. Read total profit of all months and show line plot with specific styles
plt.figure(figsize=(8, 5))
plt.plot(df['month_number'], df['total_profit'], 
         label='Profit data of last year',
         color='red', 
         linestyle='dotted', 
         linewidth=3,
         marker='o', 
         markerfacecolor='black', 
         markeredgecolor='black')

plt.xlabel('Month number')
plt.ylabel('Total profit')
plt.title('Company profit per month')
plt.legend(loc='lower right')
plt.show()

# 9. Print all product sales data and show it using a multi-line plot
plt.figure(figsize=(10, 6))

# We dynamically select product columns by excluding non-product columns.
# Adjust the excluded list if your CSV has different metadata columns.
non_product_cols = ['month_number', 'total_profit', 'total_units'] 
product_columns = [col for col in df.columns if col not in non_product_cols]

for product in product_columns:
    plt.plot(df['month_number'], df[product], label=product, marker='o', linewidth=2)

plt.xlabel('Month number')
plt.ylabel('Sales units in number')
plt.title('Sales data')
plt.legend(loc='upper left')
plt.show()

# 10. Read “bathingsoap” sales data for each month and show using a scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(df['month_number'], df['bathingsoap'], label='Bathing soap Sales data')
plt.xlabel('Month number')
plt.ylabel('Sales units in number')
plt.title('Bathingsoap Sales data')
plt.legend(loc='upper left')
plt.grid(True, linestyle='--') # Adding the dashed grid line
plt.show()


# =====================================================================
# SECTION TWO
# =====================================================================

# 11. Date vs Temperature Line Chart
date = ["25/12", "26/12", "27/12"]
temp = [8.5, 10.5, 6.8]

plt.figure(figsize=(6, 4))
plt.plot(date, temp, marker='o')
plt.xlabel('Date')
plt.ylabel('temperature')
plt.title('Date-wise Temperature')
plt.show()

# 12. Average Weight vs Average Height Chart
height = [121.9, 124.5, 129.5, 134.6, 139.7, 147.3, 152.4, 157.5, 162.6]
weight = [19.7, 21.3, 23.5, 25.9, 28.5, 32.1, 35.7, 39.6, 43.2]

plt.figure(figsize=(8, 5))
plt.plot(weight, height, 
         label='Weight vs Height',
         color='green', 
         linestyle='dashdot', 
         marker='o', 
         markersize=10, 
         markerfacecolor='green',
         markeredgecolor='green')

plt.xlabel('Weight in kg.')
plt.ylabel('Height in cm.')
plt.title('Average weight with respect to average height.')
plt.legend(loc='lower right')
plt.show()