def run(input_file: str):
    file = open(input_file, "r")

    contained_assignments = 0
    overlapped_assignments = 0

    for line in file.readlines():
        (first, second) = line.strip().split(",")
        first = first.split("-")
        second = second.split("-")

        first_assignment = SectionAssignment(int(first[0]), int(first[1]))
        second_assignment = SectionAssignment(int(second[0]), int(second[1]))

        contains = first_assignment.fully_contains(second_assignment) or second_assignment.fully_contains(first_assignment)
        overlaps = first_assignment.overlaps(second_assignment) or second_assignment.overlaps(first_assignment)

        if contains:
            contained_assignments += 1

        if overlaps:
            overlapped_assignments += 1

    print(contained_assignments, overlapped_assignments)


class SectionAssignment:

    def __init__(self, section_start: int, section_stop: int) -> None:
        super().__init__()

        self.section_start = section_start
        self.section_stop = section_stop

    def __str__(self) -> str:
        return f"({self.section_start}-{self.section_stop})"

    def fully_contains(self, other: 'SectionAssignment') -> bool:
        """
        Returns true if other is fully contained within this section assignment
        """

        start_within = self.section_start <= other.section_start <= self.section_stop
        end_within = self.section_start <= other.section_stop <= self.section_stop

        return start_within and end_within

    def overlaps(self, other: 'SectionAssignment') -> bool:
        """
        Returns true if any part of the two assignments overlaps
        """

        start_within = self.section_start <= other.section_start <= self.section_stop
        end_within = self.section_start <= other.section_stop <= self.section_stop

        return start_within or end_within


if __name__ == '__main__':
    run("input.txt")


