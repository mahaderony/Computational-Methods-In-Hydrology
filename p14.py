#HW02 Problem 5 Continued :
import math
import matplotlib.pyplot as plt
def L(t):
    return float(Lo * (math.exp(-Kd * t)))
def D(t):
    return float(9.5-((Kd * Lo)/(Ka - Kd)) * ((math.exp(-Kd * t)) - (math.exp(-Ka * t))))
Kd = .1
Ka = .09
Lo = 12
x = []
y1 = []
y2 = []
for t in range(0, 101, 1):
    x.append(t)
    y1.append(L(t))
    y2.append(D(t))
# Plotting the data
plt.plot(x, y1, label=('BOD'), color='blue', linestyle='dashed')
plt.plot(x, y2, label=('DO'), color='red',)
plt.xlabel('Time (days)') # X-axis label
plt.ylabel('Concentration of BOD and DO (mg/L)') # Y-axis label
plt.title('Time vs BOD & DO')
plt.legend()
plt.show()
# Finding Mininum DO level
print('The miminum DO level is', min(y2), 'mg/L')
if min(y2) < 2:
    print('Fish kill !!!')
elif min(y2) >= 2:
    print('DO level is satisfactory so no fish kill')