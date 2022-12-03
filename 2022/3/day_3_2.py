

def run(input_file: str):
    file = open(input_file, "r")

    value = 1
    values = {}
    for letter in "abcdefghijklmnopqrstuvwxyz":
        values[letter] = value
        values[letter.upper()] = value + 26
        value += 1

    scores = []

    group = []
    for line in file.readlines():
        group.append(line.strip())

        if len(group) != 3:
            continue

        (in_common, ) = set.intersection(
            set(group[0]),
            set(group[1]),
            set(group[2])
        )

        group = []

        scores.append(values.get(in_common))

    print(sum(scores))


if __name__ == '__main__':
    run("input.txt")


