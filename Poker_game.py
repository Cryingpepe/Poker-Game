class Cards:
    def __init__(self, shape, rank):
        self.shape = shape
        self.rank = rank
    
    def shape(self):
        return self.shape

    def rank(self):
        return self.rank
    
    def __str__(self):
        return shape + ', ' + ranks

# class Player:
#     hand = []
    
#     def __init__(self, ):
    
#     def 

Deck = []
shapes = ['\U00002660', '\U00002665', '\U00002663', '\U00002666']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
for i in shapes:
    for x in ranks:
        Deck.append(Cards(i,x))

# def draw():
print (Deck)
