import numpy as np
import math
from scipy import integrate
def Q(theta):
    def prob(theta):
        return (1/(math.sqrt(2*np.pi)))*np.exp(-.5*theta**2)
    return prob(theta)*(np.cos(theta))
QSdown =(integrate.quad(Q,0,(np.pi/2)))
QSdrip =(integrate.quad(Q,(np.pi/2),np.pi))
print(QSdown)
print(QSdrip)