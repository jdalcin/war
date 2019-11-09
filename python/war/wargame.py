import cardfactory as cardfact
import card as card
import deck as deck

# Rules:
# deck1 and deck2 should always have at least 1 card each -- if either deck has 0 cards, then the game is over
# if a draw deck gets to zero, then shuffle it
# if a deck has no card in draw or discard pile, then use latest card drawn
# winner takes all drawn cards and adds it to discard pile
# drawn cards other than the latest drawn are considered waste cards

# Round Algorithm:
# create an empty drawn list
# draw card from deck1 and deck2
# add drawn cards to the draw list
# if decks latest cards are equal
#   go to game
# if deck1's latest card > deck2's latest card
#   deck 1 wins
# else if deck1's latest card < deck2's latest card
#   deck 2 wins
# else
#   its a draw
# add drawn cards to discard pile of winner -- if draw, don't add cards

# War Algorithm:
# while deck1's latest card = deck2's latest card
#   both cards draw 2 cards -- if they can
#   add drawn cards to the drawn list

def play_round(deck1, deck2):
    if deck1.get_draw_pile_size() <= 0 or deck2.get_draw_pile_size() <= 0:
        raise Exception("Both decks need to have at least 1 card in draw pile")
    drawn_pile = []
    deck1_latest_draw = deck1.draw()
    deck2_latest_draw = deck2.draw()
    drawn_pile.extend([deck1_latest_draw, deck2_latest_draw])
    while deck1_latest_draw.get_ordinal() == deck2_latest_draw.get_ordinal() and (deck1.get_draw_pile_size() > 0 or deck2.get_draw_pile_size() > 0):
        for i in range(2):
            if deck1.get_draw_pile_size() > 0:
                deck1_latest_draw = deck1.draw()
                drawn_pile.append(deck1_latest_draw)
                if deck1.get_draw_pile_size() == 0:
                    deck1.shuffle()
            if deck2.get_draw_pile_size() > 0:
                deck2_latest_draw = deck2.draw()
                drawn_pile.append(deck2_latest_draw)
                if deck2.get_draw_pile_size() == 0:
                    deck2.shuffle()

    if deck1_latest_draw.get_ordinal() > deck2_latest_draw.get_ordinal():
        deck1.discard_pile.extend(drawn_pile)
    elif deck1_latest_draw.get_ordinal() < deck2_latest_draw.get_ordinal():
        deck2.discard_pile.extend(drawn_pile)
    else:
        pass
    if deck1.get_draw_pile_size() == 0:
        deck1.shuffle()
    if deck2.get_draw_pile_size() == 0:
        deck2.shuffle()


def play_game(player1, player2):
    """
    This function when called will play an entire game of War.
    playRound will get called until either play is completely out of cards.
    
    :param player1: Deck of cards representing player 1
    :param player2: Deck of cards representing player 2
    """
    
    while player1.get_num_cards() > 0 and player2.get_num_cards() > 0:
        play_round(player1, player2)
    if player1.get_num_cards() == player2.get_num_cards():
        print("It is a draw!")
    else:
        winner = "player 1" if player1.get_num_cards() > player2.get_num_cards() else "player 2"
        print("The winner is {}".format(winner))

if __name__== '__main__':
    # Creates the card factory
    factory = cardfact.CardFactory()

    # Makes a full deck for p1, empty for p2, shuffles
    player1 = factory.create_full_deck()
    player2 = deck.Deck()
    player1.shuffle()

    # Deals half of player 1's shuffled deck to player 2
    decksize = int(player1.get_draw_pile_size() / 2)
    for i in range(decksize):
        player2.add_to_discard(player1.draw())

    # Shuffle the decks
    player1.shuffle()
    player2.shuffle()

    # play a single round of War
    play_round(player1, player2)

    # play an entire game of War
    play_game(player1, player2)