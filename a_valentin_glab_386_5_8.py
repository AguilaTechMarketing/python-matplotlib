import matplotlib.pyplot as plt

years = [1950, 1955, 1960, 1965, 1970, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015]
pops = [2.5, 2.7, 3.0, 3.3, 3.6, 4.0, 4.4, 4.8, 5.3, 5.7, 6.1, 6.5, 7.3]
death = [1.2, 1.1, 1.2, 2.1, 2.0, 2.3, 1.8, 1.9, 2.6, 1.6, 2.4, 2.4, 4.0]
job_rate = [0.5, 0.6, 0.8, 0.9, 1.0, 1.2, 1.5, 1.7, 2.0, 2.2, 2.5, 2.7, 2.9]

# Example 1: Creating multiple lines for World Population Graph
plt.plot(years, pops, color=('red'))
plt.plot(years, death, color=('green'))
plt.ylabel("Population in Billions")
plt.xlabel("Population growth by year")
plt.title("Population Growth")
plt.show()

# Example 2: Changing line style
plt.plot(years, pops, '--', color=('red'))
plt.plot(years, death, '-.', color=('green'))
plt.ylabel("Population in Billions")
plt.xlabel("Population growth by year")
plt.title("Population Growth")
plt.show()

# Example 3: Adding markers for each line
plt.plot(years, pops, '--', color=('red'), marker="*")
plt.plot(years, death, '-.', color=('green'), marker="*")
plt.ylabel("Population in Billions")
plt.xlabel("Population growth by year")
plt.title("Population Growth")
plt.show()

# Example 4: Adding legend for each line
plt.plot(years, pops, '--', color=('red'), marker="*", label="population")
plt.plot(years, death, '-.', color=('green'), marker="*", label="death")
plt.ylabel("Population in Billions")
plt.xlabel("Population growth by year")
plt.title("Population Growth")
plt.legend()
plt.show()

# Example 5: Adding job rate line graph
plt.figure(figsize=(10, 10))
plt.plot(years, pops, '--', color='red', marker="*", label="population")
plt.plot(years, death, '-.', color='green', marker="*", label="death")
plt.plot(years, job_rate, ':', color='blue', marker="*", label="job rate")
plt.ylabel("Population in Billions")
plt.xlabel("Population growth by year")
plt.title("Population Growth")
plt.legend()
plt.show()
