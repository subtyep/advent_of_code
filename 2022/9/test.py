import unittest

from day_9_2 import Point

class TestPoint(unittest.TestCase):

    def setUp(self) -> None:
        self.tail = Point(0, 0)

    def assertSpot(self, x, y):
        self.assertEqual((x, y), (self.tail.x, self.tail.y))

    def test_one_up(self):
        head = Point(0, 2)
        self.tail.move_towards(head)
        self.assertSpot(0, 1)

    def test_one_right(self):
        head = Point(2, 0)
        self.tail.move_towards(head)
        self.assertSpot(1, 0)

    def test_one_down(self):
        head = Point(0, -2)
        self.tail.move_towards(head)
        self.assertSpot(0, -1)

    def test_one_left(self):
        head = Point(-2, 0)
        self.tail.move_towards(head)
        self.assertSpot(-1, 0)

    def test_up_right_1(self):
        head = Point(1, 2)
        self.tail.move_towards(head)
        self.assertSpot(1, 1)

    def test_up_right_1(self):
        head = Point(2, 1)
        self.tail.move_towards(head)
        self.assertSpot(1, 1)

    def test_up_right_3(self):
        head = Point(2, 2)
        self.tail.move_towards(head)
        self.assertSpot(1, 1)

    def test_down_right_1(self):
        head = Point(1, -2)
        self.tail.move_towards(head)
        self.assertSpot(1, -1)

    def test_down_right_1(self):
        head = Point(2, -1)
        self.tail.move_towards(head)
        self.assertSpot(1, -1)

    def test_down_right_3(self):
        head = Point(2, -2)
        self.tail.move_towards(head)
        self.assertSpot(1, -1)

    def test_down_left_1(self):
        head = Point(-1, -2)
        self.tail.move_towards(head)
        self.assertSpot(-1, -1)

    def test_down_left_1(self):
        head = Point(-2, -1)
        self.tail.move_towards(head)
        self.assertSpot(-1, -1)

    def test_down_left_3(self):
        head = Point(-2, -2)
        self.tail.move_towards(head)
        self.assertSpot(-1, -1)

    def test_up_left_1(self):
        head = Point(-1, 2)
        self.tail.move_towards(head)
        self.assertSpot(-1, 1)

    def test_up_left_1(self):
        head = Point(-2, 1)
        self.tail.move_towards(head)
        self.assertSpot(-1, 1)

    def test_up_left_3(self):
        head = Point(-2, 2)
        self.tail.move_towards(head)
        self.assertSpot(-1, 1)

    def test_no_move_1(self):
        head = Point(-1, 0)
        self.tail.move_towards(head)
        self.assertSpot(0, 0)

    def test_no_move_2(self):
        head = Point(-1, 1)
        self.tail.move_towards(head)
        self.assertSpot(0, 0)

    def test_no_move_3(self):
        head = Point(-1, -1)
        self.tail.move_towards(head)
        self.assertSpot(0, 0)

    def test_no_move_4(self):
        head = Point(0, 1)
        self.tail.move_towards(head)
        self.assertSpot(0, 0)

    def test_no_move_5(self):
        head = Point(0, -1)
        self.tail.move_towards(head)
        self.assertSpot(0, 0)

    def test_no_move_6(self):
        head = Point(1, 1)
        self.tail.move_towards(head)
        self.assertSpot(0, 0)

    def test_no_move_7(self):
        head = Point(1, 0)
        self.tail.move_towards(head)
        self.assertSpot(0, 0)

    def test_no_move_8(self):
        head = Point(1, -1)
        self.tail.move_towards(head)
        self.assertSpot(0, 0)
