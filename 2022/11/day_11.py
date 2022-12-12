import math


class Monkey:

    def __init__(self, num) -> None:
        super().__init__()
        self.num = num
        self.items = []
        self.true_monkey = None
        self.false_monkey = None
        self.operation = None
        self.divisible_num = None

        self.items_inspected = 0

    def throw_all_the_shit(self):
        op = self.operation[4]
        multiplier = self.operation[6:]

        while self.items:
            item = self.items.pop(0)
            self.items_inspected += 1

            if op == "*":
                if multiplier == "old":
                    item = item * item
                else:
                    item = item * int(multiplier)
            elif op == "+":
                if multiplier == "old":
                    item = item + item
                else:
                    item = item + int(multiplier)

            # lose interest
            # item = item // 3

            # test
            if item % self.divisible_num == 0:
                self.true_monkey.items.append(item)
            else:
                self.false_monkey.items.append(item)

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"{self.num}: {str(self.items)} T: {self.true_monkey.num} F: {self.false_monkey.num}"


def run(rounds):
    monkeys = initialize_state()

    divisions = [m.divisible_num for m in monkeys]

    lcm = math.lcm(*divisions)
    print(lcm)

    for round_counter in range(rounds):
        print(f"Round {round_counter}")
        for monkey in monkeys:
            monkey.throw_all_the_shit()

        # check for items over lcm
        for monkey in monkeys:
            monkey.items = [item % lcm for item in monkey.items]

        print(f"After Round {round_counter}")
        for monkey in monkeys:
            print(f"Monkey {monkey.num}: {monkey.items}")

    for monkey in monkeys:
        print(f"Monkey {monkey.num} inspected {monkey.items_inspected} items")

    inspections = sorted([m.items_inspected for m in monkeys], reverse=True)
    print(inspections)
    print(inspections[0] * inspections[1])


def initialize_state():
    file = open("input.txt", "r")
    instructions = file.read().splitlines()
    num_monkeys = int((len(instructions) + 1) / 7)

    monkeys = [Monkey(i) for i in range(num_monkeys)]

    for x, input in enumerate(range(1, len(instructions), 7)):
        cur_monkey = monkeys[x]

        cur_monkey.items = [int(i) for i in instructions[input].split(":")[1].split(",")]
        cur_monkey.operation = instructions[input + 1][19:]
        cur_monkey.divisible_num = int(instructions[input + 2][21:])
        cur_monkey.true_monkey = monkeys[int(instructions[input + 3][-1])]
        cur_monkey.false_monkey = monkeys[int(instructions[input + 4][-1])]

    return monkeys


if __name__ == '__main__':
    run(10000)


