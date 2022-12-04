def run(input_file: str):
    file = open(input_file, "r")

    contained_assignments = 0
    overlapped_assignments = 0

    for line in file.readlines():
        (first, second) = line.strip().split(",")
        (first_start, first_stop) = first.split("-")
        (second_start, second_stop) = second.split("-")

        first_assignment = SectionAssignment(int(first_start), int(first_stop))
        second_assignment = SectionAssignment(int(second_start), int(second_stop))

        if first_assignment.fully_contains(second_assignment):
            contained_assignments += 1

        if first_assignment.overlaps(second_assignment):
            overlapped_assignments += 1

    print(contained_assignments, overlapped_assignments)


class SectionAssignment:

    def __init__(self, section_start: int, section_stop: int) -> None:
        super().__init__()

        self.assignment = set(range(section_start, section_stop + 1))

    def fully_contains(self, other: 'SectionAssignment') -> bool:
        """
        Returns true if either assignment is fully contained within the other
        """
        overlap_count = len(self.assignment & other.assignment)
        return overlap_count == len(other.assignment) or overlap_count == len(self.assignment)

    def overlaps(self, other: 'SectionAssignment') -> bool:
        """
        Returns true if any part of the two assignments overlaps
        """
        return len(self.assignment & other.assignment) > 0


if __name__ == '__main__':
    run("input.txt")


