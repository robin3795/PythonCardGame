#!\Python33 python
#!\Pythin 3.4.3 Aug, 2016
"""Cardgame.py
Purpose: Five Card Evaluation Module
Developed by Robin Li robinli@live.

Assume the hand is sorted before evaluation.
"""

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
    elif (hand[1][0]==hand[2][0]):
        if (hand[3][0]==hand[4][0]):
            return True
        else:
            return False
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
    return

## Any five cards of same suit (not consecutive)
def IfFlush(hand):
    return

## Any three of same rank together any two cards of same rank
def IfFullHouse(hand):
    return

## Any four cards of the same rank
def If4ofAKind(hand):
    if (hand[0][0]==hand[1][0]):
        if (hand[0][0]==hand[2][0]):
            if (hand[0][0]==hand[3][0]):
                return True
            elif (hand[0][0]==hand[4][0]):
                return True
            else:
                return False
        else:
            return False
    elif (hand[1][0]==hand[2][0]):
        if (hand[1][0]==hand[3][0]):
            if (hand[1][0]==hand[4][0]):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

## Any Straight with all five cards of same suit
def IfStraightFlush(hand):
    if (IfFlush(hand)):
        if (IfStraight(hand)): 
            return True
        else:
            return False
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
