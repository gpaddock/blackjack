

class Player:
    def __init__(self, threshold):
        self.threshold = 18 + threshold
        if threshold > 18:
            self.personality = "Agressive"
        elif threshold == 17:
            self.personality = "Neutral"
        elif 15 < threshold < 17:
            self.personality = "Defensive"
        elif threshold <= 15:
            self.personality = "Passive"

