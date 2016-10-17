/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package us.knexus.war;

import us.knexus.deck.CardFactory;
import us.knexus.deck.Deck;

/**
 *
 * @author Justin
 */
public class WarGame {    
    public static void stepWar(Deck deck1, Deck deck2) {
        
    }
    
    public static void main(String[] args) {
        // Get a new CardFactory instance
        CardFactory factory = new CardFactory();
        
        // Get a full deck, set as player 1
        Deck player1 = factory.createFullDeck();        
        // Make a new empty deck for player 2
        Deck player2 = new Deck();
        // Shuffle the player 1 deck
        player1.shuffle();

        // deal half of player 1's shuffled deck to player 2
        int deckSize = player1.getDrawPileSize() / 2;
        for(int i=0; i<deckSize; ++i)
            player2.addToDiscard(player1.draw());

        // shuffle both decks
        player1.shuffle();
        player2.shuffle();

        // step the game
        stepWar(player1, player2);
    }
}
