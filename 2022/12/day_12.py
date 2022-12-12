
v = {char: i for i, char in enumerate("SabcdefghijklmnopqrstuvwxyzE")}
v["-"] = 99

def run():
    file = open("input.txt", "r")

    grid = []

    for i, row in enumerate(file.read().splitlines()):
        grid.append([tile for tile in row])

    grid.insert(0, ["-" for _ in range(len(grid[0]))])
    grid.append(["-" for _ in range(len(grid[0]))])

    for row in grid:
        row.insert(0, "-")
        row.append("-")

    positions = find_start_positions(grid)
    visited = set(positions)

    # start steps at -1 to account for "stepping into" the first spot
    steps = -1
    found = False
    while positions and not found:
        count = len(positions)

        steps += 1

        for _ in range(count):
            p = positions.pop(0)

            x = p[0]
            y = p[1]

            if grid[x][y] == "E":
                print("found it!")
                found = True
                break

            cur_val = v.get(grid[x][y], 100)

            pos = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
            pos = [p for p in pos if p not in visited]

            for k, j in pos:
                cell = grid[k][j]

                if v[cell] <= cur_val + 1:
                    positions.append((k, j))
                    visited.add((k, j))

    print("shortest", steps)


def find_start_positions(grid):
    starts = []

    for k, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell in ["S", "a"]:
                starts.append((k, j))

    return starts


if __name__ == '__main__':
    run()


