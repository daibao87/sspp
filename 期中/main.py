# py2c_transpiler/main.py
from lexer import tokenize
from parser import parse
from transpiler import transpile
from emitter import emit_c_code

import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python main.py <input.py>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "output/hello.c"

    with open(input_file, "r") as f:
        source = f.read()

    tokens = tokenize(source)
    ast = parse(tokens)
    c_code = transpile(ast)
    emit_c_code(c_code, output_file)

    print(f"轉譯完成，輸出檔案: {output_file}")
