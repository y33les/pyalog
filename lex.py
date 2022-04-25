from sly import Lexer

class APLLex(Lexer):
    # Set of token names.   This is always required

    tokens = { ID, NUMBER, LPAREN, RPAREN, LBRACK, RBRACK, LBRACE,
               RBRACE, SPACE, LEFT, PLUS, MINUS, TIMES, DIVIDE, POWER,
               LOG, MDIV, CIRC, BANG, QUESTION, PIPE, CEIL, FLOOR,
               TACKUP, TACKDN, TACKL, TACKR, EQ, NEQ, LTEQ, LT, GT,
               GTEQ, MATCH, TALLY, OR, AND, NAND, NOR, UP, DOWN,
               LSHOE, RSHOE, LSHOESUB, SQUAD, GRADEUP, GRADEDN, IOTA,
               WHERE, ENLIST, FIND, UNION, INTERSECTION, TILDE,
               FSLASH, BSLASH, FSLASH1, BSLASH1, COMMA, CATENATE, RHO,
               ROTATE, ROTATE1, TRANSPOSE, EACH, SELFIE, REPEAT, DOT,
               JOT, ATOP, OVER, AT, QUOTEQUAD, QUAD, QUADCOL, KEY,
               STENCIL, IBEAM, EXEC, FORMAT, DIAMOND, LAMP, RIGHT, OMEGA,
               ALPHA, DEL, AMP, OBAR, ZILDE, DELTA, DELTASUB,
               DBLALPHA, DBLOMEGA }

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

    # APL symbols (Dyalog style)
    LEFT = r'←'
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'×'
    DIVIDE = r'÷'
    POWER = r'\*'
    LOG = r'⍟'
    MDIV = r'⌹'
    CIRC = r'○'
    BANG = r'!'
    QUESTION = r'\?'
    PIPE = r'\|'
    CEIL = r'⌈'
    FLOOR = r'⌊'
    TACKUP = r'⊥'
    TACKDN = r'⊤'
    TACKL = r'⊣'
    TACKR = r'⊢'
    EQ = r'='
    NEQ = r'≠'
    LTEQ = r'≤'
    LT = r'<'
    GT = r'>'
    GTEQ = r'≥'
    MATCH = r'≡'
    TALLY = r'≢'
    OR = r'∨'
    AND = r'∧'
    NAND = r'⍲'
    NOR = r'⍱'
    UP = r'↑'
    DOWN = r'↓'
    LSHOE = r'⊂'
    RSHOE = r'⊃'
    LSHOESUB = r'⊆'
    SQUAD = r'⌷'
    GRADEUP = r'⍋'
    GRADEDN = r'⍒'
    IOTA = r'⍳'
    WHERE = r'⍸'
    ENLIST = r'∊'
    FIND = r'⍷'
    UNION = r'∪'
    INTERSECTION = r'∩'
    TILDE = r'~'
    FSLASH = r'/'
    BSLASH = r'\\'
    FSLASH1 = r'⌿'
    BSLASH1 = r'⍀'
    COMMA = r','
    CATENATE = r'⍪'
    RHO = r'⍴'
    ROTATE = r'⌽'
    ROTATE1 = r'⊖'
    TRANSPOSE = r'⍉'
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
    EXEC = r'⍎'
    FORMAT = r'⍕'
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

if __name__ == '__main__':
    data = 'x = 3 + 42 * (s - t)'
    numbers = '3 4.0 .5 12.34 12.3 3.45 4 3J4'
    life = 'life ← {⊃1 ⍵ ∨.∧ 3 4 = +/ +⌿ ¯1 0 1 ∘.⊖ ¯1 0 1 ⌽¨ ⊂⍵} ⍝ GOL in APL'
    l = APLLex()
    for t in l.tokenize(numbers):
        print('type=%r, value=%r' % (t.type, t.value))
