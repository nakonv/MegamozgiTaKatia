import unittest
from Car import Car


class TestCar(unittest.TestCase):

    def test_initialization(self):
        car = Car(team_name="Ferrari", engine_power=900, aerodynamics=85, tire_grip=80)

        self.assertEqual(car.team_name, "Ferrari")
        self.assertEqual(car.engine_power, 900)
        self.assertEqual(car.aerodynamics, 85)
        self.assertEqual(car.tire_grip, 80)
        self.assertEqual(car.fuel, 100.0)
        self.assertEqual(car.tire_wear, 0.0)
        self.assertEqual(car.speed, 0.0)

    def test_calculate_speed(self):
        car = Car(team_name="Mercedes", engine_power=800, aerodynamics=90, tire_grip=85)

        speed = car.calculate_speed(track_factor=1.0)

        expected_performance = (
            car.engine_power * 0.4 +
            car.aerodynamics * 0.3 +
            car.tire_grip * 0.3
        )
        expected_speed = expected_performance * (1 - car.tire_wear/100) * (car.fuel/100)

        self.assertAlmostEqual(speed, expected_speed, places=4)

    def test_calculate_speed_no_fuel(self):
        car = Car("RedBull", 950, 95, 90, fuel=0.0)

        speed = car.calculate_speed(track_factor=1.0)

        self.assertEqual(speed, 0)

    def test_calculate_speed_full_wear(self):
        car = Car("McLaren", 870, 88, 87, tire_wear=100.0)

        speed = car.calculate_speed(track_factor=1.0)

        self.assertEqual(speed, 0)

    def test_refuel(self):
        car = Car("Alpine", 750, 80, 75, fuel=50)

        car.refuel(40)

        self.assertEqual(car.fuel, 90)

        car.refuel(50) 
        self.assertEqual(car.fuel, 100)

    def test_change_tires(self):
        car = Car("Williams", 700, 70, 60, tire_wear=50)

        car.change_tires(new_grip=85)

        self.assertEqual(car.tire_grip, 85)
        self.assertEqual(car.tire_wear, 0.0)

    def test_update_wear(self):
        car = Car("Haas", 600, 60, 55, fuel=100, tire_wear=0)

        car.update_wear()

        self.assertAlmostEqual(car.fuel, 95.0, places=1)
        self.assertAlmostEqual(car.tire_wear, 3.0, places=1)

        car.update_wear()
        self.assertAlmostEqual(car.fuel, 90.0, places=1)
        self.assertAlmostEqual(car.tire_wear, 6.0, places=1)


if __name__ == "__main__":
    unittest.main()
