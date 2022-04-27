from sly import Parser
from lex import APLLex
from aplarrays import *

class APLParse(Parser):
    # Get the token list from the lexer (required)
    tokens = APLLex.tokens

    # Grammar rules and actions
    precedence = (('right',)+tuple(tokens),)

    """
    # TODO: Replace example string actions with actual meaningful actions
    @_('expr PLUS expr') # dyad
    def expr(self, p):
        return ("p.dyad("+str(p.expr0)+", "+str(p.expr1)+")")

    @_('MINUS expr') # monad
    def expr(self, p):
        return ("p.monad("+str(p.expr)+")")

    @_('expr expr')
    def array(self, p):
        return APLArray(p.expr0, p.expr1)

    @_('expr')
    def expr(self, p):
        return p.expr

    @_('array')
    def expr(self, p):
        return p.array

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return APLArray('E') # (str(p.expr))

    @_('LPAREN array RPAREN')
    def array(self, p):
        return APLArray(p.array) # TODO: if this is the whole line of input, it shouldn't enclose (cf. tryapl.org)

    @_('array array')
    def array(self, p):
        return APLArray(p.array0,p.array1) # Does this give [[1,2],[3,4]] or [1,2,3,4]?  TODO: Which do we want?

    @_('scalar array')
    def array(self, p):
        return APLArray(p.scalar,p.array)

    @_('array scalar')
    def array(self, p):
        return APLArray(p.array,p.scalar) # Does this give [[1,2],3] or [1,2,3]?  TODO: Which do we want?

    @_('scalar scalar')
    def array(self, p):
        return APLArray(p.scalar0, p.scalar1) # np.concatenate((p.array0,p.array1))

    @_('NUMBER')
    def scalar(self, p):
        return APLArray(p.NUMBER)

    @_('CHAR')
    def scalar(self, p):
        if p.CHAR=='q':
            exit(0)
        else:
            return APLArray(p.CHAR)
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

    @_('array array')
    def array(self, p):
        return np.concatenate((p.array0,p.array1))

    @_('value')
    def array(self,p):
        if isinstance(p.value,np.ndarray):
            return p.value # TODO: Does this need to be enclosed in another APLArray?
        else:
            return np.array([p.value])

    @_('LPAREN expr RPAREN')
    def value(self, p):
        return p.expr

    @_('NUMBER')
    def value(self, p):
        return p.NUMBER

    @_('CHAR')
    def value(self, p):
        if p.CHAR=='q':
            exit(0)
        else:
            return p.CHAR

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
