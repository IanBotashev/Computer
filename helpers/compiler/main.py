from helpers.compiler.compiler import Compiler
from helpers.compiler.tokenizer import Tokenizer

header = "v2.0 raw"


def main(file):
    print(f" - Compiling {file}...")
    f = open(file, 'r')
    raw = f.read()
    compiler = Compiler()
    tokenizer = Tokenizer()

    tokens = tokenizer.tokenize(raw)
    print(f" - Successfully tokenized. Compiling...")
    compiled = compiler.compile(tokens)
    print(f" - Successfully compiled. Writing to program.hex in hexfiles...")
    compiled.insert(0, header)

    with open('../../hexfiles/program.hex', 'w') as f:
        f.write("\n".join(compiled))

    print("----Success! Compiled program can be found in hexfiles/program.hex----")


if __name__ == "__main__":
    print("Leave blank to compile code.asm")
    file = input("File to compile: ")

    if file == '':
        file = 'code.asm'

    main(file)
