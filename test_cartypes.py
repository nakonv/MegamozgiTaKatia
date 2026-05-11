import unittest
from SportCar import SportCar
from EcoCar import EcoCar
from OldCar import OldCar
from CarManager import CarManager

class TestCarPolymorphism(unittest.TestCase):

    def test_cars_behavior(self):
        c1 = SportCar("Ferrari", 900, 85, 80)
        c2 = EcoCar("Toyota", 700, 80, 85)
        c3 = OldCar("Ford", 650, 70, 70)

        cars = [c1, c2, c3]

        for car in cars:
            car.calculate_speed(1.0)

        self.assertNotEqual(c1.speed, c2.speed)
        self.assertNotEqual(c2.speed, c3.speed)

if __name__ == "__main__":
    unittest.main()
