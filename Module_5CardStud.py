#!\Python33 python
#!\Pythin 3.4.3 Aug, 2016
"""Cardgame.py
Purpose: Five Card Evaluation Module
Developed by Robin Li robinli@live.

Assume the hand is sorted before evaluation.
"""
def Rank2Number(rank):
    i_rank=0
    if rank[0].upper() =='J':
        i_rank=11
    elif rank[0].upper() =='Q':
        i_rank=12
    elif rank[0].upper() =='K':
        i_rank=13
    elif rank[0].upper() =='A':
        i_rank=14
    elif rank[0].upper() =='1':
        i_rank=10
    else:
        i_rank=int(rank)
    return i_rank

## Any two cards of same rank
def IfOnePair(hand):
    msg="One Pair"
    max=hand[-1]
    if (hand[0][0]==hand[1][0]):
        rank=1
        max=hand[1]
    elif (hand[1][0]==hand[2][0]):
        rank=1
        max=hand[2]
    elif (hand[2][0]==hand[3][0]):
        rank=1
        max=hand[3]
    elif (hand[3][0]==hand[4][0]):
        rank=1
    else:
        rank=0
    return (rank,max,msg)

## Any two cards of same rank together with another two cards od same rank
def IfTwoPair(hand):
    msg="Three of A Kind"
    max=hand[-1]
    if (hand[0][0]==hand[1][0]):
        if (hand[2][0]==hand[3][0]):
            rank=2
            max=hand[3]
        elif (hand[3][0]==hand[4][0]):
            rank=2
        else:
            rank=0
    elif (hand[1][0]==hand[2][0] and hand[3][0]==hand[4][0]):
        rank=2
    else:
        rank=0
    return (rank,max,msg)

## Any three cards of the same rank
def If3ofAKind(hand):
    msg="Three of A Kind"
    max=hand[-1]
    if (hand[0][0]==hand[1][0] and hand[0][0]==hand[2][0]):
        rank=3
        max=hand[2]
    elif (hand[1][0]==hand[2][0] and hand[1][0]==hand[3][0]):
        rank=3
        max=hand[3]
    elif (hand[2][0]==hand[3][0] and hand[2][0]==hand[4][0]):
        rank=3
    else:
        rank=0
    return (rank,max,msg)

## Any five consecutive cards of different suits
def IfStraight(hand):
    msg="Straight"
    max=hand[-1]
    if (Rank2Number(hand[1][0])==Rank2Number(hand[0][0])+1 and \
        Rank2Number(hand[2][0])==Rank2Number(hand[1][0])+1 and \
        Rank2Number(hand[3][0])==Rank2Number(hand[2][0])+1 and \
        Rank2Number(hand[4][0])==Rank2Number(hand[3][0])+1): 
        rank=4
    elif (hand[0][0]=="2" and hand[1][0]=="3" and hand[2][0]=="4" and \
          hand[3][0]=="5" and hand[4][0]=="A"):
        rank=4
        max=hand[3]
    else:
        rank=0
    return (rank,max,msg)

## Any five cards of same suit (not consecutive)
def IfFlush(hand):
    msg="Flush"
    max=hand[-1]
    if (hand[0][-1]==hand[1][-1] and hand[0][-1]==hand[2][-1] and \
        hand[0][-1]==hand[3][-1] and hand[0][-1]==hand[4][-1]):
        rank=5
    else:
        rank=0
    return (rank,max,msg)

## Any three of same rank together any two cards of same rank
def IfFullHouse(hand):
    msg="Full House"
    max=hand[-1]
    if (hand[0][0]==hand[1][0] and hand[0][0]==hand[2][0] and \
        hand[3][0]==hand[4][0]): 
        rank=6
        max=hand[2]
    elif (hand[0][0]==hand[1][0] and hand[2][0]==hand[3][0] and \
        hand[2][0]==hand[4][0]):
        rank=6
    else:
        rank=0
    return (rank,max,msg)

## Any four cards of the same rank
def If4ofAKind(hand):
    max=hand[1]
    msg="Four of A Kind"
    if (hand[0][0]==hand[1][0] and hand[0][0]==hand[2][0] and \
        hand[0][0]==hand[3][0]): 
        rank=7
    elif (hand[1][0]==hand[2][0] and hand[1][0]==hand[3][0] and \
        hand[1][0]==hand[4][0]):
        rank=7
    else:
        rank=0
    return (rank,max,msg)

## Any Straight with all five cards of same suit
def IfStraightFlush(hand):
    max=hand[-1]
    msg="Four of A Kind"
    if (IfFlush(hand) and IfStraight(hand)): 
        rank=8
    else:
        rank=0
    return (rank,max,msg)

## Evaluate the hand
def EvaluateHand(hand):
    if (IfStraightFlush(hand)[0]==8):
        hand_value=IfStraightFlush(hand)
    elif (If4ofAKind(hand)[0]==7):
        hand_value=If4ofAKind(hand)
    elif (IfFullHouse(hand)[0]==6):
        hand_value=IfFullHouse(hand)
    elif (IfFlush(hand)[0]==5):
        hand_value=IfFlush(hand)
    elif (IfStraight(hand)[0]==4):
        hand_value=IfStraight(hand)
    elif (If3ofAKind(hand)[0]==3):
        hand_value=If3ofAKind(hand)
    elif (IfTwoPair(hand)[0]==2):
        hand_value=IfTwoPair(hand)
    elif (IfOnePair(hand)[0]==1):
        hand_value=IfOnePair(hand)
    else:
        hand_value=(0,hand[-1],"High Card")
    return hand_value
