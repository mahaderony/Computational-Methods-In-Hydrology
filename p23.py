# HW04: Problem 04  Temperature of a rod problem
import math
import numpy as np
import matplotlib.pyplot as plt
D = 10
L = 100
T1 = 16
T2 = 11
T = []
j = np.arange(0, 110, 10)
for t in range(0, 510, 10):
    for x in range(0, 110, 10):
        k = T1 + (((T2-T1)*x)/L) + (2/math.pi) * (sum(((((T2 - T1) * math.cos(n * math.pi)) / n)
            * (math.sin((n * math.pi * x) / L) * (math.exp(((-D * (math.pi ** 2) * (n ** 2) * t) / (L ** 2)))))
                                                       for n in range(1, 50))))
        T.append(k)
T10 = T[0:11]
T20 = T[11:22]
T40 = T[33:44]
T80 = T[77:88]
T160 = T[165:176]
T250 = T[264:275]
T500 = T[539:550]
print(T10)
print(T20)
print(T40)
print(T80)
print(T160)
print(T250)
print(T500)
# Plotting the data
plt.xlabel('Length (cm)') # X-axis label
plt.ylabel('Temperature (deg)') # Y-axis label
plt.title('Temperature Distribution with Time')
plt.plot(j, T10, color='black', marker='o', markerfacecolor='red')
plt.plot(j, T20, color='black', marker='v', markerfacecolor='red')
plt.plot(j, T40, color='black', marker='p', markerfacecolor='red')
plt.plot(j, T80, color='black', marker='*', markerfacecolor='red')
plt.plot(j, T160, color='black', marker='x', markerfacecolor='red')
plt.plot(j, T250, color='black', marker='>', markerfacecolor='red')
plt.plot(j, T500, color='black', marker='^', markerfacecolor='red')
plt.legend(('time@10 min', 'time@20 min', 'time@40 min', 'time@80 min', 'time@160 min', 'time@250 min', 'time@500 min'))
plt.show()
