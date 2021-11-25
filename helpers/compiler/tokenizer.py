from helpers.compiler import Token, T_INT, T_INST, D_INST, D_INT


class Tokenizer:
    def __init__(self):
        self.pos = 0
        self.results = []
        self.line = ""

    def tokenize(self, line):
        self.pos = 0
        self.results = []
        self.line = line

        while self.pos < len(line):
            result = self.handle_char(line[self.pos])
            if result is not None:
                self.results.append(result)
            self.pos += 1

        return self.results


    def handle_char(self, char):
        if char in D_INST:
            end_pos, result = get_full_type(self.pos, self.line, D_INST)
            self.pos = end_pos
            return Token(T_INST, result)


def get_full_type(pos, line, characters):
    end_pos = pos + 1

    while pos < len(line):
        if line[end_pos] not in characters:
            return end_pos, line[pos:end_pos]
        else:
            end_pos += 1

    return end_pos


if __name__ == "__main__":
    tknzer = Tokenizer()
    print(tknzer.tokenize("TEST "))