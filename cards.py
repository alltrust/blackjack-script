def create_deck() -> dict:
    """Creates a deck cards with values as weights for a game of blackJack

    Returns:
        Deck of 52 cards
    """
    card_ranks = ["2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "J", "Q", "K", "A"]
    card_suits = ["Hearts", "Spades", "Cloves", "Diamonds"]
    deck = {}
    for suit in card_suits:
        for rank in card_ranks:
            suited_rank = f"{rank}{suit[0]}"
            if rank in "JQK":
                deck[suited_rank] = 10
            elif rank == "A":
                deck[suited_rank] = 11
            else:
                deck[suited_rank] = int(rank)

    return deck


deck_of_cards = create_deck()
