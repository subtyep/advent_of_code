import unittest

from day_13_2 import in_right_order

class Tester(unittest.TestCase):

    def test_pair_1(self):
        self.assertEquals(-1, in_right_order([1,1,3,1,1], [1,1,5,1,1]))

    def test_pair_2(self):
        self.assertEquals(-1, in_right_order([[1],[2,3,4]], [[1],4]))

    def test_pair_3(self):
        self.assertFalse(0, in_right_order([9], [[8,7,6]]))

    def test_pair_4(self):
        self.assertEquals(-1, in_right_order([[4,4],4,4], [[4,4],4,4,4]))

    def test_pair_5(self):
        self.assertFalse(0, in_right_order([7,7,7,7], [7,7,7]))

    def test_pair_6(self):
        self.assertEquals(-1, in_right_order([], [3]))

    def test_pair_7(self):
        self.assertFalse(0, in_right_order([[[]]], [[]]))

    def test_pair_8(self):
        self.assertFalse(0, in_right_order([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9]))

    def test_pair_9(self):
        self.assertFalse(0,
            in_right_order(
                [[7, 9, 9, [[7, 6], 8], 5], [0, 10, [3, 5, 1, [0, 10, 1, 8]]], [[[10]], [8, [2, 0, 10, 9, 1], 7, [8, 1, 7], [0, 8, 3]]], [[9, [0, 0, 9, 3], [5, 0, 10, 7, 10]], [], [10, 7], [], [[10, 6, 10], [10, 3, 4, 8], 1, []]], [3, [], [[], [7, 10], 0], []]],
                [[[7]]]
            )
        )

    def test_pair_10(self):
        self.assertFalse(0,
            in_right_order(
                [[[], 6, [], [[9, 8, 2, 3, 8], 4, [5], [1, 0], [5, 4, 2, 9, 7]], [1]], [3, []], [[[1, 4], [4, 8, 7], [5, 1, 1]], [[9, 9, 0, 5, 4]], [9, []]]],
                [[[]], [[[3], 9, 4, []], [[2, 6, 3, 10], [5, 8, 9, 5, 8], [5, 5, 2, 7, 1], 10, [2, 8, 0, 4, 10]]], [], [[[2, 5, 10, 7], 10, 3], 6, [[10]], [[5, 3, 0, 7, 1], 6], 4]]
            )
        )


