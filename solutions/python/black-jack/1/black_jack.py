"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    if card == "J"or card =="K"or card =="Q":
        return 10
    elif  card == "A":
        return 1
    else :
        return int(card)

   
    
    """Determine the scoring value of a card.

    Parameters:
        card (str): The given card.

    Returns:
        int: The value of a given card.  See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.
    """

    


def higher_card(card_one, card_two):
    if value_of_card(card_one) < value_of_card(card_two) :
        return card_two
    elif value_of_card(card_one) > value_of_card(card_two):
        return card_one
    else :
        return card_one , card_two
   
    """Determine which card has a higher value in the hand.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.

    Returns:
        str or tuple: The resulting tuple contains both cards if they are of equal value.
    """

    pass


def value_of_ace(card_one, card_two):
    if card_one=="A" or card_two=="A"  :
        return 1
    elif value_of_card(card_one) + value_of_card(card_two) <11:
        return 11
    else :
        return 1
    """Calculate the most advantageous value for an upcoming ace card.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        int: Either 1 or 11, which is the value of the upcoming ace card.
    """




def is_blackjack(card_one, card_two):
   card = {"A","K",'Q','J','10'}
   if value_of_card(card_one) == value_of_card(card_two):
       return False
   elif card_one in card and card_two in card :
       return True
   else :
       return False

       


    


def can_split_pairs(card_one, card_two):
     if value_of_card(card_one) == value_of_card(card_two):
         return True
     else :
         return False


         
  
    


def can_double_down(card_one, card_two):
    double_down = value_of_card(card_one) + value_of_card(card_two) 
    if double_down == 9 or double_down==10 or double_down==11 :
        return True
    else :
        return False

    """Determine if a blackjack player can place a double down bet.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

    Returns:
        bool: Can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

   