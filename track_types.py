from track import Track

class TrackFactory:
  @staticmethod
  def create(track_type, name, length, turns, grip):
    if track_type == "city":
      return CityTrack(name, length, turns, 0.0, grip)
    elif track_type == "race":
      return RaceTrack(name, length, turns, 0.0, grip)
    elif track_type == "wet":
      return WetTrack(name, length, turns, 0.0, grip)
    else:
      raise ValueError("Невідомий тип треку")

class CityTrack(Track):
  def trackModifier(self):
    return 0.85

class RaceTrack(Track):
  def trackModifier(self):
    return 1.1

class WetTrack(Track):
  def trackModifier(self):
    return 0.7 + self.grip * 0.3
