import string


class Token:
    def __init__(self, type, value, **kwargs):
        self.type = type
        self.value = value
        self.kwargs = kwargs
        self.__dict__.update(self.kwargs)

    def __repr__(self):
        return f"Token({self.type} {self.value} {self.kwargs})"


# Types
T_INST = "INSTRUCTION"
T_INT = "INTEGER"
T_PROGADDR = "PROGRAM ADDRESS"

# Associated characters with type
D_INT = "0123456789"
D_INST = string.ascii_uppercase
D_IGNOREDCHARS = [' ', ',', '\n']

D_PROGADDR = "&"

D_SPECIAL_CHARACTERS = {
    D_PROGADDR: T_PROGADDR,
}
