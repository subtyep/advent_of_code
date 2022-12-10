UP = "U"
DOWN = "D"
LEFT = "L"
RIGHT = "R"

class Point:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def move_towards(self, other: 'Point'):

        x_diff = other.x - self.x
        y_diff = other.y - self.y

        if abs(x_diff) <= 1 and abs(y_diff) <= 1:
            return

        if x_diff < 0:
            self.x -= 1
        elif x_diff > 0:
            self.x += 1

        if y_diff < 0:
            self.y -= 1
        elif y_diff > 0:
            self.y += 1


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

            for i in range(1, len(knots)):
                knots[i].move_towards(knots[i-1])

            save_tail_location()

    print("count_locations_visited", len(locations_visited))  #2793


if __name__ == '__main__':
    run()


