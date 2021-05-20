#STEM_INTEGRALS
import numpy as np
import math
from scipy import integrate
def Q(theta):
    def prob(theta):
        return (1/(math.sqrt(2*np.pi)))*np.exp(-.5*theta**2)
    return prob(theta)*(np.cos(theta))
cir = 1
q = 1
QSdown =cir*q*(integrate.quad(Q,0,(np.pi/2)))
QSdrip =cir*q*(integrate.quad(Q,(np.pi/2),np.pi))
print('Flow from stem to next layer\n', QSdown)
print('Drip from stem to next layer\n', QSdrip)

#LEAF_INTEGRALS
def Q(theta):
    def prob(theta):
        beta = 60 # Zenith
        fi = 71 # Azimuth
        factor = (math.gamma(fi) * math.gamma(beta)) / (math.gamma(beta+fi))
        return ((theta)**(beta-1) * (1-theta)**(fi-1))/factor
    return prob(theta)*(np.cos(theta))
cir = 1
q = 1
QLdown =cir*q*(integrate.quad(Q,0,(np.pi/2)))
QLdrip =cir*q*(integrate.quad(Q,(np.pi/2),np.pi))
print('Flow from leaf to next layer\n', QLdown)
print('Drip from leaf to next layer\n', QLdrip)

#Variables_stem
p = 1
fs = 0.4
e = .01 #evap
h = 4.8
slice = 20
alpha = 
SAI = 1.7
rad = np.arange(.16, (3.2+0.16), 0.16)/2
CIR = []
for i in range(0,19):
    C = ((math.pi*((rad[i] + rad[i+1]) * math.sqrt(((rad[i]-rad[i+1])**2) + (0.25**2))))
        *math.cos(alpha))/1.7
    CIR.append (C)
print('CIR\n',CIR)
dl = p-0.7
dls = []
for j in range(1,19): 
    dlsj = dl * (((rad[j]/rad[j-1])**2) * CIR[j]) 
    dls.append(dlsj)
print('dlsj\n', dls)

# Stem interception for oak.

