from random import shuffle


class CardsGame():
    def __init__(self):
        self.cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'J', 'Q']
        self.suits = ['H', 'S', 'C', 'D']
        self.card_suit = [card + suit for card in self.cards for suit in self.suits]
        # self.player_count = player_count
        # self.cardcount

    def shuffle(self):
        shuffle(self.card_suit)

    def card_distribute(self, player_count=4, card_count=6):
        self.hands = [self.card_suit[i::player_count] for i in range(0, player_count)]

        max_card_per_person = len(self.card_suit) / player_count if card_count == 13 else card_count

        self.hands = [per_hand[:max_card_per_person:] for per_hand in self.hands]
        return self.hands


if  __name__=="__main__":
    card_game_obj = CardsGame()
    card_game_obj.shuffle()
    card_game_obj.card_distribute()
    print card_game_obj.hands
