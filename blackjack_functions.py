import random 

playing = True

class Deck:
	
	def __init__(self, suits, ranks):
		self.deck = []
		for suit in suits: 
			for rank in ranks: 
				card = Card(suit, rank)
				self.deck.append(card)

	def __str__(self): 
		pass  

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		return self.deck.pop() 

class Card:

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return f'{self.rank} of {self.suit}'

class Hand:

	values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11} 

	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self,card):
		self.cards.append(card)
		self.value = self.value + Hand.values[card.rank]
		
		if card.rank == 'Ace':
			self.aces = self.aces + 1

	def adjust_for_ace(self):
		self.value = self.value - 10

class Chips:

	def __init__(self):
		self.balance = 500; 

	def win_bet(self, bet_amt): 
		self.balance = self.balance + 2*bet_amt

	def lose_bet(self, bet_amt):
		self.balance = self.balance - bet_amt

def take_bet():
	while True:
		try: 
			bet_amt = int(input('Place a bet amount: '))
		except: 
			print("Please input a valid number.")
			continue
		else: 
			break 

	return bet_amt

def hit(deck, hand): 
	dealt_card = deck.deal()
	print(dealt_card)
	print('\n')
	hand.add_card(dealt_card)

	if hand.value > 21 and hand.aces > 1:
		hand.adjust_for_ace()

def hit_or_stand(deck, hand): 
	global playing 

	while playing:
		choice = input("Hit or Stand?\n")

		if choice.lower() == 'hit':
			hit(deck,hand)
		elif choice.lower() == 'stand':
			playing = False
		else: 
			print("Please enter either 'hit' or 'stand'.")

def show_some(player,dealer): 
	print("Player's cards:")
	for card in player.cards:
		print(card)
		
	print("Dealer's cards: ")	
	print(dealer.cards[0])
	print('Hidden\n')

def show_all(player,dealer):
	print("Player's cards:")
	for card in player.cards:
		print(card)
	print(f"Player amount: {player.value}")	

	print("Dealer's cards: ")	
	for card in dealer.cards:
		print(card)
	print(f"Dealer amount: {dealer.value}")

def player_busts(player_chips, bet_amt):
	player_chips.lose_bet(bet_amt)

def dealer_busts(player_chips, bet_amt):
	player_chips.win_bet(bet_amt)

def dealer_wins(player_chips, bet_amt):
	player_chips.lose_bet(bet_amt)

	

