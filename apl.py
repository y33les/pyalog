import math
import numpy as np
# TODO: implement pyspark versions?

class APLException(Exception):
    pass

class APLArgumentException(Exception):
    args=("==> You've passed wrong arguments somehow <==",)

    def __init__(self,args="==> You've passed wrong arguments somehow <=="):
        super().__init__(args)
        self.args=("==> You've passed wrong arguments somehow <==",)

class NYI(Exception):
    pass

lookup = {
    '+': 'aplPlus',
    '-': 'aplMinus',
    '×': 'aplTimes',
    '÷': 'aplDivide',
    '|': 'aplPipe',
    '⌈': 'aplFloor',
    '⌈': 'aplCeil',
    '*': 'aplExp'
    # *⍟!○~?∧∨⍲⍱<≤=≥>≠⍴,⍪⌽⊖⍉↑↓⊂⊆∊⊃/⌿\\⍀∩∪⊣⊢⍳⍸⍒⍋⍷≡≢⍎⍕⊥⊤⌹⌷
}

# TODO: Do nilads exist in Dyalog?  Or should it just return the function itself?`
#       Decided that they don't; remember that a function can be partially implemented and its args updated in the ast.Call object

######################################################################
# TODO: !!!! Check numpy.* for already-implemented array-friendly maths functions !!!!
######################################################################

# TODO: Note that outer product is already implemented by numpy (numpy.ufunc.outer)

# +
def aplPlus(*args):
    """
    Monadic +:\tconjugate
    Dyadic +:\tadd
    """
    if len(args)==0:
        return aplPlus
    elif len(args)==1: # Monadic
        if isinstance(args[0],complex):
            return(complex(args[0].real,-args[0].imag))
        else:
            return args[0]
    elif len(args)==2: # Dyadic
        return args[0]+args[1]
    else:
        raise APLArgumentException

# -
def aplMinus(*args):
    """
    Monadic -:\tnegate
    Dyadic -:\tsubtract
    """
    if len(args)==0:
        return aplMinus
    elif len(args)==1: # Monadic
        return -args[0]
    elif len(args)==2: # Dyadic
        return args[0]-args[1]
    else:
        raise APLArgumentException

# ×
def aplTimes(*args):
    """
    Monadic ×:\tsign
    Dyadic ×:\tmultiply
    """
    if len(args)==0:
        return aplTimes
    elif len(args)==1: # Monadic
        if args[0]>0:
            return 1
        elif args[0]<0:
            return -1
        elif args[0]==0:
            return 0
        else:
            raise APLArgumentException
    elif len(args)==2: # Dyadic
        return args[0]*args[1]
    else:
        raise APLArgumentException

# ÷
def aplDivide(*args):
    """
    Monadic ÷:\treciprocal
    Dyadic ÷:\tdivide
    """
    if len(args)==0:
        return aplDivide
    elif len(args)==1: # Monadic
        return 1/args[0]
    elif len(args)==2: # Dyadic
        return args[0]/args[1]
    else:
        raise APLArgumentException

# |
def aplPipe(*args):
    """
    Monadic:\tmagnitude
    Dyadic:\tmodulus
    """
    if len(args)==0:
        return aplPipe
    elif len(args)==1: # Monadic
        return abs(args[0])
    elif len(args)==2: # Dyadic
        return args[1]%args[0] # Note the wacky APL order
    else:
        raise APLArgumentException

# ⌊
def aplFloor(*args):
    """
    Monadic:\tfloor
    Dyadic:\tminimum
    """
    if len(args)==0:
        return aplFloor
    elif len(args)==1: # Monadic
        return math.floor(args[0])
    elif len(args)==2: # Dyadic
        return min(args[0],args[1])
    else:
        raise APLArgumentException

# ⌈
def aplCeil(*args):
    """
    Monadic:\tceiling
    Dyadic:\tmaximum
    """
    if len(args)==0:
        return aplCeil
    elif len(args)==1: # Monadic
        return math.ceil(args[0])
    elif len(args)==2: # Dyadic
        return max(args[0],args[1])
    else:
        raise APLArgumentException


# *
def aplExp(*args):
    """
    Monadic:\te^x
    Dyadic:\tpower
    """
    if len(args)==0:
        return aplExp
    elif len(args)==1: # Monadic
        return math.e^args[0]
    elif len(args)==2: # Dyadic
        return args[0]^args[1]
    else:
        raise APLArgumentException

# ⍟!○~?∧∨⍲⍱<≤=≥>≠⍴,⍪⌽⊖⍉↑↓⊂⊆∊⊃/⌿\\⍀∩∪⊣⊢⍳⍸⍒⍋⍷≡≢⍎⍕⊥⊤⌹⌷
