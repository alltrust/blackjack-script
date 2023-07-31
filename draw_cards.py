import random

def draw_cards(current_all_cards: list, num_to_draw: int) -> tuple[list, list]:
    """Draws 2 cards from the current deck while adjusting for the cards drawn.

    Arguments:
        current_all_cards -- The current deck with the cards adjusted

    Returns:
        The cards for the current user, with the adjusted current deck.
    """
    if num_to_draw == 2:

        cards = random.choices(current_all_cards, k=2)

        while cards[0] == cards[1]:
            cards[1] == random.choice(current_all_cards)
        # remove the cards from the current deck

        for card in cards:
            current_all_cards.remove(card)


    else:

        cards = random.choice(current_all_cards)
        current_all_cards.remove(cards)


    return cards, current_all_cards


def hit_or_pass() -> bool:
    return True if input(
        "Would you like to hit (press 'y') or pass (press 'n')?:") == 'y' else False


def prompt_play() -> bool:
    return True if input(
        "Would you like to play again? 'y' for yes, anything else to quit: ") == 'y' else False

