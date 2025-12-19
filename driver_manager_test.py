import unittest
from driver import Driver
from driver_manager import DriverManadger

class TestDriverManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # список водіїв з різними значеннями параметрів 
        cls.drivers = [
            Driver("Driver 1", aggression=0.3, skill=0.4, mistakeChance=0.5, overtakingRisk=0.6),
            Driver("Driver 2", aggression=0.9, skill=0.8, mistakeChance=0.2, overtakingRisk=0.9),
            Driver("Driver 3", aggression=0.7, skill=0.9, mistakeChance=0.1, overtakingRisk=0.5),
            Driver("Driver 4", aggression=0.5, skill=0.85, mistakeChance=0.2, overtakingRisk=0.4),
            Driver("Driver 5", aggression=0.4, skill=0.7, mistakeChance=0.1, overtakingRisk=0.3)
        ]
      
        cls.manager = DriverManadger(cls.drivers)

    def test_search_drivers_by_skill(self):
        # пошук водіїв з мінімальними навичками >= 0.7
        result = self.manager.search_drivers_by_skill(0.7)

        # перевірка результатів пошуку
        self.assertEqual(len(result), 3)
        self.assertIn(self.drivers[1], result)  # "Driver 2"
        self.assertIn(self.drivers[2], result)  # "Driver 3"
        self.assertIn(self.drivers[3], result)  # "Driver 4"

    def test_search_drivers_by_aggression(self):
        # пошук водіїв з мінімальною агресивністю >= 0.7
        result = self.manager.search_drivers_by_aggression(0.7)

        # перевірка результатів пошуку
        self.assertEqual(len(result), 2)
        self.assertIn(self.drivers[1], result)  # "Driver 2"
        self.assertIn(self.drivers[2], result)  # "Driver 3"

    def test_sort_drivers_by_skill(self):
        # сортуємо водіїв за навичками
        sorted_drivers = self.manager.sort_drivers_by_skill()

        # перевірка правильності сортування
        self.assertEqual(sorted_drivers[0], self.drivers[2])  # "Driver 3"
        self.assertEqual(sorted_drivers[1], self.drivers[1])  # "Driver 2"
        self.assertEqual(sorted_drivers[2], self.drivers[3])  # "Driver 4"
        self.assertEqual(sorted_drivers[3], self.drivers[4])  # "Driver 5"
        self.assertEqual(sorted_drivers[4], self.drivers[0])  # "Driver 1"

    def test_sort_drivers_by_aggression(self):
        # сортуємо водіїв за агресивністю
        sorted_drivers = self.manager.sort_drivers_by_aggression()

        # перевірка правильності сортування
        self.assertEqual(sorted_drivers[0], self.drivers[1])  # "Driver 2"
        self.assertEqual(sorted_drivers[1], self.drivers[2])  # "Driver 3"
        self.assertEqual(sorted_drivers[2], self.drivers[3])  # "Driver 4"
        self.assertEqual(sorted_drivers[3], self.drivers[4])  # "Driver 5"
        self.assertEqual(sorted_drivers[4], self.drivers[0])  # "Driver 1"

if __name__ == "__main__":
    unittest.main()
