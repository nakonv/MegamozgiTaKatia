import unittest
from RaceManager import RaceManage

class MockRace:
    def __init__(self, track_name, drivers):
        self.track = MockTrack(track_name)
        self.drivers = drivers
        self.results = [MockResult(d, i * 10.0) for i, d in enumerate(drivers)]

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


if __name__ == '__main__':
    unittest.main()
