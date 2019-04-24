from random import shuffle


class CardsGame():
    def __init__(self, player_count, card_count):
        self.cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'J', 'Q']
        self.suits = ['H', 'S', 'C', 'D']
        self.card_suit = [card + suit for card in self.cards for suit in self.suits]
        self.player_count = player_count
        self.card_count = card_count

    def shuffle(self):
        shuffle(self.card_suit)

    def card_distribute(self):
        self.hands = [self.card_suit[i::self.player_count] for i in range(0, self.player_count)]

        max_card_per_person = len(self.card_suit) / self.player_count if self.card_count == 13 else self.card_count

        self.hands = [per_hand[:max_card_per_person:] for per_hand in self.hands]
        return self.hands

    def player_card_info(self):
        count = 0
        deck_dict = {}
        for hand in self.hands:
            count += 1
            key = '%s%s' % ('P', count)
            deck_dict[key] = hand
        self.player_deck_info = deck_dict


if  __name__=="__main__":
    player_count = int(raw_input("How many players:"))
    card_decision = raw_input("Do you want to chose the card per persont Y/N:").upper()
    card_count = int(raw_input("Cards per player:")) if card_decision == 'Y' else 13

    card_game_obj = CardsGame(player_count, card_count)
    card_game_obj.shuffle()
    card_game_obj.card_distribute()
    card_game_obj.player_card_info()
    print card_game_obj.player_deck_info
