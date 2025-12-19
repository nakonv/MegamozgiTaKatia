from abc import ABC, abstractmethod
from driver_types import RookieDriver, AggressiveDriver, ExperiencedDriver, VeteranDriver, CautiousDriver

class DriverFactory(ABC):
    @abstractmethod
    def create_driver(self, name):
        pass

class RookieDriverFactory(DriverFactory):
    def create_driver(self, name):
        return RookieDriver(name, aggression=0.3, skill=0.4, mistakeChance=0.5, overtakingRisk=0.6)

class AggressiveDriverFactory(DriverFactory):
    def create_driver(self, name):
        return AggressiveDriver(name, aggression=0.9, skill=0.8, mistakeChance=0.2, overtakingRisk=0.9)

class ExperiencedDriverFactory(DriverFactory):
    def create_driver(self, name):
        return ExperiencedDriver(name, aggression=0.7, skill=0.9, mistakeChance=0.1, overtakingRisk=0.5)

class VeteranDriverFactory(DriverFactory):
    def create_driver(self, name):
        return VeteranDriver(name, aggression=0.5, skill=0.85, mistakeChance=0.2, overtakingRisk=0.4)

class CautiousDriverFactory(DriverFactory):
    def create_driver(self, name):
        return CautiousDriver(name, aggression=0.4, skill=0.7, mistakeChance=0.1, overtakingRisk=0.3)
