L = 0
D = 3
W = 6

R = 1
P = 2
S = 3

permutations = {
    ("A", "X"): S + L, ("A", "Y"): R + D, ("A", "Z"): P + W,
    ("B", "X"): R + L, ("B", "Y"): P + D, ("B", "Z"): S + W,
    ("C", "X"): P + L, ("C", "Y"): S + D, ("C", "Z"): R + W,
}

def run(input_file: str):
    file = open(input_file, "r")

    points = []

    for line in file.readlines():
        line = line.strip()
        round = line.split(" ")
        points.append(permutations.get((round[0], round[1])))

    print('total_score', sum(points))


if __name__ == '__main__':
    run("input.txt")


