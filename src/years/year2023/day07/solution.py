from src.services.BaseSolution import BaseSolution


# https://adventofcode.com/2023/day/7


class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = None
        self.answer_one = None
        self.answer_two = None
        self.hands = []  # each hand can hold 5 cards

        # 1. five of a kind = [AAAAA]
        # 2. four of a kind = [AAAAx]
        # 3. full house = [AAABB]
        # 4. three of a kind = [AAAxx]
        # 5. two pairs = [ABxBA]
        # 6. one pair = [AAxxx]
        # 7. high card = [Axxxx]

        # If two players have the same ranked hands then the rank made up of the highest first card wins;

    def setup(self):
        self.hands = []

    def check_hand(self, cards):
        card_list = list(cards)
        checked_hand = {}
        for card in card_list:
            if checked_hand.get(card) is None:
                checked_hand[card] = 1
            else:
                checked_hand[card] += 1
        if len(checked_hand) == 1:
            hand_type = 6  # "five of a kind"
        elif len(checked_hand) == 2:
            if 4 in checked_hand.values():
                hand_type = 5  # "four of a kind"
            else:
                hand_type = 4  # "full house"
        elif len(checked_hand) == 3:
            if 3 in checked_hand.values():
                hand_type = 3  # "three of a kind"
            else:
                hand_type = 2  # "two pairs+
        elif len(checked_hand) == 4:
            hand_type = 1  # "one pair"
        else:
            hand_type = 0  # "high card"
        return hand_type

    def convert_cards(self, cards):
        card_types = {
            "A": 14,
            "K": 13,
            "Q": 12,
            "J": 11,
            "T": 10,
            "9": 9,
            "8": 8,
            "7": 7,
            "6": 6,
            "5": 5,
            "4": 4,
            "3": 3,
            "2": 2
        }
        for i in range(len(cards)):
            cards[i] = card_types[cards[i]]
        return cards

    def compare_hands(self, hand1, hand2):
        cards1 = self.convert_cards(list(hand1["cards"]))
        cards2 = self.convert_cards(list(hand2["cards"]))
        return_value = None
        for i in range(len(cards1)):
            card1 = cards1[i]
            card2 = cards2[i]
            # print(card1, card1 == card2, card2)
            if card1 == card2:
                continue
            if card1 > card2:
                return_value = True
                break
            else:
                return_value = False
                break

        if return_value is True:
            test = ">"
        else:
            test = "<"
        print(hand1["cards"], cards1, test, hand2["cards"], cards2)

        return return_value

    def get_data(self, input_data):
        ordered_hands = []
        for line in input_data.splitlines():
            cards, point = line.split(" ")
            hand = {
                "cards": cards,
                "point": int(point),
                "type": self.check_hand(cards),
            }
            self.hands.append(hand)

        for i in range(len(self.hands)):
            hand = self.hands[i]
            if len(ordered_hands) == 0:
                ordered_hands.append(hand)
                continue
            for j in range(len(ordered_hands)):
                ordered_hand = ordered_hands[j]
                if hand["type"] == ordered_hand["type"]:
                    print(j)
                    if self.compare_hands(hand, ordered_hand):
                        ordered_hands.insert(j - 1, hand)
                        break
                    else:
                        print(j, "contine")
                        continue
                if hand["type"] > ordered_hand["type"]:
                    ordered_hands.insert(j, hand)
                    break
        return ordered_hands

    def solve_test(self):
        orderd_hands = self.get_data(self.input_test_data)
        total_winnings = 0
        for i in range(len(orderd_hands)):
            j = len(orderd_hands) - i
            # print(orderd_hands[j - 1])
            value = orderd_hands[j - 1]["point"] * (i + 1)
            # print(f"{orderd_hands[j - 1]['point']} * {i + 1}")
            total_winnings += value

        self.answer_test = total_winnings

    def solve_one(self):
        ordered_hands = self.get_data(self.input_data)

        total_winnings = 0
        for i in range(len(ordered_hands)):
            j = len(ordered_hands) - i
            # print(ordered_hands[j - 1])
            point = ordered_hands[j - 1]["point"]
            value = point * (i + 1)
            total_winnings += value

        self.answer_one = total_winnings

    def solve_two(self):
        self.answer_two = ""


if __name__ == "__main__":
    solution = Solution()
    solution.solve()

# 150335621
# 171530778 -> low


# 90001619
# 91445646 -> low
