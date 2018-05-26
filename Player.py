from Hand import Hand
from Card import Card,Suit

class Player:

	def __init__(self, name, no):
			self.name = name
			self.hand = Hand()
			self.playerNum=no
			self.score = 0
			self.tricksWon = []

	def addCard(self, card):
		self.hand.addCard(card)


	def getInput(self, option):
		card = None
		while card is None:
			card = raw_input(self.name + ", select a card to " + option + ": ")
		return card

	def play(self):
		input = raw_input(self.name)
		rank=Hand.strToCard(input)[0]
		suit=Hand.strToCard(input)[1]
		card=Card(rank,suit)
		self.removeCard(card)
		return card
	def clearCards(self):
		self.hand = Hand()


	def trickWon(self, trick):
		self.score += trick.points


	def hasSuit(self, suit):
		return len(self.hand.hand[suit.iden]) > 0

	def removeCard(self, card):
		self.hand.removeCard(card)

	def discardTricks(self):
		self.tricksWon = []

	def hasOnlyHearts(self):
		return self.hand.hasOnlyHearts()
