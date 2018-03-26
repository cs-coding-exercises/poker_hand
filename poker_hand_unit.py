import unittest
import poker_hand_helper

###=========================================================

class poker_hand_unit(unittest.TestCase):

	##Test Cases
	def test01_straight_flush(self):
		print("### test01_straight_flush")
		expected_msg = "!! Expected 'Straight Flush'"
		
		#Regular Flush (non Straight)
		hand = poker_hand_helper.evaluate_hand(flush)
		self.assertNotEqual( "Straight Flush", hand , "!! Expected 'Flush'")

		#Regular Straight (non Flush)
		hand = poker_hand_helper.evaluate_hand(straight)
		self.assertNotEqual( "Straight Flush", hand , "!! Expected 'Straight'" )

		#Straight Flush
		hand = poker_hand_helper.evaluate_hand(straight_flush)
		self.assertNotEqual( "Straight" , hand, expected_msg )
		self.assertNotEqual( "Flush" , hand, expected_msg )
		self.assertNotIn( "High" , hand, expected_msg )
		self.assertEqual( "Straight Flush", hand , expected_msg )

		#A-2-3-4-5 Straight flush
		hand = poker_hand_helper.evaluate_hand(A2345_straight_flush)
		self.assertNotEqual( "Straight" , hand, expected_msg )
		self.assertNotEqual( "Flush" , hand, expected_msg )
		self.assertNotEqual( "ACE High" , hand, expected_msg )
		self.assertEqual( "Straight Flush", hand , expected_msg )

	# -------------------------------------------------
	def test02_four_of_a_kind(self):
		print("### test02_four_of_a_kind")
		expected_msg = "!! Expected 'Four of a Kind'"
		hand = poker_hand_helper.evaluate_hand(four_of_a_kind)

		# Four of a Kind
		self.assertNotEqual( "Three of a Kind" , hand, expected_msg )
		self.assertNotEqual( "Full House" , hand, expected_msg )
		self.assertNotEqual( "Two Pairs" , hand, expected_msg )
		self.assertNotIn( "Pair of" , hand, expected_msg )
		self.assertEqual( "Four of a Kind", hand , expected_msg )

	# -------------------------------------------------
	def test03_flush(self):
		print("### test03_flush")
		expected_msg = "!! Expected 'Flush'"

		#five cards of the same suit.
		hand = poker_hand_helper.evaluate_hand(flush)
		self.assertNotEqual( "Straight Flush" , hand, expected_msg )
		self.assertEqual( "Flush", hand , expected_msg )

		#four cards of the same suit. One of another suit
		hand = poker_hand_helper.evaluate_hand(flush_minus_one)
		self.assertNotEqual( "Straight Flush" , hand ,"!! Expected '10 High'" )
		self.assertNotEqual( "Flush", hand , "!! Expected '10 High'" )

	# -------------------------------------------------
	def test04_straight(self):
		print("### test04_straight")
		expected_msg = "!! Expected 'Straight'"

		hand = poker_hand_helper.evaluate_hand(straight)
		self.assertNotEqual(" Straight Flush" , hand, expected_msg )
		self.assertNotEqual(" 6 High" , hand, expected_msg )
		self.assertEqual( "Straight", hand , expected_msg )

		# A-2-3-4-5 Straight
		hand = poker_hand_helper.evaluate_hand(A2345_straight)
		self.assertNotEqual( "Straight Flush" , hand, expected_msg )
		self.assertNotEqual( "ACE High" , hand, expected_msg )
		self.assertEqual( "Straight", hand , expected_msg )

		# Gapped straight (3-4-5-6-8: jump over 7)
		hand = poker_hand_helper.evaluate_hand(gapped_straight)
		self.assertNotEqual( "Straight" , hand, expected_msg )
 

	# -------------------------------------------------
	def test05_full_house(self):
		print("### test05_full_house")
		expected_msg = "!! Expected 'Full House'"

		hand = poker_hand_helper.evaluate_hand(full_house)

		self.assertNotEqual( "Three of a Kind" , hand, expected_msg )
		self.assertNotEqual( "Two Pairs" , hand, expected_msg )
		self.assertNotIn( "Pair of" , hand, expected_msg )
		self.assertEqual( "Full House", hand , expected_msg )


	# -------------------------------------------------
	def test06_three_of_a_kind(self):
		print("### test06_three_of_a_kind")
		expected_msg = "!! Expected 'Three of a Kind'"

		hand = poker_hand_helper.evaluate_hand(three_of_a_kind)
		self.assertNotEqual( "Full House", hand , expected_msg )
		self.assertNotEqual( "Four of a Kind", hand , expected_msg )
		self.assertNotEqual( "Two Pairs", hand , expected_msg )
		self.assertNotIn( "Pair of" , hand, expected_msg )
		self.assertEqual( "Three of a Kind" , hand, expected_msg )


	# -------------------------------------------------
	def test07_two_pairs(self):
		print("### test07_two_pairs")
		expected_msg = "!! Expected 'Two Pairs'"

		hand = poker_hand_helper.evaluate_hand(two_pairs)
		self.assertNotEqual( "Full House", hand , expected_msg )
		self.assertNotIn( "Pair of" , hand, expected_msg )
		self.assertNotEqual( "Three of a Kind", hand , expected_msg )
		self.assertEqual( "Two Pairs", hand , expected_msg )

	# -------------------------------------------------
	def test08_pair_of(self):
		print("### test08_pairs")

		expected_queens_msg = "!!Expected 'Pair of QUEENs'"
		hand = poker_hand_helper.evaluate_hand(pair_of_queens)
		self.assertNotEqual( "Full House", hand , expected_queens_msg )
		self.assertNotEqual( "Three of a Kind", hand , expected_queens_msg )
		self.assertNotIn( "High" , hand, expected_queens_msg)
		self.assertEqual( "Pair of QUEENs", hand , expected_queens_msg )
		
		expected_7s_msg = "!!Expected 'Pair of 7s'"
		hand = poker_hand_helper.evaluate_hand(pair_of_sevens)
		self.assertNotEqual( "Full House", hand , expected_7s_msg )
		self.assertNotEqual( "Three of a Kind", hand , expected_7s_msg )
		self.assertNotIn( "High" , hand, expected_7s_msg)
		self.assertEqual( "Pair of 7s", hand , expected_7s_msg )

	# -------------------------------------------------
	def test09_high_card_hand(self):
		print("### test09_high_card_hand")

		hand = poker_hand_helper.evaluate_hand(seven_high)
		self.assertNotEqual( "Straight", hand , "!!Expected '7 High'")
		self.assertEqual( "7 High", hand , "!!Expected '7 High'" )

		hand = poker_hand_helper.evaluate_hand(ten_high)
		self.assertNotEqual( "Flush", hand ,  "!!Expected '10 High'")
		self.assertEqual( "10 High", hand , "!!Expected '10 High'" )

		hand = poker_hand_helper.evaluate_hand(ace_high)
		self.assertNotEqual( "10 High", hand ,  "!!Expected 'ACE High'")
		self.assertNotEqual( "QUEEN High", hand ,  "!!Expected 'ACE High'")
		self.assertEqual( "ACE High", hand , "!!Expected 'ACE High'" )

 

