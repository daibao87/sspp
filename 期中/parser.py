# py2c_transpiler/parser.py
class Number:
    def __init__(self, value):
        self.value = value

class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

def parse(tokens):
    tokens = tokens[::-1]

    def consume():
        return tokens.pop()

    def parse_expr():
        left = parse_term()
        while tokens and tokens[-1][0] == 'OP':
            op = consume()[1]
            right = parse_term()
            left = BinOp(left, op, right)
        return left

    def parse_term():
        tok = consume()
        if tok[0] == 'NUMBER':
            return Number(tok[1])
        elif tok[0] == 'LPAREN':
            expr = parse_expr()
            consume()  # RPAREN
            return expr

    return parse_expr()
