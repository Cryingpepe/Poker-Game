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
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.currentcoin = 0
        
    def name(self):
        return self.name
    
    def draw(self, num):
        for i in range(num):
            self.hand.append(Deck.pop(random.randrange(1,len(Deck)+1)))
    
    def coin(self, coin):
        self.currentcoin += coin

    def hand(self):
        return self.hand

def settingDeck():
    global Deck
    shapes = ['\U00002660', '\U00002665', '\U00002663', '\U00002666']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    Deck = []

    for i in shapes:
        for x in ranks:
            Deck.append(Cards(i,x))

def startingGame(listofplayer):
    for i in listofplayer:
        i.draw(5)
        

def main():
    global Playerlist
    Playerlist = []
    settingDeck()
    numofnotPlayer = int(input('Number of computer: '))
    for i in range(numofnotPlayer): # + name setting plz
        Playerlist.append(Player('Player'+str(i)).name)
    NameofPlayer = input('your Name: ')
    Playerlist.append(Player(NameofPlayer))
