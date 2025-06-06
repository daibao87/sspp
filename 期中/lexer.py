# py2c_transpiler/lexer.py
def tokenize(source):
    import re
    token_spec = [
        ('NUMBER',   r'\d+'),
        ('ID',       r'[a-zA-Z_]\w*'),
        ('ASSIGN',   r'='),
        ('OP',       r'[+\-*/]'),
        ('LPAREN',   r'\('),
        ('RPAREN',   r'\)'),
        ('NEWLINE',  r'\n'),
        ('SKIP',     r'[ \t]+'),
        ('MISMATCH', r'.'),
    ]
    tok_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in token_spec)
    tokens = []
    for mo in re.finditer(tok_regex, source):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NUMBER': value = int(value)
        if kind != 'SKIP' and kind != 'MISMATCH':
            tokens.append((kind, value))
    return tokens
