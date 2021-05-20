# Problem 02:  Calculating the steady‐state current in an alternating L‐C (inductor‐capacitor) circuit
import math
E = int(input('Enter the Voltage in volt'))
R = int(input('Enter the Resistance in ohms'))
L = float(input('Enter the Inductance in henry '))
C = float(input('Enter the Capacitance farad '))
# Calculating Omega
Omega = float(math.sqrt((1 / (L * C)) - (R ** 2 / (4 * (L ** 2)))))
# Calculating Current
i = float(E / (math.sqrt((R ** 2) + ((Omega * L) - (1 / (Omega * C))) ** 2)))
print('The current is', i)
