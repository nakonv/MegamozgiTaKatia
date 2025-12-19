from track import Track

class CityTrack(Track):
  def trackModifier(self):
    return 0.85

class RaceTrack(Track):
  def trackModifier(self):
    return 1.1

class WetTrack(Track):
  def trackModifier(self):
    return 0.7 + self.grip * 0.3
