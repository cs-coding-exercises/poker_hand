Poker Hand is an application that:

- accesses five random cards from https://deckofcardsapi.com/
- prints The values and suits of the cards to the console
- evaluates the top scoring poker hand based on the cards
- displays the cards and top scoring hand in HTML format (if requested)


## Setup:
The following files should be present in the suggested locations:
```
	~/poker_hand/poker_hand.py
	~/poker_hand/poker_hand_helper.py
	~/poker_hand/poker_hand_unit.py
```

If you want to run this on a Windows machine:
- The files can be installed on whichever directory you want (in the same directory).
- Modify the location of the HTML file in the display_cards() function in the helper file (currently it's /tmp/ for Linux)

- Install Python3
	
These should be run using Python 3.  Otherwise resources will need to be installed.

It was developed using 3.5.2


## Running (2 options):
(1) No Display:

Simply run (Do not include parameters)
```
	$ python3 ~/poker_hand/code/poker_hand.py
```
This will output the values and suits of the cards to the console:

Example:
```
___ cards[x]:value;suit _____
JACK;DIAMONDS
9;CLUBS
KING;HEARTS
3;CLUBS
7;SPADES
```
(2) HTML Output Display

Run with the first argument being 'html' (case insensitive)
```
	$ python3 ~/poker_hand/code/poker_hand.py html # or HTML, HtMl, etc.
```
This will both:

	A) output the values and suits of the cards to the console,as in (1) above.
	B) create and display an HTML file including:
	- The highest scoring hand test ('Straight Flush', Full House, 'Pair of 3s', 'ACE High')
	- image links of the cards based on the data from the API call

This HTML file will be stored in the /tmp/ folder (unless modified per assumptions).  A browser will open diplaying the file.


## Unit Tests:

'''
poker_hand_unit.py
'''
Currently the unit tests include only calls to the evaluate_hand() in the helper function.

This function receives a five item list of card data, including:
- the value ('2', '10', 'JACK', 'ACE', etc. )

- the suit ("SPADES", "HEARTS", "CLUBS", "DIAMONDS")

- a numeric weight, based on the value ('2' => 2, '10'=> 10, 'JACK' => 11 , 'ACE'=> 14, etc.)

This is the same data produced by the main poker_hand.py and sent when calling the method.

it then returns the highest scoring hand value and verifies it against the expected hand.

The unit tests create several of the card lists and verifies the proper hand/description is returned.
Examples:
```
#-----------------------------
	straight_flush = [
	['10','SPADES', 10], ['JACK','SPADES', 11], ['QUEEN', 'SPADES', 12],
	['KING','SPADES', 13], ['ACE', 'SPADES', 14]]

	def test01_straight_flush(self):
		print("### test01_straight_flush")
		expected_msg = "!! Expected 'Straight Flush'"

		hand = poker_hand_helper.evaluate_hand(straight_flush)
		self.assertNotEqual("Straight" , hand, expected_msg )
		self.assertNotEqual("Flush" , hand, expected_msg )
		self.assertEqual( "Straight Flush", hand , expected_msg )
#-----------------------------
	full_house = [
	['QUEEN','SPADES', 12], ['QUEEN','HEARTS', 12], ['QUEEN', 'CLUBS', 12],
	['7', 'CLUBS', 7], ['7', 'DIAMONDS', 7]]

	def test05_full_house(self):
		print("### test05_full_house")
       		expected_msg = "!! Expected 'Full House'"

		hand = poker_hand_helper.evaluate_hand(full_house)
		self.assertNotEqual("Three of a Kind" , hand, expected_msg )
        	self.assertNotIn("Two Pairs" , hand, expected_msg )
        	self.assertNotIn("Pair of" , hand, expected_msg )
#-----------------------------
```
## Assumptions:
	- '5 of a Kind' hand, is out of scope with 1 deck of cards.
	- The sorting of the cards by weight and/or suit, though helpful, was not necessary
	- Hands above pairs did not need more information that the hand itself ('2 pairs', 'Full House, 'Flush', etc.)
  	  ones below that are clarified ('Pair of 3s', 'King High', etc.)
	- No Jokers or WildCards are expected to be logically addressed
