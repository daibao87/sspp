# py2c_transpiler/emitter.py
def emit_c_code(code, filename):
    with open(filename, "w") as f:
        f.write(code)
