import random
import unittest
from driver import Driver
from track import Track
from Car import Car

class TestDriver(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # створюємо водіїв та трек
        cls.track = Track("Test Track", 5000, 15, grip=0.8)

        cls.car1 = Car("Team A", 500, 0.8, 0.9)
        cls.car2 = Car("Team B", 480, 0.7, 0.85)

        cls.d1 = Driver("Hamilton", 70, 95, 40, 40)
        cls.d2 = Driver("Verstappen", 90, 92, 50, 60)

    def test_driver_profile_before_adaptation(self):
        # Тестуємо початкові профілі водіїв
        print("Profile before adapting to track:")
        self.d1.printProfile()
        self.d2.printProfile()

        # Перевіряємо початкові значення
        self.assertEqual(self.d1.name, "Hamilton")
        self.assertEqual(self.d2.name, "Verstappen")

    def test_adopted_to_track(self):
        # Перевірка адаптації водіїв до треку
        print("\nAdopted to track:")
        self.d1.adoptedToTrack(self.track)
        self.d2.adoptedToTrack(self.track)
    
    def test_reaction_time(self):
        # Перевірка часу реакції
        print("\nReaction time:")
        d1_reaction_time = self.d1.reactionTime()
        d2_reaction_time = self.d2.reactionTime()

        print(f"{self.d1.name}: {d1_reaction_time:.3f} s")
        print(f"{self.d2.name}: {d2_reaction_time:.3f} s")

    def test_make_mistakes(self):
        # Тестуємо помилки водіїв
        print("\nSimulation 50 events:")
        for i in range(1, 51):
            m1 = self.d1.makeMistake()
            m2 = self.d2.makeMistake()
            print(
                f"Event {i:2d}: "
                f"{self.d1.name} -> {'error' if m1 else 'ok'}, "
                f"{self.d2.name} -> {'error' if m2 else 'ok'}"
            )

            # Перевіряємо, що ймовірність помилки не є більше 1
            self.assertLessEqual(self.d1.mistakeChance, 1)
            self.assertLessEqual(self.d2.mistakeChance, 1)
    
    def test_calculate_speed(self):
        # Перевірка обчислення швидкості водія
        print("\nSpeed calculation:")
        d1_speed = self.d1.car.calculate_speed(self.track, self.d1)  # Швидкість водія 1
        d2_speed = self.d2.car.calculate_speed(self.track, self.d2)  # Швидкість водія 2

        print(f"{self.d1.name}'s speed: {d1_speed:.2f} km/h")
        print(f"{self.d2.name}'s speed: {d2_speed:.2f} km/h")

        # Перевіряємо, чи швидкість водіїв коректно обчислюється
        self.assertGreater(d1_speed, 0)
        self.assertGreater(d2_speed, 0)

    def test_race_time(self):
        # Перевірка часу гонки (час на коло)
        print("\nRace time calculation:")
        d1_time = self.track.length / self.d1.car.calculate_speed(self.track, self.d1)  # Час водія 1 на коло
        d2_time = self.track.length / self.d2.car.calculate_speed(self.track, self.d2)  # Час водія 2 на коло

        print(f"{self.d1.name}'s time per lap: {d1_time:.2f} s")
        print(f"{self.d2.name}'s time per lap: {d2_time:.2f} s")

        # Перевіряємо, чи час на коло правильний
        self.assertGreater(d1_time, 0)
        self.assertGreater(d2_time, 0)
    @classmethod
    def tearDownClass(cls):
        print("\nTests completed.")

if __name__ == "__main__":
    unittest.main()