###Test Hands ==========================================
# straight flush
straight_flush = [
['10','SPADES', 10], ['JACK','SPADES', 11], ['QUEEN', 'SPADES', 12],
['KING','SPADES', 13], ['ACE', 'SPADES', 14]]

A2345_straight_flush = [
['A', 'CLUBS', 14], ['2','CLUBS', 2], ['3', 'CLUBS', 3],
['4', 'CLUBS', 4], ['5', 'CLUBS', 5]]


# four of a kind
four_of_a_kind = [
['10','SPADES', 10], ['10','HEARTS', 10], ['3', 'SPADES', 3],
['10','CLUBS', 10], ['10', 'DIAMONDS', 10]]


#flush
flush = [
['5','CLUBS', 5], ['6','CLUBS', 6], ['7', 'CLUBS', 7],
['8', 'CLUBS', 8], ['10', 'CLUBS', 10]]

flush_minus_one = [
['5','CLUBS', 5], ['6','CLUBS', 6], ['7', 'CLUBS', 7],
['8', 'CLUBS', 8], ['10', 'SPADES', 10]]


# straights
straight = [
['2', 'DIAMONDS', 2], ['3','DIAMONDS', 3], ['4', 'HEARTS', 4],
['5', 'DIAMONDS', 5], ['6', 'DIAMONDS', 6]]

gapped_straight = [
['3', 'DIAMONDS', 3], ['4','DIAMONDS', 4], ['5', 'HEARTS', 5],
['6', 'DIAMONDS', 6], ['8', 'DIAMONDS', 8]]

A2345_straight = [
['A', 'DIAMONDS', 14], ['2','HEARTS', 2], ['3', 'SPADES', 3],
['4', 'DIAMONDS', 4], ['5', 'CLUBS', 5]]

 

# full house
full_house = [
['QUEEN','SPADES', 12], ['QUEEN','HEARTS', 12], ['QUEEN', 'CLUBS', 12],
['7', 'CLUBS', 7], ['7', 'DIAMONDS', 7]]

 

# three of a kind
three_of_a_kind = [
['QUEEN','SPADES', 12], ['QUEEN','HEARTS', 12], ['QUEEN', 'CLUBS', 12],
['7', 'CLUBS', 7], ['2', 'CLUBS', 2]]

 

# two pairs
two_pairs = [
['QUEEN','SPADES', 12], ['QUEEN','HEARTS', 12], ['4', 'HEARTS', 4],
['7', 'CLUBS', 7], ['7', 'DIAMONDS', 7]]

 

# pairs
pair_of_queens = [
['QUEEN','SPADES', 12], ['QUEEN','HEARTS', 12], ['4', 'HEARTS', 4],
['7', 'CLUBS', 7], ['6', 'DIAMONDS', 6]]

pair_of_sevens = [
['QUEEN','SPADES', 12], ['KING','HEARTS', 13], ['9', 'DIAMONDS', 9],
['7', 'CLUBS', 7], ['7', 'DIAMONDS', 7]]

 

# high card
ace_high = [
['2','SPADES', 2], ['10','HEARTS', 10], ['6', 'DIAMONDS', 6],
['QUEEN','CLUBS', 12], ['ACE', 'HEARTS', 14]]

ten_high = [
['10','CLUBS', 10], ['3','CLUBS', 3], ['2', 'SPADES', 2],
['7', 'CLUBS', 7], ['8', 'CLUBS', 8]]

seven_high = [
['2', 'DIAMONDS', 2], ['3','DIAMONDS', 3], ['4', 'HEARTS', 4],
['5', 'DIAMONDS', 5], ['7', 'DIAMONDS', 7]]

 

if __name__ == '__main__':
	unittest.main()

