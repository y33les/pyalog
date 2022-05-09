from sly import Lexer

class APLLex(Lexer):
    # Set of token names.   This is always required

    tokens = { ID,LPAREN,RPAREN,LBRACK,RBRACK,LBRACE,RBRACE,SPACE,PFUNC,LEFT,EACH,SELFIE,REPEAT,DOT,JOT,ATOP,OVER,AT,QUOTEQUAD,QUAD,QUADCOL,KEY,STENCIL,IBEAM,DIAMOND,LAMP,RIGHT,DBLOMEGA,DBLALPHA,OMEGA,ALPHA,DEL,AMP,OBAR,ZILDE,DELTA,DELTASUB,CHAR,NUMBER }

    # String containing ignored characters between tokens
    ignore = ''
    ignore_comment = r'⍝.*$'

    ## Compute line no.
    #@_(r'\n+')
    #def ignore_newline(self, t):
    #    self.lineno += len(t.value)

    ## Compute col no.
    #def find_column(text, token):
    #    last_cr = text.rfind('\n', 0, token.index)
    #    if last_cr < 0:
    #        last_cr = 0
    #    column = (token.index - last_cr) + 1
    #    return column

    # TODO: Implement error handling

    # Regular expression rules for tokens

    @_(r'(m)?\d*\.?\d+(J(m)?\d*\.?\d+)?')  # FIXME: m replaces overbar for ease of testing
    def NUMBER(self,t):
        t.value = t.value.replace('m','-') # FIXME: m replaces overbar for ease of testing
        if 'J' in t.value:
            t.value = t.value.split('J')
            for i in range(len(t.value)):
                if "." in t.value[i]:
                    t.value[i] = float(t.value[i])
                else:
                    t.value[i] = int(t.value[i])
            t.value = complex(t.value[0],t.value[1])
        elif '.' in t.value:
            t.value = float(t.value)
        else:
            t.value = int(t.value)
        return t
        # TODO: implement 0x, 0b, E notation - are these already handled by python anyway?

    @_(r'\'.\'')
    def CHAR(self,t):
        t.value=t.value[1:-1]
        return t

    @_(r'\'((\\\')|[^\'(\\\')])+\'')
    def STRING(self,t):
        t.value=t.value[1:-1]
        return t
    # TODO: arrayify into array of CHARs

    ID      = r'[a-zA-Z_][a-zA-Z0-9_]+'
    LPAREN  = r'\('
    RPAREN  = r'\)'
    LBRACK = r'\['
    RBRACK = r'\]'
    LBRACE = r'\{'
    RBRACE = r'\}'
    SPACE = r'[\ \t]+'
    # TODO: implement characters and strings ("/')

    # APL primitive functions
    PFUNC = r'[+\-×÷|⌊⌈*⍟!○~?∧∨⍲⍱<≤=≥>≠⍴,⍪⌽⊖⍉↑↓⊂⊆∊⊃/⌿\\⍀∩∪⊣⊢⍳⍸⍒⍋⍷≡≢⍎⍕⊥⊤⌹⌷]'

    # APL primitive operators
    # TODO

    # APL symbols (Dyalog style)
    LEFT = r'←'
    EACH = r'¨'
    SELFIE = r'⍨'
    REPEAT = r'⍣'
    DOT = r'\.'
    JOT = r'∘'
    ATOP = r'⍤'
    OVER = r'⍥'
    AT = r'@'
    QUOTEQUAD = r'⍞'
    QUAD = r'⎕'
    QUADCOL = r'⍠'
    KEY = r'⌸'
    STENCIL = r'⌺'
    IBEAM = r'⌶'
    DIAMOND = r'[⋄\n]' # newline equivalent to statement separator, cf. rodrigogiraoserrao/RGSPL
    LAMP = r'⍝'
    RIGHT = r'→'
    DBLOMEGA = r'⍵⍵'
    DBLALPHA = r'⍺⍺'
    OMEGA = r'⍵'
    ALPHA = r'⍺'
    DEL = r'∇'
    AMP = r'&'
    OBAR = r'¯'
    ZILDE = r'⍬'
    DELTA = r'∆'
    DELTASUB = r'⍙'

if __name__ == '__main__':
    data = 'x = 3 + 42 * (s - t)'
    numbers = '3 4.0 .5 12.34 12.3 3.45 4 3J4'
    strings = "foo 'bar' baz 'quux' xyzzy 'a' 'b'"
    life = 'life ← {⊃1 ⍵ ∨.∧ 3 4 = +/ +⌿ ¯1 0 1 ∘.⊖ ¯1 0 1 ⌽¨ ⊂⍵} ⍝ GOL in APL'
    l = APLLex()
    for t in l.tokenize(strings):
        print('type=%r, value=%r' % (t.type, t.value))
