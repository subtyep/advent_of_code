value = 1
values = {}
for letter in "abcdefghijklmnopqrstuvwxyz":
    values[letter] = value
    values[letter.upper()] = value + 26
    value += 1


def run(input_file: str):
    file = open(input_file, "r")

    print(sum(calculate_scores(file.readlines())))


def calculate_scores(lines):
    group = []
    for line in lines:
        group.append(line.strip())

        if len(group) != 3:
            continue

        (in_common, ) = set.intersection(
            set(group.pop()),
            set(group.pop()),
            set(group.pop())
        )

        yield values.get(in_common)


if __name__ == '__main__':
    run("simple_scenario.txt")


