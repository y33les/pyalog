from sly import Lexer

class APLLex(Lexer):
    # Set of token names.   This is always required

    tokens = { ID, NUMBER, LPAREN, RPAREN, LBRACK, RBRACK, LBRACE,
               RBRACE, SPACE, LEFT, PLUS, MINUS, TIMES, DIVIDE, POWER,
               LOG, MDIV, CIRC, BANG, QUESTION, PIPE, CEIL, FLOOR,
               TACKUP, TACKDN, LTACK, RTACK, EQ, NEQ, LTEQ, LT, GT,
               GTEQ, MATCH, TALLY, OR, AND, NAND, NOR, UP, DOWN,
               ENCLOSE, DISCLOSE, NEST, SQUAD, GRADEUP, GRADEDN, IOTA,
               WHERE, ENLIST, FIND, UNION, INTERSECTION, TILDE,
               FSLASH, BSLASH, FSLASH1, BSLASH1, COMMA, CATENATE, RHO,
               ROTATE, ROTATE1, TRANSPOSE, EACH, SELFIE, REPEAT, DOT,
               JOT, ATOP, OVER, AT, QUOTEQUAD, QUAD, QUADCOL, KEY,
               STENCIL, IBEAM, EXEC, FORMAT, SEP, LAMP, RIGHT, OMEGA,
               ALPHA, DEL, AMP, OBAR, ZILDE, DELTA, DELTASUB }

    # String containing ignored characters between tokens
    ignore = ' \t'

    # Regular expression rules for tokens
    ID      = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER  = r'\d+'
    LPAREN  = r'\('
    RPAREN  = r'\)'
    LBRACK = r'\['
    RBRACK = r'\]'
    LBRACE = r'\{'
    RBRACE = r'\}'
    SPACE = r' '

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
    LTACK = r'⊣'
    RTACK = r'⊢'
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
    ENCLOSE = r'⊂'
    DISCLOSE = r'⊃'
    NEST = r'⊆'
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
    SEP = r'⋄'
    LAMP = r'⍝'
    RIGHT = r'→'
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
    life = 'life ← {⊃1 ⍵ ∨.∧ 3 4 = +/ +⌿ ¯1 0 1 ∘.⊖ ¯1 0 1 ⌽¨ ⊂⍵}'
    l = APLLex()
    for t in l.tokenize(life):
        print('type=%r, value=%r' % (t.type, t.value))
