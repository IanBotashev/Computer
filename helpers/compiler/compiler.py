from helpers.compiler.errors import InvalidInstruction
from helpers.compiler.tokenizer import Tokenizer
from helpers.compiler import *
from helpers.compiler.errors import *


compile_map = {
    "LDA": {"bin": ["{0[0]}000001"], "offset": 0, "arguments_num": 1},
    "STA": {"bin": ["{0[0]}000010"], "offset": 0, "arguments_num": 1},
    "LLA": {"bin": ["000011", "{0[0]}"], "offset": 1, "arguments_num": 1},
    "LDB": {"bin": ["{0[0]}000100"], "offset": 0, "arguments_num": 1},
    "STB": {"bin": ["{0[0]}000101"], "offset": 0, "arguments_num": 1},
    "LLB": {"bin": ["000110", "{0[0]}"], "offset": 1, "arguments_num": 1},
    "HLT": {"bin": ["000111"], "offset": 0, "arguments_num": 0},
    "ADD": {"bin": ["{0[0]}001000"], "offset": 0, "arguments_num": 1},
    "SUB": {"bin": ["{0[0]}001001"], "offset": 0, "arguments_num": 1},
    "MUL": {"bin": ["{0[0]}001010"], "offset": 0, "arguments_num": 1},
    "SLI": {"bin": ["{0[0]}001011", "{0[1]}"], "offset": 1, "arguments_num": 2},
    "JMP": {"bin": ["{0[0]}001100"], "offset": 0, "arguments_num": 1},
    "OUT": {"bin": ["001101"], "offset": 0, "arguments_num": 0},
    "JEZ": {"bin": ["{0[0]}001110"], "offset": 0, "arguments_num": 1},
}
"""
Offset defines the amount that program addresses will have to offset their value after this instruction
This is done, because certain instructions like SLI take up multiple program addresses, and we need to account for that.
It's either true or false.

arguments_num is just the amount of arguments. Also used to know how many position we need to shift over to find the next
instruction.
"""


class Compiler:
    def __init__(self):
        """
        pos:        The current position in tokens we're checking
        tokens:     The tokens to compile
        results:    The results
        offset_map: Offset map to allow for program addresses to account for
        """
        self.pos = 0
        self.tokens = []
        self.results = []
        self.offset_map = {}

    def compile(self, tokens):
        self.pos = 0
        self.tokens = tokens
        self.results = []
        self.offset_map = {}

        while self.pos < len(self.tokens):
            result = self.handle_instruction(self.tokens[self.pos])
            for item in result:
                self.results.append(item)
            self.pos += 1

        return self.results

    def handle_instruction(self, token):
        if token.value in compile_map:
            data = compile_map[token.value]

            # Get arguments
            args = []
            for x in range(1, data["arguments_num"]+1):
                token = self.tokens[self.pos + x]
                if token.type == T_PROGADDR:
                    args.append(bin(self.handle_program_address(token)))
                else:
                    args.append(bin(token.value))

            # Offset check
            if data["offset"] > 0:
                print(f"Added offset of {data['offset']} after address {self.pos}")
                self.offset_map.update({self.pos: data["offset"]})

            # Position change
            self.pos += data["arguments_num"]

            # Compiling
            result = []
            for item in data["bin"]:
                result.append(hex(int(item.format(args), 2)))
            return result

        else:
            raise InvalidInstruction(f"Unrecognized Instruction {token.value}")

    def handle_program_address(self, token):
        """
        Get proper program address
        :param token:
        :return:
        """
        result = token.value

        if token.value > 0:
            for offset in self.offset_map:
                if offset < self.pos:
                    result += self.offset_map[offset]
        else:
            result = 1

        return result-1



if __name__ == "__main__":
    tokenizer = Tokenizer()
    compiler = Compiler()
    cmd = "LLA 1 LDA &2 HLT"
    tokens = tokenizer.tokenize(cmd)
    print(compiler.compile(tokens))
