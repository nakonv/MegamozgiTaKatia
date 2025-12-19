from track_types import CityTrack, RaceTrack, WetTrack, TrackFactory
from race import Race

def main():
  track = TrackFactory.create("wet", "Spa", 7004, 20, grip=0.7)
  race = Race(track, laps=3)

  #додати драйверів
  #додати машинки

  race.addParticipant(driver1, car1)
  race.addParticipant(driver2, car2)

  race.startRace()
  race.saveResults("results.txt")

  championship = RaceManage("F1 Demo")
  championship.addRace(race)
  championship.saveChampionshipResults("championship.txt")

  print("Гонка завершена. Результати збережені.")

if __name__ == "__main__":
    main()
