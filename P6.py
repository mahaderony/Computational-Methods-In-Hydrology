# Problem 06 : Temperature of a rod problem
import math
import numpy as np
import matplotlib.pyplot as plt
D = 10
L = 96
T1 = 18
T2 = 12
T = []
j = np.arange(0, 108, 12)
for t in range(0, 1440, 15):
    for x in range(0, 108, 12):
        k = T1 + (((T2-T1)*x)/L) + (2/math.pi) * (sum(((((T2 - T1) * math.cos(n * math.pi)) / n)
            * (math.sin((n * math.pi * x) / L) * (math.exp(((-D * (math.pi ** 2) * (n ** 2) * t) / (L ** 2)))))
                                                       for n in range (1, 50))))
        T.append(k)
T15 = T[0:9]
T30 = T[9:18]
T45 = T[18:27]
T60 = T[27:36]
T75 = T[36:45]
# Plotting the data
plt.xlabel('Length (cm)') # X-axis label
plt.ylabel('Temperature (deg)') # Y-axis label
plt.title('Temperature Distribution with Time')
plt.plot(j, T15, color='black', marker='o', markerfacecolor='red')
plt.plot(j, T30, color='black', marker='v', markerfacecolor='red')
plt.plot(j, T45, color='black', marker='p', markerfacecolor='red')
plt.plot(j, T60, color='black', marker='*', markerfacecolor='red')
plt.plot(j, T75, color='black', marker='x', markerfacecolor='red')
plt.legend(('time@15 min', 'time@30 min', 'time@45 min', 'time@60 min', 'time@75 min'))
plt.show()
