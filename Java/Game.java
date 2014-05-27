import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Game {

	public static void main(String[] args) {
		
		System.out.println("How many people are playing? (Must be an number)");
		int numOfPlayers = new Scanner(System.in).nextInt();
		Player[] Users = new Player[numOfPlayers];
		Boolean firstTime = true;
		
		int counter = 0;
		while(numOfPlayers > 0){
			System.out.println("Enter Player " + (counter + 1) + "'s name: " );
			String name = new Scanner(System.in).nextLine(); 
			Player player = new Player(name);
			Users[counter] = player;

			numOfPlayers--;
			counter++;
		}

		Deck mainDeck = new Deck(52);
		ArrayList <Integer> deck = new ArrayList <>();
		for(int value : mainDeck.getDeck()){  
			deck.add(value);
		}

		outerloop:
		while(deck.size() > 0){
			for(Player player : Users){
				if (deck.size() == 0){
					break outerloop;
				}
				int currentCard = deck.get(deck.size() - 1);
				deck.remove(deck.size() - 1);
				int numToDo = mainDeck.numPushUps(currentCard) * player.multiplying_factor;
				String pushOrpull = mainDeck.pushOrpull(mainDeck.numPushUps(currentCard));

				if(mainDeck.numPushUps(currentCard) == 1){
					System.out.print(player.name + ": ");
					System.out.print(mainDeck.findCardValue(currentCard) + " of " + mainDeck.findSuit(currentCard));
					System.out.println(" | " + deck.size() + " cards remaining");
					System.out.println("Double Next Card?(Y/N)");
					String input = new Scanner(System.in).nextLine();
					while(!input.equalsIgnoreCase("yes") && !input.equalsIgnoreCase("no") && !input.equalsIgnoreCase("y") && !input.equalsIgnoreCase("n")){
						System.out.println("Double Next Card?(Y/N)");
						input = new Scanner(System.in).nextLine();
					}
					if(input.equalsIgnoreCase("y") || input.equalsIgnoreCase("yes")){
						player.multiplying_factor = player.multiplying_factor * 2;
						player.ace = true;
						player.cards_done++;
					}
					else{
						System.out.print(player.name + ": ");
						System.out.print(15 + " pushups");
						System.out.println(" | " + deck.size() + " cards remaining");
						player.cards_done++;
						player.pushups_done = player.pushups_done + 15;
						new Scanner(System.in).nextLine();
					}

				}
				else{
					player.ace = false;
					player.multiplying_factor = 1;
					System.out.print(player.name + ": ");
					System.out.print(mainDeck.findCardValue(currentCard) + " of " + mainDeck.findSuit(currentCard));
					System.out.print(" - " + numToDo + " " + pushOrpull);
					System.out.println(" | " + deck.size() + " cards remaining");
					player.cards_done++;
					if(pushOrpull.equalsIgnoreCase("push-ups")){
						player.pushups_done = player.pushups_done + numToDo;
					}
					else{
						player.pullups_done = player.pullups_done + numToDo;
					}
					new Scanner(System.in).nextLine();
				}
			}
		}
		for(Player player : Users){
			System.out.println(player.name + ": " + player.pushups_done + " pushups done | " + player.pullups_done + " pullups done | "+ player.cards_done + " cards done");
		}
	}
}
