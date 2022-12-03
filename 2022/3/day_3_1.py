

def run(input_file: str):
    file = open(input_file, "r")

    value = 1
    values = {}
    for letter in "abcdefghijklmnopqrstuvwxyz":
        values[letter] = value
        values[letter.upper()] = value + 26
        value += 1

    scores = []

    for line in file.readlines():
        line = line.strip()

        item1 = set(line[: len(line) // 2])
        item2 = set(line[len(line)//2:])

        (in_common, ) = item1.intersection(item2)

        scores.append(values.get(in_common))

    print(sum(scores))


if __name__ == '__main__':
    run("input.txt")


