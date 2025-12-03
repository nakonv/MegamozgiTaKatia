import unittest
from track import Track


class MyTestCase(unittest.TestCase):
    def test_constructor(self):
        t = Track("Test", 3300, 19, grip=0.8)

        self.assertEqual(t.name, "Test")
        self.assertEqual(t.length, 3300)
        self.assertEqual(t.turns, 19)

        expected_complexity = min(1.0, (19 / 10) * (1.0 - 0.8))
        self.assertAlmostEqual(t.complexity, expected_complexity)

    def test_getSectionSpeedFactor(self):
        t = Track("Test", 1000, 10, grip=0.7)
        factor = t.getSectionSpeedFactor(0)

        base_factor = 1.0 - t.complexity * 0.5 - min(t.turns * 0.02, 0.3)
        grip_factor = t.grip * 0.8 + 0.2
        expected = base_factor * grip_factor

        self.assertAlmostEqual(factor, expected)


if __name__ == '__main__':
    unittest.main()
