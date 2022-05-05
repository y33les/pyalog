import numpy as np
from functools import reduce
from operator import and_

def toAPLArray(a):
    return np.array(a,dtype='object')

def appendAPLArray(a,b):
    return np.append(a,b)

def isAtomic(a):
    return reduce(and_,list(map(lambda x: type(x) in [int,float,str], a)))
