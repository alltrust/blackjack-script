import random
from ascii_cards import cards_logo
from cards import deck_of_cards


def play_blackjack() -> None:
    """Play a game of BlackJack!
    """

    is_play = True
    all_cards = list(deck_of_cards)
    while is_play:

        print(cards_logo)

        random.shuffle(all_cards)

        users_cards = random.choices(all_cards, k=2)
        while users_cards[0] == users_cards[1]:
            users_cards[1] = random.choice(all_cards)

        print(users_cards)
        users_cards_value = int(
            deck_of_cards[users_cards[0]]) + int(deck_of_cards[users_cards[1]])

        print(f"Your Cards: {users_cards}")

        users_ace_count = 0
        for card in users_cards:
            all_cards.remove(card)
            if "A" in card:
                users_ace_count += 1

        computers_cards = random.choices(all_cards, k=2)
        while computers_cards[0] == computers_cards[1]:
            computers_cards[1] = random.choice(all_cards)

        computers_cards_value = int(
            deck_of_cards[computers_cards[0]]) + int(deck_of_cards[computers_cards[1]])

        first_card = computers_cards[0]

        comps_ace_count = 0
        for card in computers_cards:
            all_cards.remove(card)
            if "A" in card:
                comps_ace_count += 1

        print(f"Dealers Hand: {first_card} _")

        is_hit = None
        if users_cards_value == 21:
            is_hit = False
        else:
            is_hit = True if input(
                "Would you like to hit (press 'y') or pass (press 'n')?:") == 'y' else False

        while is_hit and users_cards_value != 21:
            # check score > 21
            if users_cards_value > 21:
                if users_ace_count > 0:
                    users_cards_value -= 10
                    users_ace_count -= 1
                else:
                    is_hit = False
            else:
                new_card = random.choice(all_cards)
                all_cards.remove(new_card)
                users_cards.append(new_card)
                users_cards_value += deck_of_cards[users_cards[len(
                    users_cards) - 1]]
                print(f"Your hand: {users_cards}")
                if "A" in new_card:
                    users_ace_count += 1
                if users_cards_value > 21 and users_ace_count == 0:
                    print("You lost")
                    is_hit = False
                    break

                else:
                    is_hit = True if input(
                        "Would you like to hit (press 'y') or pass (press anything else)?: ") == 'y' else False

        print(f"Your final hand: {users_cards}")

        while computers_cards_value < users_cards_value and users_cards_value < 22:
            if computers_cards_value > 21:
                if comps_ace_count > 0:
                    computers_cards_value -= 10
                    comps_ace_count -= 1
                else : 
                    break
            else:

                new_card = random.choice(all_cards)
                all_cards.remove(new_card)
                computers_cards.append(new_card)
                computers_cards_value += deck_of_cards[computers_cards[len(
                    computers_cards) - 1]]
                
                if "A" in new_card:
                    comps_ace_count += 1
                else:
                    continue
                
            # else:
            #     break

        print(f"Dealers Final hand:  {computers_cards}")

        if users_cards_value > 21 or (22 > computers_cards_value > users_cards_value):
            print("you lost!")
            is_play = True if input(
                "Would you like to play again? 'y' for yes, anything else to quit: ") == 'y' else False
        elif computers_cards_value > 21 or (22< users_cards_value > computers_cards_value):
            is_play = True if input(
                "YOU WIN! Play again (y for yes; anything else to quit):") == 'y' else False
        elif users_cards_value == computers_cards_value:
            print("a TIE!")
            is_play = True if input(
                "Would you like to play again? 'y' for yes, anything else to quit: ") == 'y' else False

    print("Goodnight!")


play_blackjack()
