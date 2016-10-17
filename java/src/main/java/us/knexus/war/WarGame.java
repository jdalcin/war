/*
 *----------------------------------------------------------------
 * @author: Justin
 * Project Name: Programming Test
 *----------------------------------------------------------------
 * Description:(Class overview)
 *  A programming test designed to use a Deck API to build a functioning
 * version of the card game War.
 *  
 *----------------------------------------------------------------
 * Copyright Notice: Knexus Research Corporation, ${date?date?string("yyyy")}
 * All rights Reserved

 *----------------------------------------------------------------
 * Disclaimer:
 * THIS SOFTWARE IS PROVIDED BY KNEXUS RESEARCH CORP., "AS IS" 
 * AND ANY EXPRESSED OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, WARRANTIES OF INFRINGEMENT AND THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 * PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL KNEXUS RESEARCH CORP.
 * BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
 * TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
 * OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE DISTRIBUTION OR USE OF THIS SOFTWARE, EVEN IF ADVISED
 * OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 */
package us.knexus.war;

import us.knexus.deck.CardFactory;
import us.knexus.deck.Deck;

/**
 * A simple versino of the card game WarGame
 
 * @author Justin
 */
public class WarGame {    
    public static void playRound(Deck deck1, Deck deck2) {
        
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
        playRound(player1, player2);
    }
}
