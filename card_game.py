
from random import shuffle


class CardsGame():
    def __init__(self):
        self.cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'J', 'Q']
        self.suits = ['H', 'S', 'C', 'D']
        self.card_suit = [card + suit for card in self.cards for suit in self.suits]
        print self.card_suit


    def shuffle(self):
        shuffle(self.card_suit)


if  __name__=="__main__":
    card_game_obj = CardsGame()
    card_game_obj.shuffle()
