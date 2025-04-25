
def find_best_combination(hand):
    # hand :: List
    hands = {}
    pair = 0
    trips = 0
    for card in hand:
        if card.rank in hands.keys():
            hands[card.rank] += 1
        else:
            hands[card.rank] = 1

    for card in hands:
        if hands[card] == 2:
            pair += 1
        if hands[card] == 3:
            trips += 1
    if trips == 1:
        return "trips"
    elif pair == 2:
        return "two pairs"
    elif pair == 1:
        return "pair"
    else:
        return "None"