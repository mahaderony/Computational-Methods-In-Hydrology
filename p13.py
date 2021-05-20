#HW02 Problem 5 : BOD and DO problem:
import math
import matplotlib.pyplot as plt
def L(t):
    return float(Lo * (math.exp(-Kd * t)))
def D(t):
    return float(9.5-((Kd * Lo)/(Ka - Kd)) * ((math.exp(-Kd * t)) - (math.exp(-Ka * t))))
Kd = .1
Ka = .02
Lo = 12
x = []
y1 = []
y2 = []
for t in range(0, 101, 1):
    x.append(t)
    y1.append(L(t))
    y2.append(D(t))
# a : Finding the value of C after 30 days
Conc = D(30) + L(30)
print('BOD Concentration(C) after 30 days', L(30), 'mg/L')
print('DO Concentration(DO) after 30 days', D(30), 'mg/L')
# Plotting the data
plt.plot(x, y1, label='BOD', color='blue', linestyle='dashed',)
plt.plot(x, y2, label='DO', color='red',)
plt.legend()
plt.xlabel('Time (days)') # X-axis label
plt.ylabel('Concentration of BOD and DO (mg/L)') # Y-axis label
plt.title('Time vs BOD & DO')

plt.show()
# Finding Mininum DO level
print('The mininum DO level is', min(y2), 'mg/L')
for t in range(0, 101, 1):
    if D(t) == min(y2):
        print('The time to reach min DO level', t,'days')
