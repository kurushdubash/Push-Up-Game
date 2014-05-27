import java.util.Random;


public class Deck {
	private int[] mainDeck;

	public Deck(int deckSize){
		mainDeck = new int[deckSize];
		for(int x = 1; x < deckSize; x++){
			mainDeck[x - 1] = x;
		}
		Random randomGenerator = new Random();
		for(int x = 0; x < deckSize; x++){
			int ranNum = randomGenerator.nextInt(deckSize);
			int tempNum = mainDeck[x];
			mainDeck[x] = mainDeck[ranNum];
			mainDeck[ranNum] = tempNum;
		}
	}
	public int[] getDeck(){
		return mainDeck;
	}

	public String findSuit(int cardNumber){
		String suit = "";
		if(cardNumber < 14){
			suit = "Hearts";}
		else if(cardNumber > 13 && cardNumber < 27){
			suit = "Diamonds";}
		else if(cardNumber > 27 && cardNumber < 40){
			suit = "Spades";}
		else{
			suit = "Clubs";}
		return suit;
	}

	public String findCardValue(int cardNumber){
		int value = cardNumber % 13;
		String cardType;
		if(value == 0){
			cardType = "King";}
		else if(value == 1){
			cardType = "Ace";}
		else if(value == 11){
			cardType = "Jack";}
		else if(value == 12){
			cardType = "Queen";}
		else{
			cardType = Integer.toString(value);
		}
		return cardType;
	}
	
	public int numPushUps(int cardNumber){
		if(cardNumber % 13 == 0){
			return 10;}
		else if(cardNumber % 13 > 10){
			return 10;}
		else{
			return (cardNumber % 13);}
	}

	public String pushOrpull(int workoutNumber){
		if(workoutNumber <= 5){
			return "pull-ups";
		}
		return "push-ups";
	}
}
