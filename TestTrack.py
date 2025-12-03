import unittest
from track import Track


class MyTestCase(unittest.TestCase):
    def test_constructor(self):
        t = Track("Monaco", 3300, 19, grip=0.8)

        self.assertEqual(t.name, "Monaco")
        self.assertEqual(t.length, 3300)
        self.assertEqual(t.turns, 19)

        expected_complexity = min(1.0, (19 / 10) * (1.0 - 0.8))
        self.assertAlmostEqual(t.complexity, expected_complexity)


if __name__ == '__main__':
    unittest.main()
