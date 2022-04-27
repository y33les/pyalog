import numpy as np
from sly import Parser
from lex import APLLex
from arrayops import isAtomic

class Node:
    f=None
    l=None
    r=None

    def __init__(self,f,l=None,r=None):
        self.f=f
        self.l=l
        self.r=r

    def show(self):
        if self.l==None:
            if self.r==None:
                return(str(self.f))
            else:
                return("  "+str(self.f)+"  \n"+"   \\ \n"+"    "+self.r.show())
        else:
            return("  "+str(self.f)+"  \n"+" / \\ \n"+self.l.show()+"   "+self.r.show())

class Leaf:
    val=None

    def __init__(self,val):
        self.val=val

    def show(self):
        return(str(self.val))

class APLParse(Parser):
    # Get the token list from the lexer (required)
    tokens = APLLex.tokens

    # Grammar rules and actions
    precedence = (('right',)+tuple(tokens),)

    """
    @_('expr PLUS expr') # TODO: This may end up needing an APLExpr class, or maybe an AST node
    def expr(self, p):
        return p.expr0 + p.expr1

    @_('MINUS expr')
    def expr(self, p):
        return -p.expr

    @_('array')
    def expr(self, p):
        return p.array

    @_('array COMMA array')
    def array(self, p):
        return np.asarray(list(map(lambda x: np.asarray(x),np.asarray([list(p.array0),list(p.array1)],dtype=object))),dtype=object)

    @_('value')
    def array(self,p):
        #if isinstance(p.value,np.ndarray):
        #    return p.value # TODO: Does this need to be enclosed in another APLArray?
        #else:
        #    return np.array([p.value],dtype=object)
        return np.array([p.value],dtype=object)

    @_('LPAREN expr RPAREN')
    def value(self, p):
        return np.array(list(p.expr),dtype=object)
    """


    @_('node')
    def expr(self,p):
        p.node.show()
        return p.node

    @_('MINUS node')
    def node(self, p):
        return Node('m',l=Leaf('X'),r=p.value)

    @_('node PLUS node')
    def node(self, p):
        return Node('d',l=p.value0,r=p.value1)

    # TODO: nilads

    @_('NUMBER')
    def node(self, p):
        return Node(p.NUMBER)

    @_('CHAR')
    def node(self, p):
        if p.CHAR=='q':
            exit(0)
        else:
            return Node(p.CHAR)

if __name__ == '__main__':
    l = APLLex()
    p = APLParse()

    while True:
        try:
            text = input('apl > ')
            result = p.parse(l.tokenize(text))
            print(result)
        except EOFError:
            break
