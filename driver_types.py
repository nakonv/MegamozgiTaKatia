from driver import Driver
import random

class RookieDriver(Driver):         #
    def __init__(self, name, aggression, skill, mistakeChance, overtakingRisk):
        super().__init__(name, aggression, skill, mistakeChance, overtakingRisk)
        self.aggression *= 0.5
        self.skill *= 0.6

    def makeMistake(self):
        chance = self.makeMistake * (1 - self.skill) * (0.8 + self.aggression * 0.3)
        return random.random() < chance

class AggressiveDriver(Driver):       # 
    def __init__(self, name, aggression, skill, mistakeChance, overtakingRisk):
        super().__init__(name, aggression, skill, mistakeChance, overtakingRisk)
        self.aggression *= 1.5

    def makeMistake(self):
        chance = self.mistakeChance * (1 - self.skill) * (0.8 + self.aggression * 0.4)
        return random.random() < chance
    
class CauiousDriver(Driver):
    def __init__(self, name, aggression, skill, mistakeChance, overtakingRisk):
        super().__init__(name, aggression, skill, mistakeChance, overtakingRisk)
        self.aggression *= 0.5
        self.makeMistake *= 0.7

    def makeMistake(self):
        chance = self.mistakeChance * (1 - self.skill) * (0.6 + self.aggression * 0.2)
        return random.random() < chance

class ExperiencedDriver(Driver):
    def __init__(self, name, aggression, skill, mistakeChance, overtakingRisk):
        super().__init__(name, aggression, skill, mistakeChance, overtakingRisk)
        self.skill *= 1.2
        self.mistakeChance *= 0.5

    def  reactionTime(self):
        base_time = 0.25
        time = base_time - self.skill * 0.1 + self.aggression * 0.05
        return max(0.05, time)
    
    def makeMistake(self):
        chance = self.mistakeChance * (1 - self.skill) * (0.6 + self.aggression * 0.2)
        return random.random() < chance
    
class VeteranDriver(Driver):
    def __init__(self, name, aggression, skill, mistakeChance, overtakingRisk):
        super().__init__(name, aggression, skill, mistakeChance, overtakingRisk)
        self.aggression *= 0.7
        self.skill *= 0.9
        self.mistakeChance *= 1.2

    def reactionTime(self):
        base_time = 0.35
        time = base_time - self.skill * 0.1 + self.aggression * 0.05
        return max(0.1, time)
    
    def makeMistake(self):
        chance = self.mistakeChance * (1 - self.skill) * (0.8 + self.aggression * 0.3)
        return random.random() < chance
