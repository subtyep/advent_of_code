

def run():
    file = open("input.txt", "r")
    instructions = file.read().splitlines()

    score = 0
    for counter, i in enumerate(range(0, len(instructions), 3), 1):

        left = eval(instructions[i])
        right = eval(instructions[i+1])

        if in_right_order(left, right):
            score += counter

    print("score", score)


def in_right_order(left, right) -> bool:

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        if left == right:
            return None
        if left > right:
            return False

    if isinstance(left, list) and isinstance(right, list):
        for i in range(len(left)):
            if left and not right:
                return False
            elif not left and right:
                return True

            list_check = in_right_order(left.pop(0), right.pop(0))

            if list_check in [True, False]:
                return list_check

        if len(left) == len(right):
            return None

    elif isinstance(left, list) and isinstance(right, int):
        return in_right_order(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
        return in_right_order([left], right)

    return True


if __name__ == '__main__':
    run()


