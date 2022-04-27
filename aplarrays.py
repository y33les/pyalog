# TODO: implement pyspark version?
import numpy as np
from functools import reduce
from operator import and_

# This is the goer I think
# TODO: Need to handle enclosing (i.e. a one-item array array)
# TODO: Need to handle arrays of arrays vs multidimensional arrays
class APLArray(np.ndarray):
    _scalar_types = [int,float,str]

    def __typecheck(cls,x):
        if not type(x) in cls._scalar_types+[APLScalar,APLArray]:
            return False
        elif isinstance(x,str) and len(x)!=1:
            return False
        else:
            return True

    def __new__(cls,*args):
        if not reduce(and_,list(map(lambda x: cls.__typecheck(cls,x), args))):
            raise TypeError

        # Convert args to APLArrays (or maybe APLScalars?)?
        return np.asarray(list(map(lambda x: APLScalar(x) if type(x) in cls._scalar_types else x,args)),dtype=object).view(cls)

    def __array_finalize__(self,obj):
        if obj is None: return

class APLScalar(APLArray):
    def __new__(cls,value):
    # TODO: additional types (e.g. complex numbers, functions, dfns,
    #       maybe even objects in general (i.e. Python types)?
        if ((not (type(value) in super()._scalar_types)) or
            (isinstance(value,str) and len(value)!=1)):
                raise TypeError
        return np.asarray(value).view(cls) # Do we need dtype=object here?

# TODO: is this even necessary, or is this just handled by the AST?
#       is this something that will be convertible to an AST?
#       is this an APLExpression, rather than a function?
#       might be better handled by just being an AST node
class APLFunction: # monads just have self.left = None, nilads have both as None
    def __init__(self,f,alpha=None,omega=None):
        self.function = f
        self.left = alpha
        self.right = omega
    # TODO: methods, including evaluate
    #       - will need recursive evaluate if leaves are more p-ads

# TODO: operators?
