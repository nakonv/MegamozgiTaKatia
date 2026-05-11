from Car import Car
class Fleet:
    def __init__(self, name):
        self.name = name
        self.cars = [] 

    def add_car(self, car):
        self.cars.append(car)
        print(f"Авто '{car.team_name}' додано до автопарку '{self.name}'")

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"Авто '{car.team_name}' видалено з автопарку")
        else:
            print("Авто не знайдено в автопарку.")

    def print_fleet(self):
        print(f"\nАвтопарк: {self.name}")
        print("Машини у складі:")
        if not self.cars:
            print("  (порожньо)")
            return
        for car in self.cars:
            car.print_specs()

    def service_all(self):
        print(f"\nПроводимо обслуговування всіх авто в автопарку '{self.name}':")
        for car in self.cars:
            car.refuel(100)
            car.change_tires(car.tire_grip)
