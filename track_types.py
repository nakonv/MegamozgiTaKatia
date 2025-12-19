from track import Track

class CityTrack(Track):
  def getSectionSpeedFactor(self, sectionIndex):
    base = super().getSectionSpeedFactor(sectionIndex)
    return base * 0.85

class RaceTrack(Track):
  def getSectionSpeedFactor(self, sectionIndex):
    base = super().getSectionSpeedFactor(sectionIndex)
    return base * 1.1

class WetTrack(Track):
  def getSectionSpeedFactor(self, sectionIndex):
    base = super().getSectionSpeedFactor(sectionIndex)
    return base * (0.7 + self.grip * 0.3)
