# Build a card games. 


# Qu'est ce que je peux faire ? 

# Créer des cartes
# Créer un deck 
# Avec ce deck affronter un autre deck. 
# On peut juste faire une bataille. 
# La carte la plus forte l'emporte
# Jusqu'a ce que la derniere carte du paquet sois utilisé. 
# Je peux meme creer un deck random de 10 cartes. 

# Juste creer un battle deck de 5 cartes et c'est tout . 

# Logique des cartes 

# Spades	↦	3
# Hearts	↦	2
# Diamonds	↦	1
# Clubs	↦	0

# Jack	↦	11
# Queen	↦	12
# King	↦	13"


import random


# Créer des cartes. 

class Card(): 
    ### Representons des cartes. 
    # In order to print Card objects in a way that people can easily read, we need a mapping 
    # from the integer codes to the corresponding ranks and suits.
    # A natural way to do that is with lists of strings. We assign these lists to class attributes:
    suit_names = [ "Club", "Diamonds", "Hearts", "Spades"]
    rank_name = [ None, "Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]



    def __init__(self, suit=0, rank=2):
        self.suit = suit 
        self.rank = rank
    
    def __str__(self) -> str:
      
        return f' The suit is {Card.suit_names[self.suit]} and the rank is {Card.rank_name[self.rank]}'

    #  Compare the cards   
    #  __lt__, which stands for “less than”. 
    #  suits is more important, 

    def __lt__(self, other): 
        if self.suit > other.suit : 
            return False 
        if self.suit < other.suit : 
            return True

        return self.ranks < other.ranks

   
class Deck: 
    
    def __init__(self) -> None:
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14): 
                card = Card(suit, rank)
                self.cards.append(card)

    # inside class Deck:

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    

    def pop_card(self):
        return self.cards.pop()
    
    def add_card(self, card): 
        self.cards.append(card)


    def sort(self): 
        self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    
    def deal_hands(self, hand_player, card):


        pass


class Hand(Deck): 
    """Represents a hand of playing cards."""
    
    def __init__(self, label=''):
        self.cards = []
        self.label = label

        
    def deal_hands(self, hand_player, card):
        

        pass
# Écrivez une méthode Deck appelée deal_hands qui prend deux paramètres, 
# le nombre de mains et le nombre de cartes par main. 
# Elle doit créer le nombre approprié d'objets Hand,
#  distribuer le nombre approprié de cartes par main et renvoyer une liste de Hands.


hand = Hand('New Hand')
print(hand.cards)

deck = Deck()
card = deck.pop_card()
hand.add_card(card)
print(hand)

toto = hand.move_cards(deck, 1)
print(toto)