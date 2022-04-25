from sly import Parser
from lex import APLLex

class APLParse(Parser):
    # Get the token list from the lexer (required)
    tokens = APLLex.tokens

    # Grammar rules and actions
    # TODO: Replace example string actions with actual meaningful actions
    @_('expr dyad expr')
    def expr(self, p):
        return("p.dyad("+str(p.expr0)+", "+str(p.expr1+")")

    @_('monad expr')
    def expr(self, p):
        return("p.monad("+str(p.expr)+")")

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return(str(p.expr))

    @_('array')
    def expr(self, p):
        return(str(p.array))

    @_('array array')
    def array(self, p):
        return(str(p.array0)+" + "+str(p.array1))

    @_('scalar array')
    def array(self, p):
        return(str(p.scalar)+" + "+str(p.array))

    @_('array scalar')
    def array(self, p):
        return(str(p.array)+" + "+str(p.scalar))

    @_('scalar scalar')
    def array(self, p):
        return(str(p.scalar0)+" + "+str(p.scalar1))

    @_('scalar')
    def array(self, p):
        return("arrayify("+str(p.scalar)+")" # TODO: implement arrayify)

    @_('NUMBER')
    def scalar(self, p):
        return(str(p.NUMBER))

    @_('CHAR')
    def scalar(self, p):
        return(str(p.CHAR))

    @_('expr PLUS expr') # example dyadic function for now
    def expr(self, p):
        return(str(p.expr0)+" + "str(p.expr1))

    @_('MINUS expr') # example monadic function for now
    def expr(self, p):
        return("-"+str(p.expr))

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
