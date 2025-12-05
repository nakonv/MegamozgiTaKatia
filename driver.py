import random

class Driver:
    def __init__(self, name, aggression, skill, mistakeChance, overtakingRisk, rng=None):
        self.name = name    # ім'я гонщика
        self.aggression = self._norm01(aggression)   # агресивність [0; 1] 
        self.skill = self._norm01(skill)    # навички [0; 1]
        self.mistakeChance = self._norm01(mistakeChance)    # ймовірність помилки [0; 1]
        self.overtakingRisk = self._norm01(overtakingRisk)     # ризикованість під час обгону [0; 1]
        #self.rng = rng or random.Random()
        

    def _norm01(self, x: float) ->float:
        if x > 1:
            x = x / 100.0
        return max(0.0, min(1.0, x))

    def printProfile(self):     # виведення значенн полів
        print("Driver:", self.name)
        print("  Aggression:", self.aggression)
        print("  Skill:", self.skill)
        print("  Mistake chance:", self.mistakeChance)
        print("  Overtaking risks:", self.overtakingRisk)
        
    def makeMistake(self):      # чи помилиться гонщик
        chance = self.mistakeChance * (1 - self.skill) * (0.8 + self.aggression * 0.2)
        return random.random() < chance

    def reactionTime(self):     # як швидко гощик реагує на події
        base_time = 0.3
        time = base_time - self.skill * 0.1 + self.aggression * 0.05
        return max(0.05, time)

    def adoptedToTrack(self, track):    # адаптація гонщика до треку, як змінюється поведінка гонщика залежно від траси
        self.mistakeChance += track.complexity * 0.1 + (1 - track.grip) * 0.1
        if self.mistakeChance > 1:
            self.mistakeChance = 1
