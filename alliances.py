from typing import List
import random

class Alliences:
    def __init__(self, size=7):
        self.size = size
        self.players = []
    
    def get_allies(self, player: int) -> List[int]:
        """Return list of allies for player"""
        assert player >= 0 and player < self.size
        
        position = self.players.index(player)
        allies = [self.players[position - 1]]
        if position == self.size - 1:
            allies.append(self.players[0])
        else:
            allies.append(self.players[position + 1])
        return allies
    
    def generate(self):
        self.players = list(range(self.size))
        random.shuffle(self.players)