L = 0
D = 3
W = 6

R = 1
P = 2
S = 3

permutations = {
    ("A", "X"): R + D, ("A", "Y"): P + W, ("A", "Z"): S + L,
    ("B", "X"): R + L, ("B", "Y"): P + D, ("B", "Z"): S + W,
    ("C", "X"): R + W, ("C", "Y"): P + L, ("C", "Z"): S + D,
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


