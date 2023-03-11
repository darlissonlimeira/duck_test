import unittest
from little_ducks import show_duck_name


class TestShowDuckName(unittest.TestCase):
    def test_prefix_J(self):
        self.assertEqual(show_duck_name('J'), 'Jack', "if prefix equal to J result should be Jack")

    def test_prefix_O(self):
        self.assertEqual(show_duck_name('O'), 'Ouack', "if prefix equal to O result should be Ouack")

    def test_prefix_Q(self):
        self.assertEqual(show_duck_name('Q'), 'Quack', "if prefix equal to Q result should be Quack")

    def test_invalid_prefix(self):
        self.assertIsNone(show_duck_name(2), "if prefix is type of int invalid should return None")
        self.assertIsNone(show_duck_name(bool), "if prefix is type of bool should return None")

    def test_wrong_prefix(self):
        self.assertIsNone(show_duck_name('A'), "if prefix equal to A should return None")
        self.assertIsNone(show_duck_name('B'), "if prefix equal to B should return None")
        self.assertIsNone(show_duck_name('2'), "if prefix equal to '2' should return None")

    def test_lowercase_prefix(self):
        self.assertEqual(show_duck_name('j'), 'Jack', "if prefix equal to j result should be Jack")
        self.assertEqual(show_duck_name('o'), 'Ouack', "if prefix equal to o result should be Ouack")


if __name__ == '__main__':
    unittest.main()
