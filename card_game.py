from random import shuffle


class CardsGame():
    def __init__(self):
        self.cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'J', 'Q']
        self.suits = ['H', 'S', 'C', 'D']
        self.card_suit = [card + suit for card in self.cards for suit in self.suits]

    def shuffle(self):
        shuffle(self.card_suit)

    def card_distribute(self, player_count=5, card_count=13):
        # if card_count == 13:
        hand_deck_list = []
        self.hands = [self.card_suit[i::player_count] for i in range(0, player_count)]
        max_card_per_person = len(self.card_suit) / player_count

        # import pdb;pdb.set_trace()
        for per_hand in self.hands:
            hand_deck_list.append(per_hand[:max_card_per_person:])
        print hand_deck_list


if  __name__=="__main__":
    card_game_obj = CardsGame()
    card_game_obj.shuffle()
    card_game_obj.card_distribute()
