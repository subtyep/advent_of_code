
def run():
    file = open("input.txt", "r")
    instructions = file.read().splitlines()

    cycles = [1, 1]

    for instruction in instructions:
        current_value = cycles[-1]
        
        if instruction == "noop":
            cycles.append(current_value)
        else:
            _, amount = instruction.split()

            cycles.append(current_value)
            cycles.append(current_value + int(amount))

    strength = 0

    for i in range(20, 221, 40):
        strength += i * cycles[i]

    print("signal_strength", strength)

    position = 0
    for i in range(1, 241):
        x_value = cycles[i]

        if x_value - 1 <= position <= x_value + 1:
            print("#", end="")
        else:
            print(".", end="")

        position += 1

        if i % 40 == 0:
            position = 0
            print()

    print() #PBZGRAZA


if __name__ == '__main__':
    run()


