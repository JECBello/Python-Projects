import blackjack_functions

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

playing = True
running = True

while running: 
	print("Welcome to BlackJack!")

	player = blackjack_functions.Hand()
	dealer = blackjack_functions.Hand()
	game_deck = blackjack_functions.Deck(suits,ranks)

	print("The deck will now be shuffled")
	game_deck.shuffle()

	print("Two cards will now be dealt to each player.")
	dealt_card1 = game_deck.deal()
	dealt_card2 = game_deck.deal()
	player.add_card(dealt_card1)
	player.add_card(dealt_card2)

	dealt_card3 = game_deck.deal()
	dealt_card4 = game_deck.deal()
	dealer.add_card(dealt_card3)
	dealer.add_card(dealt_card4)

	print("You will begin with $500")
	player_chips = blackjack_functions.Chips()

	bet_amt = blackjack_functions.take_bet()
	blackjack_functions.show_some(player,dealer)

	while blackjack_functions.playing:
		blackjack_functions.hit_or_stand(game_deck, player)
		if player.value > 21:
			print("You bust!")
			blackjack_functions.player_busts(player_chips, bet_amt)


	while dealer.value < player.value:
		blackjack_functions.hit(game_deck, dealer) 

	blackjack_functions.show_all(player, dealer) 

	if dealer.value > 21:
		blackjack_functions.dealer_busts(player_chips, bet_amt)
	elif dealer.value > player.value: 
		blackjack_functions.dealer_wins(player_chips, bet_amt)
	elif dealer.value == player.value:
		print("It's a tie!") 

	print(f"Player balance: {player_chips.balance}")

	
	while running:
		again = input("Would you like to play again? Yes or no?\n")
		if again.lower() == 'yes':
			break 
		elif again.lower() == 'no':
			running = False
		else: 
			print("Please enter yes or no.")


	



