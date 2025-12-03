class Track:
  def __init__(self, name="", length=0, turns=0, complexity=0.0, grip=1.0):
    self.name = name
    self.length = length      #довжина кола (м)
    self.turns = turns        #кількість поворотів
    self.grip = grip        #зчеплення покриття з шинами
    self.complexity = min(1.0, (self.turns / 10) * (1.0 - self.grip)) #коефіцієнт складності (0–1)

  def getSectionSpeedFactor(self, sectionIndex):
    base_factor = 1.0 - self.complexity * 0.5 - min(self.turns * 0.02, 0.3)
    grip_factor = self.grip * 0.8 + 0.2
    return base_factor * grip_factor

  def loadFromFile(self, filename):
    with open(filename, "r", encoding="utf-8") as f:
      lines = [line.strip() for line in f.readlines()]
    self.name = lines[0]
    self.length = int(lines[1])
    self.turns = int(lines[2])
    self.complexity = float(lines[3])
    self.grip = float(lines[4])
