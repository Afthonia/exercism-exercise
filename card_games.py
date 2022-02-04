def get_rounds(number):
    return [number, number+1, number+2]

def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2

def list_contains_round(rounds, number):
    return number in rounds

def card_average(hand):
    return sum(hand) / len(hand)

def approx_average_is_average(hand):
    approx_average = (hand[0] + hand[-1]) / 2
    median = hand[int((len(hand) - 1) / 2)]
    return card_average(hand) == median or card_average(hand) == approx_average

def average_even_is_average_odd(hand):
    hand_even = []
    hand_odd = []
    for i in range(len(hand)):
        if i%2==0:
            hand_even.append(hand[i])
        else:
            hand_odd.append(hand[i])
    
    return sum(hand_even) / len(hand_even) == sum(hand_odd) / len(hand_odd)
    
def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] = 22
    return hand
