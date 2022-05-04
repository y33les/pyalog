import numpy as np
import operator as op
import ast
from astor import to_source
from sly import Parser
from lex import APLLex
from arrayops import isAtomic

def exprWrap(n):
    return ast.Expression(n) # TODO: A proper lineno fix would be nice

def callWrap(f,a):
    return ast.Call(ast.Name(id=f,ctx=ast.Load()),a,keywords=[]) # TODO: A proper lineno fix would be nice

def encapsulate(n):
    return n

lookup = { # TODO: Move this to a more appropriate module
    'a': 'aplPlus',
    'b': 'aplMinus'
}

class APLException(Exception):
    pass

def aplPlus(*args):
    if len(args)==0:
        print("+nilad!")
    elif len(args)==1:
        print("+monad!")
    elif len(args)==2:
        print("+dyad!")
    else:
        raise APLException

def aplMinus(*args):
    if len(args)==0:
        print("-nilad!")
    elif len(args)==1:
        print("-monad!")
    elif len(args)==2:
        print("-dyad!")
    else:
        raise APLException

class APLParse(Parser):
    # Get the token list from the lexer (required)
    tokens = APLLex.tokens

    # Grammar rules and actions
    precedence = (('right',)+tuple(tokens),)

    @_('expr DIAMOND') # FIXME: Temporary hack to help me wrap my head around this - can probably do this with ^ actually, thinking about it (may need to modify the lexer) - or even with \n$ actually probably makes more sense, if we can get the precedence right (last)
    def root(self,p):
        return ast.fix_missing_locations(exprWrap(p.expr)) # The lineno fix should be in the root node only, and this should also be the only ast.Expression (the lineno fix fails for nested ast.Expressions)

    @_('LPAREN expr RPAREN')
    def expr(self,p):
        return callWrap('encapsulate',[p.expr])

    @_('const')
    def expr(self,p):
        return p.const

    # Can we work out valence by delaying execution or using a transformer?
    # Can we work out valence with some kind of partial Call (like a projection in K)?

    #@_('COMMA expr') # Monadic comma
    #def expr(self, p):
    #    return callWrap('testmonad',[p.expr])
    #
    #@_('expr COMMA expr') # Dyadic comma
    #def expr(self, p):
    #    return callWrap('testdyad',[p.expr0,p.expr1])

    @_('FUNC') # Nilad
    def expr(self, p):
        print(p.FUNC)
        return callWrap(lookup.get(p.FUNC),[])

    @_('FUNC expr') # Monad
    def expr(self, p):
        return callWrap(lookup.get(p.FUNC),[p.expr])

    @_('expr FUNC expr') # Dyad
    def expr(self, p):
        return callWrap(lookup.get(p.FUNC),[p.expr0,p.expr1])

    # TODO: nilads

    # TODO: strings

    #@_('const const')
    #def const(self, p):

    @_('NUMBER')
    def const(self, p):
        return ast.Constant(p.NUMBER)

    @_('CHAR')
    def const(self, p):
        if p.CHAR=='q':
            exit(0)
        else:
            return ast.Constant(p.CHAR)

# Test stuff # TODO: remove
l=APLLex()
p=APLParse()
def testnilad():
    return 2
def testmonad(x):
    return x+1
def testdyad(x,y):
    return x-y
def testparse(e):
    return p.parse(l.tokenize(e))
def testcompile(n):
    return eval(compile(n,filename="<ast>",mode="eval"))
def testsource(e):
    print(to_source(p.parse(l.tokenize(e))))
def testeval(e):
    print(eval(compile(p.parse(l.tokenize(e)),filename="<ast>",mode="eval")))

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
