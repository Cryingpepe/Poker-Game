import random

class Cards:
    def __init__(self, shape, rank):
        self.shape = shape
        self.rank = rank
    
    def shape(self):
        return self.shape

    def rank(self):
        return self.rank
    
    def __repr__(self):
        return self.shape + ' ' + self.rank

class Player:
    hand = []
    shapes = ['\U00002660', '\U00002665', '\U00002663', '\U00002666']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    Deck = []

    for i in shapes:
        for x in ranks:
            Deck.append(Cards(i,x))

    def __init__(self, num):
        self.num = num

    def draw(self, num):
        for i in range(num):
            hand.append(Deck.pop(random.randrange(1,len(Deck)+1)))
