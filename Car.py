class Car:
    def __init__(self, team_name, engine_power, aerodynamics, tire_grip, fuel=100.0, tire_wear=0.0, speed=0.0):
        self.team_name = team_name
        self.engine_power = engine_power
        self.aerodynamics = aerodynamics
        self.tire_grip = tire_grip
        self.fuel = fuel
        self.tire_wear = tire_wear
        self.speed = speed

    def print_specs(self):
        print(f"Команда: {self.team_name}")
        print(f"Потужність двигуна: {self.engine_power} к.с.")
        print(f"Аеродинаміка: {self.aerodynamics}")
        print(f"Зчеплення шин: {self.tire_grip}")
        print(f"Рівень пального: {self.fuel:.1f}%")
        print(f"Зношеність шин: {self.tire_wear:.1f}%")
        print(f"Поточна швидкість: {self.speed:.1f} км/год")

    def calculate_speed(self, track_factor):
        if self.fuel <= 0 or self.tire_wear >= 100:
            self.speed = 0
        else:
            performance_factor = (self.engine_power * 0.4 +
                                  self.aerodynamics * 0.3 +
                                  self.tire_grip * 0.3)
            wear_penalty = (100 - self.tire_wear) / 100
            fuel_penalty = self.fuel / 100
            self.speed = performance_factor * track_factor * wear_penalty * fuel_penalty
        return self.speed

    def refuel(self, amount):
        self.fuel = min(100.0, self.fuel + amount)
        print(f"Автомобіль заправлено. Поточний рівень пального: {self.fuel:.1f}%")

    def change_tires(self, new_grip):
        self.tire_grip = new_grip
        self.tire_wear = 0.0
        print(f"Шини замінено. Нове зчеплення: {self.tire_grip}")

    def update_wear(self):
        fuel_consumption = 5.0
        tire_degradation = 3.0

        self.fuel = max(0.0, self.fuel - fuel_consumption)
        self.tire_wear = min(100.0, self.tire_wear + tire_degradation)
        print(f"Оновлено: пальне = {self.fuel:.1f}%, зношеність шин = {self.tire_wear:.1f}%")

def set_mode(self, mode):
    self.mode = mode

def apply_mode(self):
    if hasattr(self, "mode") and self.mode:
        self.mode.apply(self)
