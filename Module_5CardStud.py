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
    if (hand[0][0]==hand[1][0]):
        return True
    elif (hand[1][0]==hand[2][0]):
        return True
    elif (hand[2][0]==hand[3][0]):
        return True
    elif (hand[3][0]==hand[4][0]):
        return True
    else:
        return False

## Any two cards of same rank together with another two cards od same rank
def IfTwoPair(hand):
    if (hand[0][0]==hand[1][0]):
        if (hand[2][0]==hand[3][0]):
            return True
        elif (hand[2][0]==hand[4][0]):
            return True
        elif (hand[3][0]==hand[4][0]):
            return True
        else:
            return False
    elif (hand[1][0]==hand[2][0] and hand[3][0]==hand[4][0]):
        return True
    else:
        return False

## Any three cards of the same rank
def If3ofAKind(hand):
    if (hand[0][0]==hand[1][0]):
        if (hand[0][0]==hand[2][0]):
            return True
        elif (hand[0][0]==hand[3][0]):
            return True
        elif (hand[0][0]==hand[4][0]):
            return True
        else:
            return False
    elif (hand[1][0]==hand[2][0]):
        if (hand[1][0]==hand[3][0]):
            return True
        elif (hand[1][0]==hand[4][0]):
            return True
        else:
            return False
    elif (hand[2][0]==hand[3][0]):
        if (hand[2][0]==hand[4][0]):
            return True
        else:
            return False
    else:
        return False

## Any five consecutive cards of different suits
def IfStraight(hand):
    if (Rank2Number(hand[1][0])==Rank2Number(hand[0][0])+1 and \
        Rank2Number(hand[2][0])==Rank2Number(hand[1][0])+1 and \
        Rank2Number(hand[3][0])==Rank2Number(hand[2][0])+1 and \
        Rank2Number(hand[4][0])==Rank2Number(hand[3][0])+1): 
        return True
    elif (hand[0][0]=="2" and hand[1][0]=="3" and hand[2][0]=="4" and \
          hand[3][0]=="5" and hand[4][0]=="A"):
        return True
    else:
        return False
    return

## Any five cards of same suit (not consecutive)
def IfFlush(hand):
    if (hand[0][-1]==hand[1][-1] and hand[0][-1]==hand[2][-1] and \
        hand[0][-1]==hand[3][-1] and hand[0][-1]==hand[4][-1]):
        return True
    else:
        return False

## Any three of same rank together any two cards of same rank
def IfFullHouse(hand):
    if (hand[0][0]==hand[1][0] and hand[0][0]==hand[2][0] and \
        hand[3][0]==hand[4][0]): 
        return True
    elif (hand[0][0]==hand[1][0] and hand[2][0]==hand[3][0] and \
        hand[2][0]==hand[4][0]):
        return True
    else:
        return False
    return

## Any four cards of the same rank
def If4ofAKind(hand):
    if (hand[0][0]==hand[1][0] and hand[0][0]==hand[2][0] and \
        hand[0][0]==hand[3][0]): 
        return True
    elif (hand[1][0]==hand[2][0] and hand[1][0]==hand[3][0] and \
        hand[1][0]==hand[4][0]):
        return True
    else:
        return False

## Any Straight with all five cards of same suit
def IfStraightFlush(hand):
    if (IfFlush(hand) and IfStraight(hand)): 
        return True
    else:
        return False

## Evaluate the hand
def EvaluateHand(hand):
    max=hand[-1]
    msg=" Card Rank Message"
    if (IfStraightFlush(hand)):
        rank=8
        msg="Straight Flush"
    elif (If4ofAKind(hand)):
        rank=7
        msg="Four of A Kind"
    elif (IfFullHouse(hand)):
        rank=6
        msg="Full House"
    elif (IfFlush(hand)):
        rank=5
        msg="Flush"
    elif (IfStraight(hand)):
        rank=4
        msg="Straight"
    elif (If3ofAKind(hand)):
        rank=3
        msg="Three of A Kind"
    elif (IfTwoPair(hand)):
        rank=2
        msg="Two Pair"
    elif  (IfOnePair(hand)):
        rank=1
        msg="One Pair"
    else:
        rank=0
        msg="High Card"
    return (rank,max,msg)
