############################################################
# poker_hand_helper.py:
# This module contains the two functions called by
# poker_hand.py ( evaluate_hand() and display_cards() )
# 
#####################################################
import webbrowser

def evaluate_hand(hand):

	# properties with which to evaluate the hands
	flush 		= None
	straight	= None
	four_of_a_kind 	= None
	three_of_a_kind = None
	pairs 		= 0

	#create lists and populate to evalueate
	suits_list   = []
	weights_list = []
	values_list  = []

	for card in hand:
		values_list.append(card[0])
		suits_list.append(card[1])
		weights_list.append(card[2])


	### Flush? verify number of unique suits
	unique_suits = len(set(suits_list))

	if unique_suits == 1:
		flush = True
	else:
		flush = False

	### Straight? sort weight list and verify
	# the items are sequential
	weights_sorted = sorted(weights_list)

	for x in range(1,5):
		if ( weights_sorted[x] - weights_sorted[x-1] ) != 1:
			straight = False

	# [Ace, '2', '3', '4', '5'] is considered a straight
	if straight == None or weights_sorted == [2, 3, 4, 5, 14]:
		straight = True

	### Multiples? (Four of a Kind, Three of a Kind, Pairs? ====

	#list to store numbers of each unique value
	value_counts = []

	#initialize a list with only unique values and a count of zero
	unique_values = set(values_list)

	for unique_value in unique_values:
		value_counts.append([unique_value, 0])

	# get the counts of each value in the hand and over-writes the zero count
	for value_count in value_counts:
		value_count[1] = values_list.count(value_count[0])
	
	for value_count in value_counts:
		if value_count[1] == 2:
			pairs += 1
			pair_of = value_count[0] + "s"
		if value_count[1] == 3:
			three_of_a_kind = True
		if value_count[1] == 4:
			four_of_a_kind = True

	###Highest Card ==========================================
	highest_weight = weights_sorted[4]
	if   highest_weight == 11: high_card = "JACK"
	elif highest_weight == 12: high_card = "QUEEN"
	elif highest_weight == 13: high_card = "KING"
	elif highest_weight == 14: high_card = "ACE"
	else: high_card = str(highest_weight)

	unique_values_count = len(unique_values)

	#Return Highest Scoring Hand
	#if five_of_a_kind:
		# (Not relevant, given one deck)
	if flush and straight:
		return "Straight Flush"
	elif four_of_a_kind:
		return "Four of a Kind"
	elif pairs == 1 and three_of_a_kind == True:
		return "Full House"
	elif flush:
		return "Flush"
	elif straight:
		return "Straight"
	elif three_of_a_kind:
		return "Three of a Kind"
	elif pairs == 2:
		return "Two Pairs"
	elif pairs == 1:
		return "Pair of " + pair_of
	elif unique_values_count == 5:
		return "%s High" % high_card
	else:
		return "Error: Hand does not meet any criteria"

#--------------------------------------
def display_cards(json_data, hand):
	# Generate HTML page with top scoring hand and card images

	print("\n*** Displaying cards ***")
	hand_imgs = []

	for x in range (0,5):
		hand_imgs.append(json_data['cards'][x]['image'])
	hand_imgs=sorted(hand_imgs)

	
	ph_html = "/tmp/poker_hand.html"
	#Build HTML Page to display Hand
	with open(ph_html, "w") as html:
		html.write("<HTML>\n<HEAD>\n<title>Poker Hand</title>\n")
		html.write("</HEAD>\n<BODY>\n")
		html.write("<h2><b>%s</b></h2>\n" % hand)
		for image in hand_imgs:
			html.write("<img src='%s'>\n" % image)
		html.write("</BODY>\n</HTML>")

	webbrowser.open_new(ph_html)
