# Problem 03 :  Well Draw-down problem
import math
import matplotlib.pyplot as plt
x = []
y = []
Q = float(input('Enter flow rate in cfs'))
k = float(input('Enter coefficient of permeability in fps'))
h1 = float(input('Enter height of water surface above bottom aquifer h1 in ft'))
r1 = float(input('Enter the radius to water surface at perimeter of well r1 in ft'))
# Using For loop to find r2
for h2 in range(50, 400, 50):
    y.append(h2)  # Putting the values in the array to plot
    r2 = float(math.e ** (((math.pi * k * (h2 ** 2 - h1 ** 2)) / Q) + (math.log(r1))))
    x.append(r2)  # Putting the values in the array to plot
# Plotting the data
plt.plot(x, y, color='black', marker='o', markerfacecolor='red')
plt.xlabel('h2 (ft)') # X-axis label
plt.ylabel('r2 (ft)') # Y-axis label
plt.title('r2 vs h2')
plt.show()
