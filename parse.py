import numpy as np
import operator as op
import ast
from astor import to_source
from sly import Parser
from lex import APLLex
from arrayops import isAtomic

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
        return(ast.Call(ast.Name(id='testfunc',ctx=ast.Load()),[p.node0,p.node1],keywords=[]))

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
def testeval(e):
    print(eval(compile(p.parse(l.tokenize(e)),filename="<ast>",mode="eval")))

if __name__ == '__main__':
    l = APLLex()
    p = APLParse()

    while True:
        try:
            text = input('apl > ')
            result = t.visit(p.parse(l.tokenize(text)))
            print(to_source(result))
            #print(eval(compile(result, filename="<ast>", mode="eval")))
            #print(result)
        except EOFError:
            break
