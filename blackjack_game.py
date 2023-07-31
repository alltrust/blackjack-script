import random
from draw_cards import draw_cards, prompt_play, hit_or_pass
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

        users_cards, all_cards = draw_cards(all_cards, 2)

        users_cards_value = int(
            deck_of_cards[users_cards[0]]) + int(deck_of_cards[users_cards[1]])

        print(f"Your Cards: {users_cards}")

        computers_cards, all_cards = draw_cards(
            all_cards, 2)

        computers_cards_value = int(
            deck_of_cards[computers_cards[0]]) + int(deck_of_cards[computers_cards[1]])

        first_card = computers_cards[0]
        print(f"Dealers Hand: {first_card} _")

        is_hit = None
        if users_cards_value == 21:
            is_hit = False
        else:
            is_hit = hit_or_pass()

        users_ace_count = sum(card.count("A") for card in users_cards)
        while is_hit and users_cards_value != 21:

            if users_cards_value > 21:
                if users_ace_count > 0:
                    users_cards_value -= 10
                    users_ace_count -= 1
                else:
                    is_hit = False
            else:

                new_card, all_cards= draw_cards(
                    all_cards, 1)

                users_cards.append(new_card)
                users_cards_value += deck_of_cards[users_cards[len(
                    users_cards) - 1]]

                print(f"Your hand: {users_cards}")

                if users_cards_value > 21 and users_ace_count == 0:
                    is_hit = False
                    break

                else:
                    is_hit = hit_or_pass()

        print(f"Your final hand: {users_cards}")


        comps_ace_count = sum(card.count("A") for card in computers_cards )
        while (22 < users_cards_value > computers_cards_value) and computers_cards_value != 21:

            new_card, all_cards= draw_cards(
                all_cards, 1)

            computers_cards.append(new_card)

            computers_cards_value += deck_of_cards[computers_cards[len(
                computers_cards) - 1]]
            if computers_cards_value > 21:
                if comps_ace_count > 0:
                    computers_cards_value -= 10
                    comps_ace_count -= 1
                else:
                    break

        print(f"Dealer's Final hand:  {computers_cards}")

        if users_cards_value > 21 or (22 > computers_cards_value > users_cards_value):
            print("you lost!")

        elif computers_cards_value > 21 or (22 < users_cards_value > computers_cards_value):
            print("you win!")

        elif users_cards_value == computers_cards_value:
            print("a TIE!")

        is_play = prompt_play()

    print("Goodnight!")


play_blackjack()
