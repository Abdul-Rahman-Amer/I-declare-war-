import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)
    
    def deal_card(self):
        return self.cards.pop()
    
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
    
    def play_card(self):
        return self.cards.pop(0)
    
    def add_cards(self, new_cards):
        self.cards += new_cards
    
    def has_cards(self):
        return bool(self.cards)
    
class Game:
    def __init__(self, player1_name, player2_name):
        self.deck = Deck()
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        
    def play(self):
        # deal cards to each player
        for i in range(26):
            self.player1.add_cards([self.deck.deal_card()])
            self.player2.add_cards([self.deck.deal_card()])
        
        # play the game until one player runs out of cards
        round_num = 1
        while self.player1.has_cards() and self.player2.has_cards():
            print(f"\nRound {round_num}")
            print(f"{self.player1.name} plays {self.player1.cards[0]}")
            print(f"{self.player2.name} plays {self.player2.cards[0]}")
            if self.player1.cards[0].rank > self.player2.cards[0].rank:
                print(f"{self.player1.name} wins the round!")
                self.player1.add_cards([self.player1.play_card(), self.player2.play_card()])
            elif self.player1.cards[0].rank < self.player2.cards[0].rank:
                print(f"{self.player2.name} wins the round!")
                self.player2.add_cards([self.player1.play_card(), self.player2.play_card()])
            else:
                print("War!")
                war_cards = []
                for i in range(3):
                    if self.player1.has_cards() and self.player2.has_cards():
                        war_cards.append(self.player1.play_card())
                        war_cards.append(self.player2.play_card())
                if self.player1.has_cards():
                    war_cards.append(self.player1.play_card())
                if self.player2.has_cards():
                    war_cards.append(self.player2.play_card())
                random.shuffle(war_cards)
                self.player1.add_cards(war_cards[:len(war_cards)//2])
                self.player2.add_cards(war_cards[len(war_cards)//2:])
            round_num += 1
        
        # determine the winner
        if self.player1.has_cards():
            print(f"\n{self.player1.name} wins the game!")
        else:
            print(f"\n{self.player2.name} wins the game!")
