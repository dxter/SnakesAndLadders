import numpy

# https://boardgamegeek.com/image/207990/giant-game-board-book


class SnakesAndLadders:
    """ a class for SnakesAndLadders parameters to calculate Q matrix and expected number of dice rolls"""
    
    def __init__(self, width: int, height: int, snakes: list, ladders: list, diceSize=6) -> None:
        self.width = width
        self.height = height
        self.dicesize = diceSize
        
        self.states = [i for i in range(self.width * self.height) if (i not in [s[0] for s in snakes]) and (i not in [l[0] for l in ladders])]

        self.transitionMatrix = self.createTransitionMatrix(self.states, snakes, ladders)

    def createTransitionMatrix(self, states: list, snakes: list, ladders: list) -> numpy.array:
        matrix = numpy.array([])
        for row in states:
            validStates = [r for r in range(row + 1, row + 1 + self.dicesize) if r in states]
            

        return matrix


if __name__ == '__main__':
    
    snakes = [(8,2)]
    ladders = [(4,7)]
    pici = SnakesAndLadders(3,3,snakes, ladders)
    print(pici.states)