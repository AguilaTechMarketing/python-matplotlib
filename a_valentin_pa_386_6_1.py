import matplotlib.pyplot as plt

# Sample Data
categories = ['Groceries', 'Utilities', 'Transportation', 'Dining Out', 'Entertainment']
amounts = [500, 300, 200, 400, 250]

# Create horizontal bar chart
plt.figure(figsize=(9, 6))

# Bonus: Experiment with different color schemes and bar widths
colors = ["#028edf", "#EE0606", "#6ab66a", "#df7912", "#df02df"]
plt.barh(categories, amounts, color=colors, height=0.69)

# Add title and axis labels
plt.title('Monthly Expenses Distribution', fontsize=18, fontweight='bold')
plt.xlabel('Amount Spent', fontsize=12)
plt.ylabel('Expense Categories', fontsize=12)

plt.grid(axis='x', linestyle='-.', color="#d4af37", alpha=0.99)

# Display the chart
plt.show()