from pretty_cave import pretty_cave

def run():
    cave, min_elevation = create_grid()

    num_sand_fallen = simulate_sand(cave, min_elevation + 1)
    print(num_sand_fallen)

    # pretty_cave(cave)


def simulate_sand(cave, min_elevation):
    counter = 0
    while True:
        sx = 500
        sy = 0

        if cave.get((sx, sy)):
            return counter

        while True:
            if sy == min_elevation:
                cave[(sx, sy)] = "o"
                break
            if not cave.get((sx, sy + 1)):
                sy += 1
            elif not cave.get((sx - 1, sy + 1)):
                sx -= 1
                sy += 1
            elif not cave.get((sx + 1, sy + 1)):
                sx += 1
                sy += 1
            else:
                cave[(sx, sy)] = "o"
                break

        counter += 1


def create_grid():
    file = open("input.txt", "r")

    cave = {}
    min_elevation = 0

    for scanline in file.read().splitlines():
        points = scanline.split(" -> ")

        for i in range(1, len(points)):
            left = extract_points(points[i-1])
            right = extract_points(points[i])

            cave[left] = "#"
            cave[right] = "#"

            lx, ly = left
            rx, ry = right

            min_elevation = max(min_elevation, ly, ry)

            if lx == rx:
                for ny in range(ly, ry, (ly < ry) - (ly > ry)):
                    cave[(lx, ny)] = "#"

            if ly == ry:
                for nx in range(lx, rx, (lx < rx) - (lx > rx)):
                    cave[(nx, ly)] = "#"

    return cave, min_elevation


def extract_points(point):
    x, y = point.split(",")
    return int(x), int(y)


if __name__ == '__main__':
    run()


