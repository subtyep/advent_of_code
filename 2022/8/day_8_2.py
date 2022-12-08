
def run():
    trees = parse_trees()

    high_score = 0

    for x in range(len(trees)):
        for y in range(len(trees[x])):
            high_score = max(calculate_score(x, y, trees), high_score)

    print("high_score:", high_score)


def calculate_score(x, y, trees):
    tree = trees[x][y]

    to_check = [
        list(reversed(trees[x][:y])),  # up
        trees[x][y + 1:],  # down
        list(reversed([trees[i][y] for i in range(x)])),  # left
        [trees[i][y] for i in range(x + 1, len(trees))]  # right
    ]

    score = 1

    for row in to_check:
        count = 0
        for row_tree in row:
            count += 1

            if row_tree >= tree:
                break

        score = score * count

    return score


def parse_trees():
    file = open("input.txt", "r")

    tree_grid = []
    for x, row in enumerate(file.read().splitlines()):
        for y, tree in enumerate(row):
            if x == 0:
                tree_grid.append([])

            tree_grid[y].append(tree)

    return tree_grid


if __name__ == '__main__':
    run()


