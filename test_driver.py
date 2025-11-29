import random
from driver import Driver

class TestTrack:        # модель траси для тестування
    def __init__(self, complexity, grip):
        self.complexity = complexity
        self.grip = grip
    

if __name__ == "__name__":
    rng = random.Random(42)

    d1 = Driver("Hamilton", 70, 95, 5, 40, rng=rng)
    d2 = Driver("Verstappen", 90, 92, 7, 60, rng=rng)

    print("profile before adapted to track")
    d1.printProfile()
    d2.printProfile()

     # Створюємо трасу
    track = TestTrack(complexity=0.7, grip=0.6)

    print("\nAdopted to track...")
    d1.adoptedToTrack(track)
    d2.adoptedToTrack(track)

    print("\nProfile after adopted")
    d1.printProfile()
    d2.printProfile()

    # час реакції
    print("\nReaction time:")
    print(f"{d1.name}: {d1.reactionTime():.3f} c")
    print(f"{d2.name}: {d2.reactionTime():.3f} c")

    print("\nSimulation 10 event:")
    for i in range(1, 11):
        m1 = d1.makeMistake()
        m2 = d2.makeMistake()
        print(
            f"Event {i:2d}: "
            f"{d1.name} -> {'error' if m1 else 'ок'}, "
            f"{d2.name} -> {'error' if m2 else 'ок'}"
        )