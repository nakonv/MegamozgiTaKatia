from abc import ABC, abstractmethod

class DrivingMode(ABC):
    """Базова стратегія керування автомобілем"""
    @abstractmethod
    def apply(self, car):
        pass


class AggressiveMode(DrivingMode):
    """Агресивний режим керування"""
    def apply(self, car):
        car.engine_power *= 1.15
        car.tire_wear = min(100.0, car.tire_wear + 7)


class SafeMode(DrivingMode):
    """Безпечний режим керування"""
    def apply(self, car):
        car.engine_power *= 0.9
        car.tire_wear = max(0.0, car.tire_wear - 3)
