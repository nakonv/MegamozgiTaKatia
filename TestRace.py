import unittest
import os
from driver import Driver
from Race import Race

class MockTrack:
    def __init__(self, length):
        self.length = length

    def getSectionSpeedFactor(self, lapIndex):
        return 1.0

class MockCar:
    def __init__(self, speed):
        self.speed = speed
        self.wear_updates = 0

    def calculate_speed(self, factor):
        return self.speed * factor

    def update_wear(self):
        self.wear_updates += 1

class MyTestCase(unittest.TestCase):
    def test_addParticipant(self):
        track = MockTrack(5000)
        race = Race(track, laps=1)
        driver = Driver(name="Tester", aggression=0.3, skill=0.8, mistakeChance=0.1, overtakingRisk=0.2)
        car = MockCar(250)

        race.addParticipant(driver, car)

        self.assertEqual(len(race.drivers), 1)
        self.assertEqual(len(race.cars), 1)

    def test_simulateLap(self):
        track = MockTrack(5000)
        race = Race(track, laps=1)
        driver = Driver(name="Tester", aggression=0.3, skill=0.8, mistakeChance=0.1, overtakingRisk=0.2)
        car = MockCar(250)

        race.addParticipant(driver, car)
        race.startRace()

        result_names = [r.driver.name for r in race.results]
        self.assertIn("Tester", result_names)

        expected_time = 5000 / 250  # length / speed
        total_time = race.results[0].total_time
        self.assertAlmostEqual(total_time, expected_time, places=4)

    def test_sorted_results(self):
        track = MockTrack(5000)
        race = Race(track, laps=1)

        d1 = Driver(name="Tester1", aggression=0.8, skill=0.7, mistakeChance=0.2, overtakingRisk=0.5)
        c1 = MockCar(200)

        d2 = Driver(name="Tester2", aggression=0.3, skill=0.8, mistakeChance=0.1, overtakingRisk=0.2)
        c2 = MockCar(300)

        race.addParticipant(d1, c1)
        race.addParticipant(d2, c2)
        race.startRace()

        sorted_res = race.sortedResults()

        self.assertEqual(sorted_res[0].driver.name, "Tester2")
        self.assertEqual(sorted_res[1].driver.name, "Tester1")

    def test_save_results(self):
        track = MockTrack(5000)
        race = Race(track, laps=1)

        driver = Driver(name="Tester", aggression=0.3, skill=0.8, mistakeChance=0.1, overtakingRisk=0.2)
        car = MockCar(250)

        race.addParticipant(driver, car)
        race.startRace()

        filename = "test_results.txt"
        race.saveResults(filename)

        self.assertTrue(os.path.exists(filename))

        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("Результати гонки", content)

        os.remove(filename)


if __name__ == '__main__':
    unittest.main()



