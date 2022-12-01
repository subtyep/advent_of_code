
def run():
    file = open("2022/1/calorie_input.txt", "r")

    current_calories = 0
    calories = []

    for line in file.readlines():
        line = line.strip()

        if line != "":
            current_calories += int(line)
        else:
            calories.append(current_calories)
            current_calories = 0

    calories.sort(reverse=True)

    print('max', calories[0])
    print('top_three', sum(calories[:3]))


if __name__ == '__main__':
    run()


