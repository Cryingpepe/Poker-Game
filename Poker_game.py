class Cards:
    shapes = ['\U00002660', '\U00002665', '\U00002663', '\U00002666']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, shape, rank):
        self.shape = shape
        self.rank = rank
    
    def shape(self):
        return self.shape

    def rank(self):
        return self.rank
    
    def __str__(self):
        return self.shape, self.ranks

class Hand:
    hand = []

    def draw(self):

Deck = []

for i in range(4):
    for x in range(13):
        Deck.append([Cards.shapes[i],Cards.ranks[x]])
