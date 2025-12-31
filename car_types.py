from Car import Car

class SportCar(Car):
    """Спортивний автомобіль — максимальна швидкість, високий знос"""
    def calculate_speed(self, track_factor):
        speed = super().calculate_speed(track_factor)
        return speed * 1.25


class EcoCar(Car):
    """Економний автомобіль — менша витрата пального"""
    def calculate_speed(self, track_factor):
        speed = super().calculate_speed(track_factor)
        self.fuel = max(0.0, self.fuel - 2.0)
        return speed * 0.9


class OldCar(Car):
    """Застарілий автомобіль — більший знос і менша швидкість"""
    def calculate_speed(self, track_factor):
        speed = super().calculate_speed(track_factor)
        self.tire_wear = min(100.0, self.tire_wear + 5.0)
        return speed * 0.85
