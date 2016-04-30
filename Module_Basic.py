#!\Python33 python
#!\Pythin 3.4.3 Aug, 2016
"""Cardgame.py
Purpose: Basic Card Game Setting Python script
Developed by Robin Li robinli@live.
Rank: 1(Ace),2,3,4,5,6,7,8,9,10,11(Jack),12(Queen),13(King)
Suite: C(Clubs), D(Diamonds), H(Hearts), and S(Spades)
"""

import random

def ShortRank(rank):
    rank=str(rank)
    if rank == '11':
        return 'J'
    elif rank == '12':
        return 'Q'
    elif rank == '13':
        return 'K'
    elif rank == '14':
        return 'A'
    else:
        return rank

def RankName(i_rank):
    rank=ShortRank(i_rank)
    if rank[0].upper() =='J':
        return 'Jack'
    elif rank[0].upper() =='Q':
        return 'Queen'
    elif rank[0].upper() =='K':
        return 'King'
    elif rank[0].upper() =='A':
        return 'Ace'
    else:
        return rank

def SuitName(i_suit):
    suit=str(i_suit)
    if suit=='1' or suit[0].upper() =='C':
        return 'Clubs'
    elif suit=='2' or suit[0].upper() =='D':
        return 'Diamonds'
    elif suit=='3' or  suit[0].upper() =='H':
        return 'Hearts'
    elif suit=='4' or suit[0].upper() =='S':
        return 'Spades'
    else:
        return suit

def ShuffleDeck(deck):
    random.shuffle(deck)
    return deck

def MergeDeck(deck,hand):
##    deck=deck+hand
##    hand=[]
    while (len(hand)>0):
        deck.append(hand[-1])
        hand.pop(-1)
    return deck,hand

def DrawCard(deck,hand):
    if len(deck)<11:
        print ("\t ***  Not enough cards in the deck, please reset the deck !\n\n")
    else:
        random_index=random.randint(1,len(deck))
        hand.append(deck[random_index-1])
        deck.pop(random_index-1)
    return deck,hand
