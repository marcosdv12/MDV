import numpy as np
from scipy.special import comb

def probBoth(infecRatio,groupSize):
    probOne = 0
    for i in range(1,groupSize//2 + 1):
        probOne += 2*comb(groupSize/2,i)*np.power(infecRatio,i)*np.power(1-infecRatio,groupSize-i)

    probOne /= (1 - np.power(1-infecRatio,groupSize))
    return 1 - probOne

def expectedSamplesOne(infecRatio,groupSize):
    if groupSize == 1:
        return 1

    return 3 + (1 + probBoth(infecRatio,groupSize))*(expectedSamplesOne(infecRatio,groupSize//2) - 1)

def expectedSamplesGeneral(infecRatio,groupSize):
    ES1 = expectedSamplesOne(infecRatio,groupSize)
    return ES1 + np.power(1-infecRatio,groupSize)*(1 - ES1)

for p in range(1700,1800):
    print (p/10000,expectedSamplesGeneral(p/10000,32))