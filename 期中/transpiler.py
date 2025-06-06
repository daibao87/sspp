# py2c_transpiler/transpiler.py
def transpile(node):
    def visit(n):
        if isinstance(n, int):
            return str(n)
        elif hasattr(n, 'value'):
            return str(n.value)
        elif hasattr(n, 'op'):
            return f"({visit(n.left)} {n.op} {visit(n.right)})"
    return f"#include <stdio.h>\n\nint main() {{\n    printf(\"%d\\n\", {visit(node)});\n    return 0;\n}}\n"
