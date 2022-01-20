import random

class Deck:
	suite = {0: 'Spades', 1:'Hearts', 2:'Clubs', 3:'Diamonds', 4: 'Spades' }
	cards_point = {1 :1 , 2: 2 , 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11:11, 12:12, 0:13}

	def __init__(self):
		self.cards = list(range(1,53))
		random.shuffle(self.cards)

	def pick_a_card(self):
		while self.cards:	
			picked_card = self.cards.pop()
			picked_suite = Deck.suite[int(picked_card // 13)]
			picked_point = Deck.cards_point[int(picked_card % 13)]		
			return picked_suite , picked_point


class Player(Deck):
	
	cards_value = {1 :1 , 2: 2 , 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11:10, 12:10, 13:10}
	def __init__(self,name, card= None, value = 0):
		super().__init__()
		self.name = name
		if not card:
			card = []
		self.card = card
		self.value = value
		
	def add_card(self, card):
		self.card.append(card)
		self.value += Player.cards_value[card] 
		
	def winning_prob(self, cards):
		self.cards = cards
		#print(len(self.cards),self.cards)
		#for unseen_card in self.cards:
		#	print(unseen_card, int(unseen_card % 13),Deck.cards_point[int(unseen_card % 13)] )
		return sum(Deck.cards_point[int(unseen_card % 13)] < ( 21 - self.value ) for unseen_card in self.cards) / len(self.cards)


cards = Deck()

run = 0
p1 = Player('dealer')
p2 = Player('player')
#print(p1.winning_prob(cards.cards))
#print(p2.winning_prob(cards.cards))
while run <= 10:
	run +=1
	p1.add_card(cards.pick_a_card()[1]) 
	print(f"Run:{run}")
	print(f"{p1.name} got {p1.card} with total value {p1.value}; the prob of winning: {float(sum(Deck().cards_point[int(card % 13)] < 21-p1.value for card in cards.cards)/len(cards.cards))}")
	print(f"the prob of winning: {p1.winning_prob(cards.cards)}")
	p2.add_card(cards.pick_a_card()[1]) 
	print(f"{p2.name} got {p2.card} with total value {p2.value}")
	print(f"the prob of winning: {p2.winning_prob(cards.cards)}")
        
	if p1.value > 21 or p2.value >21:
		print("Game Over!")
		break
