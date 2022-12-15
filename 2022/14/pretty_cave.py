def pretty_cave(cave):
    max_x = 0
    max_y = 0
    for x, y in cave.keys():
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    print(max_x)
    print(max_y)

    for y in range(max_y):
        for x in range(max_x):
            print(cave.get((x, y), "."), end="")

        print()