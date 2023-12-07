from functools import cmp_to_key

inputfile = open('input.txt', 'r')

hands = []

for line in inputfile:
    hands.append(line.split(' '))

# Basically the same shit as before, we just have to shift cards estimates and now gather jokers separately from other logic with adding them where applicable
# (funny enough full house doesn't really change). BE AWARE that 'JJJJJ' is a valid combination for five of a kind


class Combination:
    def __init__(self):
        self.baseCardsValues = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4,
                                '3': 3, '2': 2, 'J': 1}

    def get_base_card_value(self, card: str) -> int:
        return self.baseCardsValues[card]

    def get_cards_count(self, card_stack: str) -> dict:
        cards_count = {}
        for card in card_stack:
            if card == 'J':
                continue
            if card in cards_count:
                cards_count[card] += 1
            else:
                cards_count[card] = 1

        return cards_count

    def get_jokers(self, card_stack: str) -> int:
        result = 0
        for card in card_stack:
            if card == 'J':
                result += 1
        return result

    def get_calculation_of_stack(self, stack: str) -> (int, str):
        pass


class SingleCard(Combination):
    def get_calculation_of_stack(self, stack: str) -> int:
        return 1


class Pair(Combination):
    def get_calculation_of_stack(self, stack: str) -> int:
        cards_count = self.get_cards_count(stack)
        jokers = self.get_jokers(stack)

        for card in cards_count:
            if cards_count[card] + jokers == 2:
                return 2

        return 0


class TwoPairs(Combination):
    def get_calculation_of_stack(self, stack: str) -> int:
        cards_count = self.get_cards_count(stack)
        jokers = self.get_jokers(stack)

        stack_assembly = []
        for card in cards_count:
            if cards_count[card] == 2:
                stack_assembly.append(card)

        if len(stack_assembly) == 2:
            return 3

        return 0


class ThreeOfAKind(Combination):
    def get_calculation_of_stack(self, stack: str) -> int:
        cards_count = self.get_cards_count(stack)
        jokers = self.get_jokers(stack)
        for card in cards_count:
            if cards_count[card] + jokers == 3:
                return 4

        return 0


class FullHouse(Combination):
    def get_calculation_of_stack(self, stack: str) -> (int):
        cards_count = self.get_cards_count(stack)

        if len(cards_count) == 2:
            return 5

        return 0


class FourOfAKind(Combination):
    def get_calculation_of_stack(self, stack: str) -> (int):
        cards_count = self.get_cards_count(stack)
        jokers = self.get_jokers(stack)
        for card in cards_count:
            if cards_count[card]+jokers == 4 or jokers > 2:
                return 6

        return 0


class FiveOfAKind(Combination):
    def get_calculation_of_stack(self, stack: str) -> (int):
        cards_count = self.get_cards_count(stack)
        jokers = self.get_jokers(stack)
        if jokers == 5:
            return 7
        for card in cards_count:
            if cards_count[card]+jokers == 5 or jokers > 3:
                return 7

        return 0


combinations = [FiveOfAKind(), FourOfAKind(), FullHouse(), ThreeOfAKind(), TwoPairs(), Pair(), SingleCard()]


def compare(item1, item2) -> int:
    if item1 == item2:
        return 0

    rank1 = 0
    rank2 = 0

    itemCards1 = item1[0]
    itemCards2 = item2[0]

    for combination in combinations:
        calculated = combination.get_calculation_of_stack(itemCards1)
        if calculated > 0:
            rank1 = calculated
            break

    for combination in combinations:
        calculated = combination.get_calculation_of_stack(itemCards2)
        if calculated > 0:
            rank2 = calculated
            break

    if rank1 != rank2:
        return rank1 - rank2

    comparer = Combination()

    for index, symbol1 in enumerate(itemCards1):
        symbol2 = itemCards2[index]
        rankOfCard1 = comparer.get_base_card_value(symbol1)
        rankOfCard2 = comparer.get_base_card_value(symbol2)
        if rankOfCard1 != rankOfCard2:
            return rankOfCard1 - rankOfCard2

    return 0


sorted_hands = sorted(hands, key=cmp_to_key(compare))
print(sorted_hands)

result = 0


for index, hand in enumerate(sorted_hands):
    result += int(int(hand[1]) * (index + 1))

print(result)
