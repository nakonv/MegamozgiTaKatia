class Race:
  def __init__(self, track, laps=3):
    self.track = track #об'єкт класу трек, агрегація
    self.laps = laps #к-ть кіл 
    self.cars = [] #список машин, агрегація
    self.drivers = [] #список водіїв, агрегація
    self.results = [] #результати, композиця (RaceResult)

  def addParticipant(self, driver, car): #додає машину і водія
    self.drivers.append(driver)
    self.cars.append(car)
    self.results.append(RaceResult(driver)) #композиція

  def startRace(self): #починає симуляцію гонки
    for lap in range(1, self.laps + 1):
      self.simulateLap(lap)

  def simulateLap(self, lapIndex):
    for i, car in enumerate(self.cars):
      driver = self.drivers[i]
      current_result = self.results[i]

      section_speed = car.calculate_speed(self.track.getSectionSpeedFactor(lapIndex))
      section_time = self.track.length / section_speed
      current_result.add_time(section_time)
      car.update_wear()

  def sortedResults(self):
    return sorted(self.results, key=lambda r: r.total_time)

  def saveResults(self, filename):
    with open(filename, "w", encoding="utf-8") as f:
      f.write("Результати гонки:\n")
      for idx, r in enumerate(self.sortedResults(), start=1):
        f.write(f"{idx}. {r.driver.name}: {r.total_time:.2f} с\n")

class RaceResult:
  def __init__(self, driver):
      self.driver = driver
      self.total_time = 0.0
    
  def add_time(self, time):
      self.total_time += time
