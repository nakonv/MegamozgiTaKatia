class CarManager:
    def __init__(self, cars):
        self.cars = cars

    def sort_by_speed(self):
        return sorted(self.cars, key=lambda c: c.speed, reverse=True)

    def search_by_fuel(self, min_fuel):
        return [c for c in self.cars if c.fuel >= min_fuel]
