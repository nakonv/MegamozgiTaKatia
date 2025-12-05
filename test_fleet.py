import unittest
from Car import Car
from Fleet import Fleet

class MockCar(Car):
    def print_specs(self):
        pass

    def refuel(self, amount):
        self.fuel = min(100.0, self.fuel + amount)

    def change_tires(self, new_grip):
        self.tire_grip = new_grip
        self.tire_wear = 0.0


class TestFleet(unittest.TestCase):

    def test_add_car(self):
        fleet = Fleet("TestFleet")
        car = MockCar("Ferrari", 900, 85, 80)

        fleet.add_car(car)

        self.assertEqual(len(fleet.cars), 1)
        self.assertIs(fleet.cars[0], car)

    def test_remove_car(self):
        fleet = Fleet("TestFleet")
        car1 = MockCar("Ferrari", 900, 85, 80)
        car2 = MockCar("McLaren", 880, 82, 78)

        fleet.add_car(car1)
        fleet.add_car(car2)
        fleet.remove_car(car1)

        self.assertEqual(len(fleet.cars), 1)
        self.assertIs(fleet.cars[0], car2)

    def test_print_fleet(self):
        fleet = Fleet("TestFleet")
        car = MockCar("Ferrari", 900, 85, 80)
        fleet.add_car(car)

        try:
            fleet.print_fleet()
        except Exception as e:
            self.fail(f"print_fleet викликав помилку: {e}")

    def test_service_all(self):
        fleet = Fleet("TestFleet")
        car = MockCar("Ferrari", 900, 85, 80, fuel=50.0, tire_wear=40.0)
        fleet.add_car(car)

        fleet.service_all()

        self.assertEqual(car.fuel, 100.0)
        self.assertEqual(car.tire_wear, 0.0)

    def test_aggregation(self):
        fleet = Fleet("TestFleet")
        car = MockCar("Ferrari", 900, 85, 80)

        fleet.add_car(car)

        self.assertIsNotNone(car)
        self.assertIn(car, fleet.cars)


if __name__ == "__main__":
    unittest.main()
