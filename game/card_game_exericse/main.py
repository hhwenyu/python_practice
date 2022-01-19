import random


class Player:
	
	def __init__(self,name:str,deck = 10):
		self.name = name
		self.points = 0
		self.cards = list(range(1,deck +1 ,1))
		self.won_score = (deck //2) +1
		random.shuffle(self.cards) ## this will automatically shuffle the cards and in replace the list


	def pick_card(self):
		while self.cards:
			picked_card = self.cards.pop()
			print(f"{self.name} got an {picked_card}")
			return picked_card


	def add_point(self):
		self.points += 1
		print(f"A point has been added to {self.name}")
		return self.points

	def is_game_over(self):
		return (not self.cards) or (self.points >= self.won_score)

p1 = Player(name="Player 1")
p2 = Player(name="Player 2")

## game
print("Game starts..")
while True:
	input("Press Enter to pick a card!")
	p1_card = p1.pick_card()
	p2_card = p2.pick_card()
	if p1_card > p2_card:
		p1.add_point()
	elif p2_card > p1_card:
		p2.add_point()
	else:
		print("TIE") 
	if p1.is_game_over() or p2.is_game_over():
		print("Game over!")
		if p1.points > p2.points:
			print(f"{p1.name} wins")
		elif p2.points > p1.points:
			print(f"{p2.name} wins")
		else:
			print("score is tie")

		print(f"score: {p1.points} vs {p2.points}")

		break
		
	
