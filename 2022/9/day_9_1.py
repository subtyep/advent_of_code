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


def run():
    file = open("input.txt", "r")
    commands = file.read().splitlines()

    head = Point(0, 0)
    tail = Point(0, 0)

    locations_visited = set()

    def log_move(tail_spot):
        locations_visited.add((tail_spot.x, tail_spot.y))

    log_move(tail)

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

            x_diff = head.x - tail.x
            y_diff = head.y - tail.y

            if x_diff == 2 and y_diff == 0:
                tail.x += 1
            elif x_diff == -2 and y_diff == 0:
                tail.x -= 1
            elif x_diff == 0 and y_diff == 2:
                tail.y += 1
            elif x_diff == 0 and y_diff == -2:
                tail.y -= 1

            elif (x_diff == -2 and y_diff == 1) or (x_diff == -1 and y_diff == 2):
                tail.x -= 1
                tail.y += 1
            elif (x_diff == 1 and y_diff == 2) or (x_diff == 2 and y_diff == 1):
                tail.x += 1
                tail.y += 1
            elif (x_diff == 2 and y_diff == -1) or (x_diff == 1 and y_diff == -2):
                tail.x += 1
                tail.y -= 1
            elif (x_diff == -1 and y_diff == -2) or (x_diff == -2 and y_diff == -1):
                tail.x -= 1
                tail.y -= 1

            log_move(tail)

    print("count_locations_visited", len(locations_visited))


if __name__ == '__main__':
    run()


