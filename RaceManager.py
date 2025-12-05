from Race import Race

class RaceManage:
    def __init__(self, name):
        self.name = name
        self.races = []  
        
    def addRace(self, race: Race):
        self.races.append(race)

    def totalDrivers(self):
        drivers = set()
        for race in self.races:
            for d in race.drivers:
                drivers.add(d.name)
        return len(drivers)

    def saveChampionshipResults(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Чемпіонат: {self.name}\n\n")
            for i, race in enumerate(self.races, start=1):
                f.write(f"Гонка #{i} ({race.track.name}):\n")
                for idx, r in enumerate(race.sortedResults(), start=1):
                    f.write(f"  {idx}. {r.driver.name}: {r.total_time:.2f} с\n")
                f.write("\n")
  


