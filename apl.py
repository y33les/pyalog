# APL builtin functions, *M=>monadic, *D=>dyadic

# TODO: implement pyspark versions?
import numpy as np


lookup = {
    '+': 'aplPlus',
    '!': 'aplBang'
}

class APLException(Exception):
    pass

# +
def aplPlus(*args):
    if len(args)==0:
        print("+nilad!")
    elif len(args)==1:
        print("+monad!")
    elif len(args)==2:
        print("+dyad!")
    else:
        raise APLException

# -×÷|⌊⌈*⍟!○~?∧∨⍲⍱<≤=≥>≠⍴,⍪⌽⊖⍉↑↓⊂⊆∊⊃/⌿\\⍀∩∪⊣⊢⍳⍸⍒⍋⍷≡≢⍎⍕⊥⊤⌹⌷
