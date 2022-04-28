import numpy as np
import operator as op
import ast
from astor import to_source
from sly import Parser
from lex import APLLex
from arrayops import isAtomic

def passfunc(x=0,y=0): # FIXME: Replace this with something proper inside APL*ad
    pass

class APLNilad(ast.operator):
    f = ast.Name(id='passfunc',ctx='load')

    def __init__(self,f):
        self.f = ast.Name(id=f,ctx='load')
        super().__init__()

class APLMonad(ast.operator):
    f = ast.Name(id='passfunc',ctx='load')

    def __init__(self,f):
        self.f = ast.Name(id=f,ctx='load')
        super().__init__()

class APLDyad(ast.operator):
    f = ast.Name(id='passfunc',ctx='load')

    def __init__(self,f):
        self.f = ast.Name(id=f,ctx='load')
        super().__init__()

#class _APLTransformer(ast.NodeTransformer):
class APLTransformer(ast.NodeTransformer):
    def visit_APLDyad(self,node):
        self.generic_visit(node)
        return node

    def visit_BinOp(self,node):
        self.generic_visit(node)
        if isinstance(node.op,APLDyad):
            if isinstance(node.op.f,ast.Name): # Call
                return(ast.Call(node.op.f,[node.left,node.right]))
            elif isinstance(node.op.f,ast.Lambda): # Lambda
                raise Exception("lambdas not yet implemented") # TODO
            # TODO: dfn?
            else:
                raise TypeError("your dyad doesn't have a name or a lambda as its op")

class APLParse(Parser):
    # Get the token list from the lexer (required)
    tokens = APLLex.tokens

    # Grammar rules and actions
    precedence = (('right',)+tuple(tokens),)

    @_('node')
    def expr(self,p):
        return ast.fix_missing_locations(ast.Expression(p.node)) # TODO: A proper lineno fix would be nice

    @_('MINUS node')
    def node(self, p):
        return ast.UnaryOp(ast.USub(),p.node)

    @_('node PLUS node')
    def node(self, p):
        return ast.BinOp(p.node0,ast.Add(),p.node1)

    @_('node COMMA node')
    def node(self, p):
        return ast.BinOp(p.node0,APLDyad('testfunc'),p.node1)

    # TODO: nilads

    # TODO: strings

    #@_('node node')
    #def node(self, p):

    @_('NUMBER')
    def node(self, p):
        return ast.Constant(p.NUMBER)

    @_('CHAR')
    def node(self, p):
        if p.CHAR=='q':
            exit(0)
        else:
            return ast.Constant(p.CHAR)

# Test stuff # TODO: remove
x=ast.Constant(2)
y=ast.Constant(3)
a=ast.BinOp(x,ast.Add(),y)
b=ast.BinOp(x,APLDyad('testfunc'),y)
l=APLLex()
p=APLParse()
t=APLTransformer()
def testfunc(x,y):
    return x-y
def testparse(e):
    print(to_source(p.parse(l.tokenize(e))))

if __name__ == '__main__':
    l = APLLex()
    p = APLParse()

    while True:
        try:
            text = input('apl > ')
            result = p.parse(l.tokenize(text))
            print(to_source(result))
            #print(eval(compile(result, filename="<ast>", mode="eval")))
            #print(result)
        except EOFError:
            break
