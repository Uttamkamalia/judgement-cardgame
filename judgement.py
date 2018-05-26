from Deck import Deck
from Card import Card, Suit, Rank
from Player import Player
from random import randint

'''
Suit identification (iden)
0: clubs
1: diamonds
2: spades
3: hearts

The suit that leads is trump, aces are high
'''

class Scoreboard:
    def __init__(self,num):
        self.score = []
        for i in range(0,num):
            self.score.insert(0,0)
    def showScore(self):
        print "Score board indexwise is:"
        print self.score
    def updateScore(self,index,val):
        self.score[index]+=val
    def displayWinner(self):
        return self.score.index(max(self.score))

class Judgement:
    def __init__(self):
        self.dealer = -1
        #self.players = [Player("Danny",0), Player("Desmond",1), Player("Ben",2), Player("Tyler",3)]
        self.players=self.getPlayers()
        #self.players = [Player("Danny",0), Player("Desmond",1)]
        self.score = Scoreboard(len(self.players))
        self.trump = randint(0,3)
        self.NumGames = 1#52/len(self.players)
        self.gameNo = self.NumGames
        while self.NumGames != 0:
            self.newGame()
            self.NumGames = self.NumGames-1
            self.gameNo = self.gameNo-1
        self.showWinner()

    def showWinner(self):
        print "Winner is "+str(self.players[self.score.displayWinner()].name)

    def getPlayers(self):
        NumPlayers = raw_input("Enter Number of Players:")
        players = []
        for i in range(0,int(NumPlayers)):
            name = raw_input("Enter Name of the Player ")
            players.append(Player(name,i))
        return players

    def newGame(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.dealer = (self.dealer + 1) % len(self.players)
        self.dealCards()
        self.Show()
        self.startplayer=self.dealer
        claim =self.getClaim()
        Gamescore=[]
        for i in range(0, len(self.players)):
                Gamescore.insert(0,0);
        for i in range(0,self.gameNo):
            self.startplayer=self.newRound()
            Gamescore[self.startplayer]+=1
        self.UpdateScoreboard(claim,Gamescore)

    def UpdateScoreboard(self,claim,Gscore):
        for i in range(0, len(self.players)):
                if(int(claim[i])==Gscore[i]):
                    if(Gscore[i]==0):
                        self.score.updateScore(i,10)
                        continue
                    self.score.updateScore(i,int(claim[i])*10+int(claim[i]))
        self.Show()

    def dealCards(self):
        cardsDealt = self.gameNo*len(self.players)
        i=0
        while cardsDealt != 0:
            self.players[i % len(self.players)].addCard(self.deck.deal())
            i += 1
            cardsDealt=cardsDealt-1

    def getClaim(self):
        claim=[]
        for i in range(0, len(self.players)):
                claim.insert(0,0);
        for i in range(1, len(self.players)+1):
            claim[(self.dealer + i) % len(self.players)] = raw_input("Enter Cliam for "+str(self.players[(self.dealer + i) % len(self.players)].name)+str((self.dealer + i) % len(self.players))+" ")
        return claim

    def Show(self):
        for p in self.players:
            print p.name+str(p.playerNum)+":",
            print p.hand
        print "The trump is "+str(self.trump)+"\n0: clubs\n1: diamonds\n2: spades\n3: hearts"
        self.score.showScore()
    def getWinner(self,round,lsuit):
        win = round[len(self.players)-1]
        tflag=0
        if(win[0].suit.iden==self.trump):
            tflag=1
        for card in round:
            if(card[0].suit.iden==self.trump):
                if(tflag==1):
                    if(card[0]>win[0]):
                        win=card
                    else:
                        continue
                else:
                    tflag=1
                    win=card
            else:
                if(tflag==1):
                    continue
                else:
                    if(card[0].suit.string==lsuit):
                        if(card[0]>win[0]):
                            win=card
                        else:
                            continue
                    else:
                        continue
        print "Player "+str(win[1])+" won the hand!"
        return win[1]

    def newRound(self):
        round = []
        suit = ""

        for i in range(0, len(self.players)):
            while True:
                res=self.players[(self.startplayer + i) % len(self.players)].play()
                if(i==0):
                    suit=res.suit.string
                    round.insert(0,[res,self.players[(self.startplayer + i) % len(self.players)].playerNum])
                    break
                if(res.suit.string==suit):
                    round.insert(0,[res,self.players[(self.startplayer + i) % len(self.players)].playerNum])
                    break
                else:
                    if(self.players[(self.startplayer + i) % len(self.players)].hand.hasCardofSuit(suit)):
                        print "play the right move!"
                        self.players[(self.startplayer + i) % len(self.players)].hand.addCard(res)
                        print self.players[(self.startplayer + i) % len(self.players)].name
                        print self.players[(self.startplayer + i) % len(self.players)].hand

                        continue
                    else:
                        round.insert(0,[res,self.players[(self.startplayer + i) % len(self.players)].playerNum])
                        break
        return self.getWinner(round,suit)



def main():

    judgement = Judgement()


if __name__ == '__main__':
	main()
