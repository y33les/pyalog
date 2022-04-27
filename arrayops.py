
from functools import reduce
from operator import and_

def isAtomic(a):
    return reduce(and_,list(map(lambda x: type(x) in [int,float,str], a)))
