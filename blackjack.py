#bjShuffleStart.py
#mcvan
#16/Sept/14

from random import *
import pygame, os, sys

DECKS = 1
playerHand = []
dealerHand = []
dealerScore = 0
playerScore = 0

font = pygame.font.SysFont("comicsansms", 72)
pygame.font.init()
win = font.render("You Win!", 1, (255,255,0))
lose = font.render("You Lose",1, (255,255,255))

CARDPOINTS = {'AD': 11, 'AH': 11, 'AC': 11, 'AS': 11,
              'KD': 10, 'KH': 10, 'KC': 10, 'KS': 10,
              'QD': 10, 'QH': 10, 'QC': 10, 'QS': 10,
              'JD': 10, 'JH': 10, 'JC': 10, 'JS': 10,
              '2D':  2, '2H':  2, '2C':  2, '2S':  2,
              '3D':  3, '3H':  3, '3C':  3, '3S':  3,
              '4D':  4, '4H':  4, '4C':  4, '4S':  4,
              '5D':  5, '5H':  5, '5C':  5, '5S':  5,
              '6D':  6, '6H':  6, '6C':  6, '6S':  6,
              '7D':  7, '7H':  7, '7C':  7, '7S':  7,
              '8D':  8, '8H':  8, '8C':  8, '8S':  8,
              '9D':  9, '9H':  9, '9C':  9, '9S':  9,
              '10D': 10, '10H': 10, '10C': 10, '10S':10}


def cardList():

    cards  =  ['AD', 'AH', 'AC', 'AS',
               'KD', 'KH', 'KC', 'KS',
               'QD', 'QH', 'QC', 'QS',
               'JD', 'JH', 'JC', 'JS',
               '2D', '2H', '2C', '2S',
               '3D', '3H', '3C', '3S',
               '4D', '4H', '4C', '4S',
               '5D', '5H', '5C', '5S',
               '6D', '6H', '6C', '6S',
               '7D', '7H', '7C', '7S',
               '8D', '8H', '8C', '8S',
               '9D', '9H', '9C', '9S',
               '10D', '10H', '10C', '10S'] * DECKS

    NUMCARDS = len(cards)

    shuffled_cards = []

    for i in range(NUMCARDS):
        
        cardCount = randrange(0,(NUMCARDS - i))
        shuffled_cards.append(cards[cardCount])
        del cards[cardCount]
                  
    return shuffled_cards

shuffledCards = cardList()

def startHandPlayer(shuffledDeck):
    playersCards = []
    playersScore = 0
    
    newCard = shuffledDeck.pop(0)
    playersCards.append(newCard)
    playersScore += CARDPOINTS[newCard]
    
    newCard = shuffledDeck.pop(0)
    playersCards.append(newCard)
    playersScore += CARDPOINTS[newCard]
    
    #playersScore = checkAces(playersScore, playersCards)
    print("Player's cards: ", playersCards, " Player's hand score ", playersScore)

    return (playersScore, playersCards)

def ace(score):
        if score > 10:
            return 1
        else:
            return 11

def score(hand):
    score = 0
    for card in hand:
        cardpoint = CARDPOINTS.get(card)
        if cardpoint == 11:
            score += ace(score)
        else:
            score += cardpoint
    return score

def startPlayer(deck):
    hit(deck)
    hit(deck)
    addCard(dealerHand,shuffledCards)
    addCard(dealerHand,shuffledCards)

def getCard(tempDeck):
        card = choice(tempDeck)
#        tempDeck.remove(choice)
        return card

def addCard(hand, tempDeck):
    hand.append(getCard(tempDeck))

def hit(deck):
    addCard(playerHand,deck)
    score(playerHand)
    score(dealerHand)

def dealerTurn(deck):
    addCard(dealerHand,deck)

def checkWin(screen):
    dealerScore = score(dealerHand)
    playerScore = score(playerHand)
    if dealerScore > 21:
        screen.blit(win,(100,300))
    if playerScore > 21:
        screen.blit(lose,(100,300))
    if dealerScore > playerScore:
        print ("You lose")

#graphics
pygame.display.set_caption("Get to the red square!")
screen = pygame.display.set_mode((1000, 600))

while True:
    pygame.font.init()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
        if (e.type==pygame.KEYDOWN):
            if e.key==pygame.K_h:
                addCard(playerHand,shuffledCards)
                if dealerScore < 17:
                    addCard(dealerHand,shuffledCards)
                    print (dealerHand)
                print (playerHand)
                checkWin()
            if e.key==pygame.K_t:
                hit(shuffledCards)
                addCard(dealerHand,shuffledCards)
                print (playerHand)
                print (dealerHand)
                checkWin()
            if e.key==pygame.K_r:
                startPlayer(shuffledCards)
                playerScore = 0
                dealerScore = 0
                checkWin()
            if e.key==pygame.K_s:
                startPlayer(shuffledCards)
                print (playerHand)
                print (dealerHand)
                print (score(playerHand))
#                if playerScore == 21

#                cardPlayer = pygame.image.load(("card/"+dealerHand[0]+".png"),(10,10))

#    cardPlayer = pygame.image.load(("card/"+dealerHand[0]+"png"),10,10)
#    cardDealer = pygame.image.load("dealer.jpg")

    screen.fill((255, 0, 0))
#    screen.blit(cardPlayer, (10,10))
    x=0
    for card in playerHand:
        x+=1
        temp = pygame.image.load("card/"+card+".png")
        screen.blit(temp, (72*x,10))
    y=0
    for card in dealerHand:
        y+=1
        temp = pygame.image.load("card/"+card+".png")
        screen.blit(temp, (72*y,200))
    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    # Draw the scene

    pygame.display.flip()
