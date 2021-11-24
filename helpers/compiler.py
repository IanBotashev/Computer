def main():
    file = input("File to compile: ")
    lines = open(file, 'r').readlines()
    result_lines = ['v2.0 raw']
    for line in lines:
        result = handle_line(line)
        if type(result) == str:
            result_lines.append(hex(int(result, 2))[2:])
        else:
            for item in result:
                result_lines.append(hex(int(item, 2))[2:])

    with open('../hexfiles/program.hex', 'w') as f:
        f.write("\n".join(result_lines))
    print(result_lines)
    print("Finished!")


def handle_line(line):
    parts = line.strip().lower().split(' ')
    print(parts)

    if parts[0] == 'nop':
        return "0b0"

    elif parts[0] == 'lda':
        return f"0b{format(int(parts[1]), '010b')}000001"

    elif parts[0] == 'sta':
        return f"0b{format(int(parts[1]), '010b')}000010"

    elif parts[0] == 'lla':
        return [f"0b000011", f"{bin(int(parts[1]))}"]

    elif parts[0] == 'ldb':
        return f"0b{format(int(parts[1]), '010b')}000100"

    elif parts[0] == 'stb':
        return f"0b{format(int(parts[1]), '010b')}000101"

    elif parts[0] == 'llb':
        return [f"0b000110", f"{bin(int(parts[1]))}"]

    elif parts[0] == 'hlt':
        return str(bin(7))

    elif parts[0] == 'add':
        return f"0b{format(int(parts[1]), '010b')}001000"

    elif parts[0] == 'sub':
        return f"0b{format(int(parts[1]), '010b')}001001"

    elif parts[0] == 'mul':
        return f"0b{format(int(parts[1]), '010b')}001010"

    elif parts[0] == 'sli':
        return [f"0b{format(int(parts[1]), '010b')}001011", f"{bin(int(parts[2]))}"]

    elif parts[0] == 'jmp':
        return f"0b{format(int(parts[1])-1, '010b')}001100"

    elif parts[0] == 'out':
        return str(bin(13))

    else:
        raise Exception(f"Unrecognized instruction {parts[0]}")


if __name__ == "__main__":
    main()