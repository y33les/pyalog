import math, cmath, arrayops as a
import numpy as np
from random import randint, shuffle, sample
# TODO: implement pyspark versions?

class APLException(Exception):
    pass

class APLArgumentException(APLException):
    args=("==> You've passed wrong arguments somehow <==",)

    def __init__(self,args="==> You've passed wrong arguments somehow <=="):
        super().__init__(args)
        self.args=("==> You've passed wrong arguments somehow <==",)

class APLDomainError(APLException):
    pass

class NYI(APLException):
    pass

lookup = {
    '+': 'aplPlus',
    '-': 'aplMinus',
    '×': 'aplTimes',
    '÷': 'aplDivide',
    '|': 'aplPipe',
    '⌊': 'aplFloor',
    '⌈': 'aplCeil',
    '*': 'aplExp',
    '⍟': 'aplLog',
    '!': 'aplBang',
    '○': 'aplCirc',
    '~': 'aplTilde',
    '?': 'aplQuestion',
    '∧': 'aplAnd',
    '∨': 'aplOr'
    #⍲⍱<≤=≥>≠⍴,⍪⌽⊖⍉↑↓⊂⊆∊⊃/⌿\\⍀∩∪⊣⊢⍳⍸⍒⍋⍷≡≢⍎⍕⊥⊤⌹⌷
}

# TODO: Do nilads exist in Dyalog?  Or should it just return the function itself?`
#       Decided that they don't; remember that a function can be partially implemented and its args updated in the ast.Call object

######################################################################
# TODO: !!!! Check numpy.* for already-implemented array-friendly maths functions !!!!
#            Update: there are so many, TODO: implement (see https://numpy.org/doc/stable/reference/routines.math.html)
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
        return math.exp(args[0]) # TODO: Do we need math.expm1 for small x?
    elif len(args)==2: # Dyadic
        if isinstance(args[1],float):
            return math.pow(args[0],args[1]) # More accurate for non-integer exponents, apparently
        else:
            return args[0]**args[1]
    else:
        raise APLArgumentException

# ⍟
def aplLog(*args):
    """
    Monadic:\tln
    Dyadic:\tlog
    """
    if len(args)==0:
        return aplLog
    elif len(args)==1: # Monadic
        return math.log(args[0])
    elif len(args)==2: # Dyadic
        if args[0]==2:
            return math.log2(args[1]) # More accurate than math.log(x,2), apparently
        elif args[0]==10:
            return math.log10(args[1]) # More accurate than math.log(x,10), apparently
        else:
            return math.log(args[1],args[0]) # Note the wacky APL order
    else:
        raise APLArgumentException

#!
def aplBang(*args):
    """
    Monadic:\tfactorial
    Dyadic:\tbinomial
    """
    if len(args)==0:
        return aplBang
    elif len(args)==1: # Monadic
        return math.factorial(args[0])
    elif len(args)==2: # Dyadic
        return math.comb(args[1],args[0]) # Note the wacky APL order
    else:
        raise APLArgumentException

