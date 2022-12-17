import re

regex = re.compile(r"Sensor at x=(?P<sx>-?\d*), y=(?P<sy>-?\d*): closest beacon is at x=(?P<bx>-?\d*), y=(?P<by>-?\d*)")

def run():
    file = open("input.txt", "r")

    sensors = {}
    beacons = set()

    min_x = 100_000_000
    max_x = -100_000_000

    for i, scanline in enumerate(file.read().splitlines(), 1):
        r = regex.search(scanline)

        sx = int(r["sx"])
        sy = int(r["sy"])
        bx = int(r["bx"])
        by = int(r["by"])

        distance_to_sensor = abs(sx - bx) + abs(sy - by)
        sensors[(sx, sy)] = distance_to_sensor
        beacons.add((bx, by))

        min_x = min(min_x, sx - distance_to_sensor)
        max_x = max(max_x, sx + distance_to_sensor)

    no_go_spots = 0

    y = 2_000_000
    for x in range(min_x, max_x + 1):
        print("x", x)
        if (x, y) in beacons:
            continue

        for sensor, d in sensors.items():
            sx, sy = sensor
            distance_to_sensor = abs(x - sx) + abs(y - sy)

            if distance_to_sensor <= d:
                no_go_spots += 1
                break

    print(no_go_spots)


if __name__ == '__main__':
    run()


