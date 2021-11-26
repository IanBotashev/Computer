from helpers.compiler import *
from helpers.compiler.errors import IllegalCharacter, IllegalArgumentType


class Tokenizer:
    def __init__(self):
        self.pos = 0
        self.results = []
        self.text = ""

    def tokenize(self, text):
        self.pos = 0
        self.results = []
        self.text = text

        while self.pos < len(self.text):
            result = self.handle_char(self.text[self.pos])
            if result is not None:
                self.results.append(result)
            self.pos += 1

        self.parse()
        return self.results

    def parse(self):
        """
        Last step in tokenization. Put tokens together.
        For example, a program address token and an integer token will be put together into one program address token.
        :return:
        """
        pos = 0
        while pos < len(self.results):
            token = self.results[pos]
            if token.type == T_PROGADDR:
                next_token = self.results[pos+1]
                if next_token.type == T_INT:
                    self.results[pos] = Token(T_PROGADDR, next_token.value)
                    self.results.remove(next_token)
                else:
                    raise IllegalArgumentType(f"Type {next_token.type} is not a valid target for a program address.")

            pos += 1

    def handle_char(self, char):
        if char in D_INST:
            end_pos, result = get_full_type(self.pos, self.text, D_INST)
            self.pos = end_pos
            return Token(T_INST, result)

        elif char in D_INT:
            end_pos, result = get_full_type(self.pos, self.text, D_INT)
            self.pos = end_pos
            return Token(T_INT, int(result))

        elif char in D_SPECIAL_CHARACTERS:
            return Token(D_SPECIAL_CHARACTERS[char], char)

        elif char in D_IGNOREDCHARS:
            pass

        else:
            raise IllegalCharacter(f"Illegal character '{char}' at position {self.pos}")


def get_full_type(pos, line, characters):
    """
    Get the full type from a specific datatype from a line. Returns the string, and the end pos.
    :param pos:
    :param line:
    :param characters:
    :return:
    """
    end_pos = pos + 1

    while end_pos < len(line):
        if line[end_pos] not in characters:
            break
        else:
            end_pos += 1

    return end_pos-1, line[pos:end_pos]


if __name__ == "__main__":
    tknzer = Tokenizer()
    cmd = "SLI 105, &0 STA &1"
    print(tknzer.tokenize(cmd))
