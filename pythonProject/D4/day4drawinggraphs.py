from matplotlib import pyplot as plt

years = [2018, 2019, 2020, 2021, 2022]
bananasales = [2000, 2200, 2600, 2100, 4000]
applesales = [1600, 1900, 2800, 3200, 3000]

plt.plot(years, bananasales, color="yellow", linestyle="solid")
plt.plot(years, applesales, color="green", linestyle="solid")
plt.title("Banana sales over time")
plt.ylabel("Millions of bananas")
plt.xlabel("Time")

plt.show()







#use pypi.org to see a list of python libraries