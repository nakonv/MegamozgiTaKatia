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
  

