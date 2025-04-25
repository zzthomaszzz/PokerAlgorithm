from card import Card
import algorithm

def test(hand, expect):
    # hand :: List of 7 cards
    # expect :: String of best combination
    result = algorithm.find_best_combination(hand)
    if result == expect.lower():
        print("Pass")
    else:
        print("Fail")

case = [Card("A", "d"),
        Card("A", "h"),
        Card("A", "c"),
        Card("7", "h"),
        Card("8", "s"),
        Card("10", "s"),
        Card("J", "c"),
        ]
expected = "Trips"

test(case, expected)

case = [Card("J", "d"),
        Card("A", "h"),
        Card("2", "c"),
        Card("7", "h"),
        Card("8", "s"),
        Card("10", "s"),
        Card("J", "c"),
        ]
expected = "Pair"

test(case, expected)

case = [Card("A", "d"),
        Card("A", "h"),
        Card("7", "c"),
        Card("7", "h"),
        Card("8", "s"),
        Card("10", "s"),
        Card("J", "c"),
        ]
expected = "two pairs"

test(case, expected)
