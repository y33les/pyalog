# TODO: implement pyspark version?
import numpy as np

# TODO: type checking
class APLArray(np.ndarray):
    def __init__(self,values,rank=0):
        for i in values:
            if not (isinstance(i,APLScalar) or
                    isinstance(i,APLVector) or
                    isinstance(i,APLArray)):
                raise TypeError
        self.value = np.array(values,dtype=object)
        self.dimension = None # FIXME
        self.rank = rank # TODO: can this be automated?
        self.depth = None # FIXME
    # TODO: methods

class APLVector(APLArray):
    def __init__(self,values):
        for i in values:
            if not isinstance(i,APLScalar):
                raise TypeError
        super().__init__(self,values,1)
        self.value = np.array(values,dtype=object)
        self.dimension = len(values) # TODO: See note on APLScalar
        self.rank = 1
        self.depth = 1
    # TODO: methods

# TODO: type checking
class APLScalar(APLArray):
    # TODO: additional types (e.g. complex numbers, maybe even objects in general (i.e. Python types)?
    def __init__(self,value):
        if not (isinstance(value,int) or
                isinstance(value,float) or
                isinstance(value,function) or
                (isinstance(value,str) and len(value)==1)):
            raise TypeError
        self.value = np.array(value)
        self.dimension = [0,0] # TODO: Methods returning these three as proper APLObjects
        self.rank = 0
        self.depth = 0
    # TODO: methods

class APLZilde(np.ndarray):
    def __new__(cls):
        return super.__new__(cls,(0,))

    def __array_finalize__(self,obj):
        if obj is None: return

    def __repr__(self):
        return '⍬'

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
