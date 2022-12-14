import functools

def run():
    file = open("input.txt", "r")
    instructions = file.read().splitlines()

    signals = [[[2]], [[6]]]
    for counter, i in enumerate(range(0, len(instructions), 3), 1):

        signals.append(eval(instructions[i]))
        signals.append(eval(instructions[i+1]))

    signals = sorted(signals, key=functools.cmp_to_key(in_right_order))

    for i, row in enumerate(signals, 1):
        if row == [[2]] or row == [[6]]:
            print(i)


def in_right_order(left, right) -> int:
    if isinstance(left, int) and isinstance(right, int):
        return (left > right) - (left < right)

    if isinstance(left, list) and isinstance(right, list):
        for list_check in map(in_right_order, left, right):
            if list_check != 0:
                return list_check

        return in_right_order(len(left), len(right))

    elif isinstance(left, list) and isinstance(right, int):
        return in_right_order(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
        return in_right_order([left], right)


if __name__ == '__main__':
    run()