#○
def aplCirc(*args):
    """
    Monadic:\tπ times
    Dyadic:\tcircular

    Circular function:

      Trigonometric functions:
        ⍺ =  0\t⍺○⍵ = sqrt(1-⍵²)
        ⍺ =  1\t⍺○⍵ = sin ⍵\t\t-⍺○⍵ = arcsin ⍵
        ⍺ =  2\t⍺○⍵ = cos ⍵\t\t-⍺○⍵ = arccos ⍵
        ⍺ =  3\t⍺○⍵ = tan ⍵\t\t-⍺○⍵ = arctan ⍵
        ⍺ =  4\t⍺○⍵ = sqrt(1+⍵²)\t-⍺○⍵ = sqrt(⍵²-1)
        ⍺ =  5\t⍺○⍵ = sinh ⍵\t\t-⍺○⍵ = arcsinh ⍵
        ⍺ =  6\t⍺○⍵ = cosh ⍵\t\t-⍺○⍵ = arccosh ⍵
        ⍺ =  7\t⍺○⍵ = tanh ⍵\t\t-⍺○⍵ = arctanh ⍵

      Functions on complex numbers:
        ⍺ =  8\t⍺○⍵ = sqrt(¯1-⍵²)\t-⍺○⍵ = -sqrt(¯1-⍵²)
        ⍺ =  9\t⍺○⍵ = real(⍵)\t\t-⍺○⍵ = ⍵
        ⍺ = 10\t⍺○⍵ = |⍵\t\t-⍺○⍵ = +⍵
        ⍺ = 11\t⍺○⍵ = imag(⍵)\t\t-⍺○⍵ = i×⍵
        ⍺ = 12\t⍺○⍵ = phase(⍵)\t\t-⍺○⍵ = e^(i×⍵)
    """
    if len(args)==0:
        return aplCirc
    elif len(args)==1: # Monadic
        return math.pi*args[0]
    elif len(args)==2: # Dyadic
        fs=[[(lambda x: cmath.sqrt(1-math.pow(args[1],2)))],
            [cmath.sin,cmath.asin],
            [cmath.cos,cmath.acos],
            [cmath.tan,cmath.atan],
            [(lambda x: cmath.sqrt(1+math.pow(args[1],2))),(lambda x: cmath.sqrt(math.pow(args[1],2)-1))],
            [cmath.sinh,cmath.asinh],
            [cmath.cosh,cmath.acosh],
            [cmath.tanh,cmath.atanh],
            [(lambda x: cmath.sqrt(-1-math.pow(args[1],2))),(lambda x: -cmath.sqrt(-1-math.pow(args[1],2)))],
            [(lambda x: x.real),(lambda x: x)],
            [(lambda x: aplPipe(x)),(lambda x: aplPlus(x))],
            [(lambda x: x.imag),(lambda x: x*complex(0,1))],
            [(lambda x: cmath.atan(x.imag/x.real) if x.real!=0 else aplTimes(x.imag)*cmath.pi/2),(lambda x: complex(cmath.cos(x),cmath.sin(x)))]]
        return fs[abs(args[0])][args[0]<0](args[1])
    else:
        raise APLArgumentException

def _aplCircTest(x):
    for i in range(0,13):
        print(str(i)+":",end="\t")
        print(aplCirc(i,x),end="\t")
        print(str(-i)+":",end="\t")
        print(aplCirc(-i,x))

#~
def aplTilde(*args):
    """
    Monadic:\tnot
    Dyadic:\twithout
    """
    if len(args)==0:
        return aplTilde
    elif len(args)==1: # Monadic
        if args[0]==1:
            return 0
        elif args[0]==0:
            return 1
        else:
            raise APLDomainError
    elif len(args)==2: # Dyadic
        return a.toAPLArray([e for e in args[0] if e not in args[1]])
    else:
        raise APLArgumentException

#### POINT AT WHICH I REALISED ABOUT ALL THE NUMPY MATHS FUNCTIONS ####
# TODO: Correct above methods

#?
def aplQuestion(*args):
    """
    Monadic:\troll
    Dyadic:\tdeal
    """
    if len(args)==0:
        return aplQuestion
    elif len(args)==1:
        return randint(0,args[0]-1) # TODO: Check this (Dyalog is 1-indexed)
    elif len(args)==2:
        if(args[1]<args[0]):
            raise APLDomainError
        else:
            l=list(range(0,args[1])) # TODO: Check this (Dyalog is 1-indexed)
            if args[1]==None: # TODO: Check this (Dyalog can do ?⍨⍵ (i.e. ⍺?) to do a random permutation of ⍳⍺ (see APL Wiki))
                # FIXME: It doesn't seem to like taking None as an argument
                shuffle(l)
                return a.toAPLArray(l)
            else:
                return a.toAPLArray(sample(l,args[0]))
    else:
        raise APLArgumentException

#∧
def aplAnd(*args):
    """
    (Dyadic only)
    Dyadic: LCM/and
    """
    if len(args)==0:
        return aplAnd
    elif len(args)==2: # Dyadic only
        return np.lcm(args[0],args[1])
    else:
        raise APLArgumentException

#∨
def aplOr(*args):
    """
    (Dyadic only)
    Dyadic: GCD/and
    """
    if len(args)==0:
        return aplOr
    elif len(args)==2: # Dyadic only
        return np.gcd(args[0],args[1])
    else:
        raise APLArgumentException

#⍲⍱<≤=≥>≠⍴,⍪⌽⊖⍉↑↓⊂⊆∊⊃/⌿\\⍀∩∪⊣⊢⍳⍸⍒⍋⍷≡≢⍎⍕⊥⊤⌹⌷
