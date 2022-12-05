import re

def run(input_file: str):
    (cargo, moves) = parse_cargo_and_moves(input_file)
    stacked_cargo = create_cargo_stacks(cargo)
    move_cargo(stacked_cargo, moves)

    top_cargo = ""

    for cargo_stack in stacked_cargo:

        if cargo_stack:
            top_cargo += cargo_stack[-1]

    print(top_cargo)


def parse_cargo_and_moves(input_file):
    cargo = []
    moves = []

    add_cargo = True

    file = open(input_file, "r")
    for line in file.readlines():
        if not line.strip():
            add_cargo = False
            continue

        if add_cargo:
            cargo.append(line)
        else:
            moves.append(line.strip())

    return (cargo, moves)


def create_cargo_stacks(cargo):
    stacks = cargo.pop()
    stack_indexes = stacks.strip().replace("   ", ",").split(",")

    stacked_cargo = []
    stacked_cargo.append([]) #empty first stack to account for 1 based counting
    cargo_slots = {}

    for i in stack_indexes:
        cargo_slots[int(i)] = stacks.index(i)
        stacked_cargo.append([])

    stack_indexes = [int(i) for i in stack_indexes]

    for row in reversed(cargo):
        for i in stack_indexes:
            value = row[cargo_slots[i]]

            if value != " ":
                stacked_cargo[int(i)].append(value)

    return stacked_cargo


def move_cargo(stacked_cargo, moves):
    r = re.compile(r"move (?P<quantity>\d*) from (?P<stack1>\d*) to (?P<stack2>\d*)")

    for move in moves:
        m = r.search(move)
        quantity = int(m["quantity"])
        stack1 = int(m["stack1"])
        stack2 = int(m["stack2"])

        move_stack = []

        for _ in range(quantity):
            cargo = stacked_cargo[stack1].pop()
            move_stack.insert(0, cargo)

        stacked_cargo[stack2].extend(move_stack)


if __name__ == '__main__':
    run("input.txt")


