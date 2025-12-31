import unittest
from Car import Car
from driving_modes import AggressiveMode, SafeMode

class TestDrivingMode(unittest.TestCase):

    def test_aggressive_mode(self):
        car = Car("Ferrari", 900, 85, 80)
        car.set_mode(AggressiveMode())
        car.apply_mode()

        self.assertGreater(car.engine_power, 900)

    def test_safe_mode(self):
        car = Car("Mercedes", 900, 85, 80, tire_wear=20)
        car.set_mode(SafeMode())
        car.apply_mode()

        self.assertLess(car.engine_power, 900)
        self.assertLess(car.tire_wear, 20)

if __name__ == "__main__":
    unittest.main()
