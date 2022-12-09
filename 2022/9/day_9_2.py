UP = "U"
DOWN = "D"
LEFT = "L"
RIGHT = "R"


class Point:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x},{self.y})"

    def __repr__(self) -> str:
        return str(self)


def run():
    file = open("input.txt", "r")
    commands = file.read().splitlines()

    knots = [Point(0, 0) for _ in range(10)]
    head = knots[0]
    tail = knots[-1]

    locations_visited = set()

    def save_tail_location():
        locations_visited.add((tail.x, tail.y))

    for command in commands:
        move, length = command.split(" ")

        for _ in range(int(length)):
            if move == UP:
                head.y += 1
            elif move == DOWN:
                head.y -= 1
            elif move == RIGHT:
                head.x += 1
            elif move == LEFT:
                head.x -= 1

            for i in range(len(knots) - 1):
                move_knot(knots[i], knots[i+1])

            save_tail_location()

    print("count_locations_visited", len(locations_visited))


def move_knot(lead_knot: Point, follow_knot: Point) -> None:
    x_diff = lead_knot.x - follow_knot.x
    y_diff = lead_knot.y - follow_knot.y

    if x_diff == 2 and y_diff == 0:
        follow_knot.x += 1
    elif x_diff == -2 and y_diff == 0:
        follow_knot.x -= 1
    elif x_diff == 0 and y_diff == 2:
        follow_knot.y += 1
    elif x_diff == 0 and y_diff == -2:
        follow_knot.y -= 1

    elif (x_diff == -2 and y_diff == 1) or (x_diff == -1 and y_diff == 2) or (x_diff == -2 and y_diff == 2):
        follow_knot.x -= 1
        follow_knot.y += 1
    elif (x_diff == 1 and y_diff == 2) or (x_diff == 2 and y_diff == 1) or (x_diff == 2 and y_diff == 2):
        follow_knot.x += 1
        follow_knot.y += 1
    elif (x_diff == 2 and y_diff == -1) or (x_diff == 1 and y_diff == -2) or (x_diff == 2 and y_diff == -2):
        follow_knot.x += 1
        follow_knot.y -= 1
    elif (x_diff == -1 and y_diff == -2) or (x_diff == -2 and y_diff == -1) or (x_diff == -2 and y_diff == -2):
        follow_knot.x -= 1
        follow_knot.y -= 1


if __name__ == '__main__':
    run()


