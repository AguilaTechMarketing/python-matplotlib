import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data for Example 1 & 2
CoursesName = ['C Course', 'C++ Course', 'Java Course', 'Python Course', ]
Student = [90, 60, 130, 190]

# Example 1: Create Simple Bar Charts Vertically
plt.bar(CoursesName, Student, color='green', width=0.3)
plt.xlabel('Courses Name')
plt.ylabel('Student Registrations number')
plt.title('Number of Students in Different Courses')
plt.show()

# Example 2: Create Simple Bar Charts Horizontally
plt.barh(CoursesName, Student, color='green', height=0.3)
plt.xlabel('Student Registration number')
plt.ylabel('Courses Name')
plt.title('Number of Student in Different Courses')
plt.show()

# Example 3.1 Matplotlib Bars - Stacked Bar Charts
StudentGroup1 = [90, 60, 130, 600]
StudentGroup2 = [100, 30, 160, 690]

plt.bar(CoursesName, StudentGroup1, color='green', width=0.3)
plt.bar(CoursesName, StudentGroup2, bottom=StudentGroup1, width=0.3)
plt.xlabel('Courses Name')
plt.ylabel('Student Registration number')
plt.title('Number of Students in Different Courses')
plt.show()

# Example 3.2: Stacked Bar plot for Rice and Wheat
years = ['2016', '2017', '2018', '2019']
rice_price = [57, 50, 47, 30]
wheat_price = [43, 50, 53, 70]

plt.figure(figsize=(10, 6))
plt.bar(years, rice_price, label='Rice')
plt.bar(years, wheat_price, bottom=rice_price, label='Wheat')
plt.xlabel('Years', fontsize=14)
plt.ylabel('Preference (%)', fontsize=14)
plt.title('The Price of Rice and Wheat', fontsize=20)
plt.legend()
plt.show()

# Example 3.3: Stacking three or more categories
rice = np.array([57, 50, 47, 30])
wheat = np.array([43, 50, 53, 70])
mustard = np.array([10, 16, 13, 15])

plt.figure(figsize=(10, 6))
plt.bar(years, rice, label='Rice')
plt.bar(years, wheat, bottom=rice, label='Wheat')
plt.bar(years, mustard, bottom=rice+wheat, label='Mustard seeds')
plt.xlabel('Years', fontsize=14)
plt.ylabel('Preference (%)', fontsize=14)
plt.title('The results of Rice, Wheat & Mustard seeds export', fontsize=20)
plt.legend()
plt.show()

# Example 4: Group Bar Charts in a Single Figure
width = 0.3
x = np.arange(len(CoursesName))

plt.bar(x - width/2, StudentGroup1, color='red', width=width, label='Student Group 1')
plt.bar(x + width/2, StudentGroup2, color='green', width=width, label='Student Group 2')
plt.xlabel('Courses Name')
plt.ylabel('Number of Students')
plt.title('Number of Students in Different Courses')
plt.xticks(x, CoursesName, rotation=45, ha='right')
plt.legend()
plt.show()

# Example 5: Creating a Bar Chart using Pandas and Matplotlib
data_ex5 = {
    'CoursesName': ['C Programming Course', 'C++ Programming Course', 'Java Programming Course', 'Python Programming Course'],
    'Student': [90, 60, 130, 600]
}
df_ex5 = pd.DataFrame(data_ex5)

plt.bar(df_ex5['CoursesName'], df_ex5['Student'], color='green')
plt.xlabel('Courses Name')
plt.ylabel('Number of Students')
plt.title('Number of Students in Different Courses')
plt.xticks(rotation=45, ha='right')
plt.show()

# Example 6: Creating a Group Bar Chart Using Pandas and Matplotlib
data_ex6 = {
    'CoursesName': ['C Programming Course', 'C++ Programming Course', 'Java Programming Course', 'Python Programming Course'],
    'Student Group 1': [90, 60, 130, 600],
    'Student Group 2': [100, 30, 160, 690]
}
df_ex6 = pd.DataFrame(data_ex6)
bar_width = 0.35
index = df_ex6.index

plt.bar(index - bar_width/2, df_ex6['Student Group 1'], bar_width, label='Student Group 1', color='blue')
plt.bar(index + bar_width/2, df_ex6['Student Group 2'], bar_width, label='Student Group 2', color='orange')
plt.xlabel('Courses Name')
plt.ylabel('Number of Students')
plt.title('Number of Students in Different Courses')
plt.xticks(index, df_ex6['CoursesName'], rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()