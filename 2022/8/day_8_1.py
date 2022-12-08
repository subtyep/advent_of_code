
def run():
    trees = parse_trees()

    visible_count = 0

    for x in range(len(trees)):
        for y in range(len(trees[x])):
            if is_visible(x, y, trees):
                visible_count += 1

    print("visible_count:", visible_count)


def is_visible(x, y, trees):
    # First row and column
    if x == 0 or y == 0:
        return True

    # Last row and column
    if x == len(trees) - 1 or y == len(trees[x]) - 1:
        return True

    tree = trees[x][y]

    # above
    if max(trees[x][:y]) < tree:
        return True

    # below
    if max(trees[x][y+1:]) < tree:
        return True

    # left
    if max([trees[i][y] for i in range(x)]) < tree:
        return True

    # right
    if max([trees[i][y] for i in range(x+1, len(trees))]) < tree:
        return True

    return False


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


