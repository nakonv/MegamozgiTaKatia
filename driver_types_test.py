import unittest
import random
from driver_types import DriverFactory, RookieDriver, AggressiveDriver, ExperiencedDriver, VeteranDriver, CautiousDriver
from driver import Driver

class TestDriverTypes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # водії різних типів через фабрику
        cls.rookie_driver = DriverFactory.create("rookie", "Rookie Driver", aggression=0.3, skill=0.4, mistakeChance=0.5, overtakingRisk=0.6)
        cls.aggressive_driver = DriverFactory.create("aggressive", "Aggressive Driver", aggression=0.9, skill=0.8, mistakeChance=0.2, overtakingRisk=0.9)
        cls.experienced_driver = DriverFactory.create("experienced", "Experienced Driver", aggression=0.7, skill=0.9, mistakeChance=0.1, overtakingRisk=0.5)
        cls.veteran_driver = DriverFactory.create("veteran", "Veteran Driver", aggression=0.5, skill=0.85, mistakeChance=0.2, overtakingRisk=0.4)
        cls.cautious_driver = DriverFactory.create("cautious", "Cautious Driver", aggression=0.4, skill=0.7, mistakeChance=0.1, overtakingRisk=0.3)

    def test_rookie_driver_initialization(self):
        # правильність ініціалізації для RookieDriver
        self.assertEqual(self.rookie_driver.aggression, 0.3 * 0.5)  # агресивність повинна бути 0.15
        self.assertEqual(self.rookie_driver.skill, 0.4 * 0.6)  # навички повинні бути 0.24

    def test_aggressive_driver_initialization(self):
        # правильність ініціалізації для AggressiveDriver
        self.assertEqual(self.aggressive_driver.aggression, 0.9 * 1.5)  # агресивність повинна бути 1.35

    def test_experienced_driver_initialization(self):
        # правильність ініціалізації для ExperiencedDriver
        self.assertEqual(self.experienced_driver.skill, 0.9 * 1.2)  # навички повинні бути 1.08
        self.assertEqual(self.experienced_driver.mistakeChance, 0.1 * 0.5)  # ймовірність помилки повинна бути 0.05

    def test_veteran_driver_initialization(self):
        # правильність ініціалізації для VeteranDriver
        self.assertEqual(self.veteran_driver.aggression, 0.5 * 0.7)  # агресивність повинна бути 0.35
        self.assertEqual(self.veteran_driver.skill, 0.85 * 0.9)  # навички повинні бути 0.765
        self.assertEqual(self.veteran_driver.mistakeChance, 0.2 * 1.2)  # ймовірність помилки повинна бути 0.24

    def test_cautious_driver_initialization(self):
        # правильність ініціалізації для CautiousDriver
        self.assertEqual(self.cautious_driver.aggression, 0.4 * 0.5)  # агресивність повинна бути 0.2
        self.assertEqual(self.cautious_driver.mistakeChance, 0.1 * 0.7)  # ймовірність помилки повинна бути 0.07

    def test_makeMistake(self):
        # чи робить водій помилку (для цього перевіримо, чи метод повертає значення True або False)
        rookie_mistake = self.rookie_driver.makeMistake()
        aggressive_mistake = self.aggressive_driver.makeMistake()
        experienced_mistake = self.experienced_driver.makeMistake()
        veteran_mistake = self.veteran_driver.makeMistake()
        cautious_mistake = self.cautious_driver.makeMistake()

        # перевірка того, що метод не викликає помилок
        self.assertIn(rookie_mistake, [True, False])
        self.assertIn(aggressive_mistake, [True, False])
        self.assertIn(experienced_mistake, [True, False])
        self.assertIn(veteran_mistake, [True, False])
        self.assertIn(cautious_mistake, [True, False])

if __name__ == "__main__":
    unittest.main()
