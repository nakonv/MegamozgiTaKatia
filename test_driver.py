import random
import unittest
from driver import Driver
from track import Track

class TestDriver(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # створюємо водіїв та трек
        cls.track = Track("Test Track", 5000, 15, grip=0.8)
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
    @classmethod
    def tearDownClass(cls):
        print("\nTests completed.")

if __name__ == "__main__":
    unittest
