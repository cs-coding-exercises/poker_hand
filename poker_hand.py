############################################################
# poker_hand.py:
# This module:
# - Accesses five random cards from deckofcards.api
# - Prints values and suits to console
# - Evaluates the top scoring hand based on the cards
# - Displays the cards and top scoring hand in HTML format
#####################################################
import sys
import requests
import json
import poker_hand_helper
import os

##==========================================================

display_html = None
#print("args: " + str(argv[1]) )

if len(sys.argv) > 1:
	if sys.argv[1].lower() == 'html':
		display_html = True
	elif sys.argv[1].lower() != 'html':
		print("!! make first argument 'html' to display hand\n")

### Create and shuffle deck of cards ----------------------
response = requests.get('https://deckofcardsapi.com/api/deck/new/draw/?count=5')
if response.status_code == 200:
	cards_json_data = json.loads(response.content.decode('utf-8'))
else:
	print("!! Status Code not 200")
	sys.exit()

 

### Print values and suits to console ---------------------
print("___ cards[x]:value;suit _____")
for x in range (0,5):
	print(cards_json_data['cards'][x]['value'] + ";"
	+ cards_json_data['cards'][x]['suit'])
print("")


### Create 3 item list array and pass into evaluate_hand()
evaluation_criteria = []

#assign weights to the cards based on value
for x in range (0,5):
	value = cards_json_data['cards'][x]['value']
	if value == "JACK" : weight = 11
	elif value == "QUEEN": weight = 12
	elif value == "KING" : weight = 13
	elif value == "ACE" : weight = 14
	else: weight = int(value)

	evaluation_criteria.append([
		value,
		cards_json_data['cards'][x]['suit'],
		weight
	])

#Get top scoring hand and print to console

top_scoring_hand = poker_hand_helper.evaluate_hand(evaluation_criteria)
print("top_scoring_hand: " + top_scoring_hand)

if display_html:
	poker_hand_helper.display_cards(cards_json_data, top_scoring_hand)

# remove cache file
os.system("rm -r __pycache__")
