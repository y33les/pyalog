from sly import Lexer

class APLLex(Lexer):
    # Set of token names.   This is always required

    tokens = { ID,LPAREN,RPAREN,LBRACK,RBRACK,LBRACE,RBRACE,SPACE,PFUNC,LEFT,EACH,SELFIE,REPEAT,DOT,JOT,ATOP,OVER,AT,QUOTEQUAD,QUAD,QUADCOL,KEY,STENCIL,IBEAM,DIAMOND,LAMP,RIGHT,DBLOMEGA,DBLALPHA,OMEGA,ALPHA,DEL,AMP,OBAR,ZILDE,DELTA,DELTASUB, CHAR, NUMBER }

    # String containing ignored characters between tokens
    ignore = ' \t'
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
    ID      = r'[a-zA-Z_][a-zA-Z0-9_]+'
    LPAREN  = r'\('
    RPAREN  = r'\)'
    LBRACK = r'\['
    RBRACK = r'\]'
    LBRACE = r'\{'
    RBRACE = r'\}'
    SPACE = r'\ '
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

    @_(r'\d*\.?\d+')
    def NUMBER(self,t):
        if "." in t.value:
            t.value = float(t.value)
        else:
            t.value = int(t.value)
        return t
        # TODO: implement 0x, 0b, E notation, complex numbers, floats without integer parts (e.g .3)
        # TODO: arrayify

    @_(r'\'.\'')
    def CHAR(self,t):
        t.value=t.value[1:-1]
        return t
    # TODO: arrayify

    @_(r'\'((\\\')|[^\'(\\\')])+\'')
    def STRING(self,t):
        t.value=t.value[1:-1]
        return t
    # TODO: arrayify into array of CHARs

if __name__ == '__main__':
    data = 'x = 3 + 42 * (s - t)'
    numbers = '3 4.0 .5 12.34 12.3 3.45 4 3J4'
    strings = "foo 'bar' baz 'quux' xyzzy 'a' 'b'"
    life = 'life ← {⊃1 ⍵ ∨.∧ 3 4 = +/ +⌿ ¯1 0 1 ∘.⊖ ¯1 0 1 ⌽¨ ⊂⍵} ⍝ GOL in APL'
    l = APLLex()
    for t in l.tokenize(strings):
        print('type=%r, value=%r' % (t.type, t.value))
