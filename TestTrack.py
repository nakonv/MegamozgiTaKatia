import unittest
import os
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

    def test_loadFromFile(self):
        #тимчасовий файл
        filename = "track_data.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("Spa\n")
            f.write("7004\n")
            f.write("20\n")
            f.write("0.4\n")
            f.write("0.9\n")

        t = Track()
        t.loadFromFile(filename)

        self.assertEqual(t.name, "Spa")
        self.assertEqual(t.length, 7004)
        self.assertEqual(t.turns, 20)
        self.assertEqual(t.complexity, 0.4)
        self.assertEqual(t.grip, 0.9)

        os.remove(filename)


if __name__ == '__main__':
    unittest.main()

