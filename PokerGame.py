#!\Python33 python
#!\Pythin 3.4.3 Aug, 2015
"""Cardgame.py
Purpose: Python script for XXXX Interview May 2013 initially
Developed by Robin Li robinli@live.
Rank: 1(Ace),2,3,4,5,6,7,8,9,10,11(Jack),12(Queen),13(King)
Suite: C(Clubs), D(Diamonds), H(Hearts), and S(Spades)

Release Note:
V0: introduce Module_Basic
"""

import Module_Basic
import Module_5CardStud

def menu_display():
    print ("           Welcome to play the Card Games ! \n")

def main():
## Initial Setting
    value_msg={0:"High Card",1:"One Pair",2:"Two Pair",3:"3 of A Kind",4:"Straight",5:"Flush",6:"Full House",7:"4 of A Kind",8:"Straight Flush"}

# initialize a deck
    deck=[]
    Hand_A=[]
    Hand_B=[]
    name_dict={}
    value_dict={}
    i=1
    for rank in range(2,15):
        for suit in ['C','D','H','S']:
            card_short=Module_Basic.ShortRank(rank)+suit
            card_full=Module_Basic.RankName(rank) + " of " + Module_Basic.SuitName(suit)
            deck.append(card_short)
            name_dict[card_short]=card_full
            value_dict[card_short]=i
            i=i+1
    ##print (len(deck)," cards in the deck ",deck," now.\n\n")
    Module_Basic.ShuffleDeck(deck)

    menu_display()
    exit_index="a"
    while (exit_index!="E"):
        
#Antes:Each player must place a forced bet, the ante, before the cards are dealt. 
#Starting hand: the hole card
        Module_Basic.DrawCard(deck,Hand_A)
        Module_Basic.DrawCard(deck,Hand_B)
# Door card and first betting round
        Module_Basic.DrawCard(deck,Hand_A)
        print ("Player A has: ",Hand_A[1:])
        Module_Basic.DrawCard(deck,Hand_B)
        print ("Player B has: ",Hand_B[1:],"\n")
#Actions: Fold, Call, Raise
#3rd street and second betting round
        Module_Basic.DrawCard(deck,Hand_A)
        print ("Player A has: ",Hand_A[1:])
        Module_Basic.DrawCard(deck,Hand_B)
        print ("Player B has: ",Hand_B[1:],"\n")
#Actions: Fold, Call, Raise
#4th street and third betting round
        Module_Basic.DrawCard(deck,Hand_A)
        print ("Player A has: ",Hand_A[1:])
        Module_Basic.DrawCard(deck,Hand_B)
        print ("Player B has: ",Hand_B[1:],"\n")
#Actions: Fold, Call, Raise
#5th street and fourth betting round
        Module_Basic.DrawCard(deck,Hand_A)
        print ("Player A has: ",Hand_A[1:])
        Module_Basic.DrawCard(deck,Hand_B)
        print ("Player B has: ",Hand_B[1:],"\n")
#Actions: Fold, Call, Raise

###Test Hand
##      Hand_A=["AS","3S","2S","5S","4S"]
##      Hand_B=["6H","3D","9S","3C","9H"]

# Sort all hands before comparing
        Sorted_Hand_A=sorted(Hand_A, key=value_dict.get)
        Sorted_Hand_B=sorted(Hand_B, key=value_dict.get)

# Showdown
        Hand_A_value=Module_5CardStud.EvaluateHand(Sorted_Hand_A)
        Hand_B_value=Module_5CardStud.EvaluateHand(Sorted_Hand_B)
        print ("A: ",Sorted_Hand_A," ",value_msg[Hand_A_value[0]], "  vs  ")
        print ("B:",Sorted_Hand_B," ",value_msg[Hand_B_value[0]])
        if (Hand_A_value[0]==Hand_B_value[0]):
            print ("A: ",name_dict[Hand_A_value[1]],"vs B: ",name_dict[Hand_B_value[1]],"\n")
            if(value_dict[Hand_A_value[1]]>value_dict[Hand_B_value[1]]):
                print ("A wins. \n\n")
            else:
                print ("B Wins. \n\n")
        else:
            if (Hand_A_value[0]>Hand_B_value[0]):
                print ("A Wins. \n\n")
            else:
                print ("B Wins. \n\n")

#Reset the deck
        Module_Basic.MergeDeck(deck,Hand_A) 
        Module_Basic.MergeDeck(deck,Hand_B)
        Module_Basic.ShuffleDeck(deck)    
        exit_index=input("Press e Exit or Enter key to continue! \n").upper()

if __name__ == "__main__":
    main()
