import unittest
from track import Track
from driver import Driver
from Car import Car
from Race import Race


class MyTestCase(unittest.TestCase):
    def test_addParticipant(self):
        track = Track("TestTrack", 3000, 10, grip=0.8)
        race = Race(track, laps=3)
        driver = Driver(name="Tester", aggression=0.3, skill=0.8, mistakeChance=0.1, overtakingRisk=0.2)
        car = Car(team_name="Ferrari", engine_power=800, aerodynamics=0.9, tire_grip=0.85, fuel=100, tire_wear=0, speed=250.0)

        race.addParticipant(driver, car)

        self.assertEqual(len(race.drivers), 1)
        self.assertEqual(len(race.cars), 1)


if __name__ == '__main__':
    unittest.main()
