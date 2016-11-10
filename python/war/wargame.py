"""
Knexus Python Programming test

Author: JT
"""
import cardfactory as cardfact
import card as card
import deck as deck


def play_round(deck1, deck2):
    pass  # YOUR CODE GOES HERE

if __name__== '__main__':
    # Creates the card factory
    factory = cardfact.CardFactory()

    # Makes a full deck for p1, empty for p2, shuffles
    player1 = factory.create_full_deck()
    player2 = deck.Deck()
    player1.shuffle()

    # Deals half of player 1's shuffled deck to player 2
    decksize = player1.get_draw_pile_size() / 2
    for i in range(decksize):
        player2.add_to_discard(player1.draw())

    # Shuffle the decks
    player1.shuffle()
    player2.shuffle()

    # Step the game
    play_round(player1, player2)