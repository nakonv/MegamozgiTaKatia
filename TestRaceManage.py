import unittest
from RaceManager import RaceManage

class MockRace:
    def __init__(self, track_name, drivers):
        self.track = MockTrack(track_name)
        self.drivers = drivers
        self.results = [MockResult(d, i * 10.0) for i, d in enumerate(drivers)]

      def sortedResults(self):
        return sorted(self.results, key=lambda r: r.total_time)

class MockResult:
    def __init__(self, driver, total_time):
        self.driver = driver
        self.total_time = total_time

class MockTrack:
    def __init__(self, name):
        self.name = name

class MockDriver:
    def __init__(self, name):
        self.name = name

class MyTestCase(unittest.TestCase):
    def test_addRace(self):
        rm = RaceManage("TestChampionship")

        race1 = MockRace("Track1", [MockDriver("A"), MockDriver("B")])
        rm.addRace(race1)

        self.assertEqual(len(rm.races), 1)
        self.assertEqual(rm.races[0].track.name, "Track1")

    def test_totalDrivers(self):
        rm = RaceManage("TestChampionship")

        race1 = MockRace("Track1", [MockDriver("A"), MockDriver("B")])
        race2 = MockRace("Track2", [MockDriver("B"), MockDriver("C")])

        rm.addRace(race1)
        rm.addRace(race2)

        self.assertEqual(rm.totalDrivers(), 3)

    def test_saveChampionshipResults(self):
        rm = RaceManage("TestChampionship")

        race1 = MockRace("Grand Prix A", [MockDriver("AA"), MockDriver("BB")])
        rm.addRace(race1)

        filename = "test_champ_results.txt"
        rm.saveChampionshipResults(filename)

        self.assertTrue(os.path.exists(filename))

        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()

        self.assertIn("Чемпіонат: TestChampionship", content)
        self.assertIn("Гонка #1 (Grand Prix A):", content)
        self.assertIn("AA", content)
        self.assertIn("BB", content)

        os.remove(filename)


if __name__ == '__main__':
    unittest.main()

