"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    num1=number+1
    num2=number+2
    number=[number,num1,num2]
    return number
    
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int): The current round number.

    Returns:
        list: The current round number and the two that follow.
    """

    pass


def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1+rounds_2
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """

    


def list_contains_round(rounds, number):
    return number in rounds
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """

    


def card_average(hand):
    sum=0
    for num in hand:
        sum+=num
    avg=sum/len(hand)  
    return avg
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """

    


def approx_average_is_average(hand):
    avg1 = (hand[0]+hand[-1])/2
    avg2 = hand[len(hand)//2]
    if avg1 == card_average(hand) or avg2 == card_average(hand):
        return True
    else :
        return False
    
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """




def average_even_is_average_odd(hand):
    sum1=sum2=0
    hand1=hand[::2]
    for num in hand1:
        sum1+=num
    avg1=sum1/len(hand1)    
    hand2=hand[1::2]
    for num in hand2:
        sum2+=num
    avg2=sum2/len(hand2)  
    if avg1 == avg2:
        return True
    else:
        return False
    """Return if the (average of even indexed card values) ==         (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """

    pass


def maybe_double_last(hand):
    if hand[-1]==11:
        hand[-1]=hand[-1]*2
        return hand
    else:
        return hand
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """

    pass
