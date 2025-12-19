from driver import Driver

class DriverManadger:
    def __init__(self, drivers):
        self.drivers = drivers

    def search_drivers_by_skill(self, min_skill):           # пошук за мінімальним рівнем навичок (min_skill і вище)
        return[driver for driver in self.drivers if driver.skill >= min_skill]
    
    def sort_drivers_by_skill(self):              # сортування за навичками (від найгіршого до найкращого)
        return sorted(self.drivers, key=lambda driver: driver.skill, reverse=True)

    def sort_drivers_by_aggression(self):           # сортування за агресивністю (від агресивніших до менш)
        return sorted(self.drivers, key=lambda driver: driver.aggression, reverse=True)

    def search_drivers_by_aggression(self, min_aggression):          # пошук за мініальною агресивністю (min_aggression і вище)
        return [driver for driver in self.drivers if driver.aggression >= min_aggression]
