import random
import json	
from colorama import init
init()
from colorama import Fore, Back, Style
import datetime
#from wait import read_single_keypress


def shuffle_deck(num_of_cards=52):
	main_list = list(range(1, num_of_cards + 1))	
	x = 0
	while x < len(main_list):
		random_index = random.randint(0, 51)
		main_list[x], main_list[random_index] = main_list[random_index], main_list[x]
		x += 1
	return main_list

def draw(main_list):
	return main_list.pop()

def find_suit(num):
	suit =''
	if num < 14:
		suit = 'Hearts'
	elif num > 13 and num < 27:
		suit = 'Diamonds'
	elif num > 27 and num < 40:
		suit = 'Spades'
	else:
		suit = 'Clubs'
	return suit

def find_card_value(num):
	value = num % 13
	if value == 0:
		value = 'King'
	elif value == 1:
		value = 'Ace'
	elif value == 11:
		value = 'Jack'
	elif value == 12:
		value = 'Queen'
	return value

def number_of_pushups(num):
	if num % 13 == 0:
		return 10
	elif num % 13 > 10:
		return 10
	else:
		return num % 13

def make_players(num):
	i = 0
	list_of_players = []
	while i < num:
		list_of_players.append(Player(input("Enter Player " + str(i + 1) + "'s name: ")))
		i += 1
	return list_of_players

def pushup_or_pullups(number):
	if number <= 5:
		return 'pull-ups'
	return 'push-ups'
	
def push_ups(number_of_players, players):

	while len(Player.main_deck) > 0:
		for k in range(len(players)):
			if len(Player.main_deck) == 0:
				break
			card = draw(Player.main_deck)
			num_to_do = number_of_pushups(card) * players[k].multiplying_factor
			pull_or_push = pushup_or_pullups(num_to_do) 

			if number_of_pushups(card) == 1:
				print(Style.BRIGHT + Fore.YELLOW + players[k].name, ':', Fore.CYAN +'', find_card_value(card), 'of', find_suit(card))
				double_or_fifteen = ''
				while double_or_fifteen == '':
					double_or_fifteen = input('Double Next Card?(Y/N)')
					double_or_fifteen = double_or_fifteen.lower()
				if double_or_fifteen.lower() == 'y' :
					players[k].double = True
					players[k].multiplying_factor *= 2
					players[k].cards_done += 1
				else:
					print(Fore.RED + players[k].name, ': 15 push-ups'+ Fore.GREEN + ' | ' + 
						str(len(players[k].main_deck)) + ' cards remaining')

					players[k].pushups_done += 15
					players[k].cards_done += 1

			else:
				print(Style.BRIGHT + Fore.YELLOW + players[k].name, ':', Fore.CYAN +'', find_card_value(card), 'of',
					 find_suit(card), '-',  Fore.RED +'', num_to_do, pull_or_push, Fore.GREEN + '| ' + 
					 str(len(players[k].main_deck)) + ' cards remaining')

				if pushup_or_pullups(num_to_do) == 'pull-ups':
					players[k].pullups_done += num_to_do
				else:
					players[k].pushups_done += num_to_do
				players[k].cards_done += 1
				players[k].multiplying_factor = 1

			input('') #read_single_keypress()
	return get_scores(players, get_database())

def get_database():
	jsonFile = open("data.json", "r+")
	data = json.load(jsonFile)
	jsonFile.close()

	return data

def clear_database():
	jsonFile = open("data.json", "r+")
	data = json.load(jsonFile)
	jsonFile.close()

	data.clear()
	
	jsonFile = open('data.json', 'w+')
	jsonFile.write(json.dumps(data))
	jsonFile.close()

def get_scores(players, database):

	for x in range(len(players)):

		name = players[x].name
		pushups = players[x].pushups_done
		pullups = players[x].pullups_done
		cards = players[x].cards_done


		if name in database:
			database[name][0] += players[x].pushups_done #pushups
			database[name][1] += players[x].pullups_done #pullups
			database[name][2] += players[x].cards_done #cards done
			#first_date = database[name][3]

			current_player = database[players[x].name]
			print(Style.BRIGHT + Fore.YELLOW + name, Fore.RED + '-', pushups, 'push-ups |', pullups, 'pull-ups -', Fore.CYAN + '', cards, 'cards')
			#print(Style.BRIGHT + Fore.CYAN + 'Since: ' + Fore.GREEN + first_date.strftime("%A %d. %B %Y"), Fore.Red + ': ' + get_date() - first_date + 'have elapsed' )
			print(Style.BRIGHT + Fore.GREEN + 'TOTAL: ', Fore.RED + '', current_player[0], 'push-ups |', current_player[1], 'pull-ups -',  Fore.CYAN + '', current_player[2], 'cards')

			
		else:
			database[players[x].name] = [players[x].pushups_done,
										players[x].pullups_done,
										players[x].cards_done#,
										#get_date()
										]

			print(Style.BRIGHT + Fore.YELLOW + name, Fore.RED + '-', pushups, 'push-ups |', pullups, 'pull-ups -', Fore.CYAN + '', cards, 'cards')
			print(Style.BRIGHT + Fore.GREEN + 'Today: ' + get_date().strftime("%A %d. %B %Y"))

		input('') #read_single_keypress()

	jsonFile = open('data.json', 'w+')
	jsonFile.write(json.dumps(database))
	jsonFile.close()

	reset_deck() #Reload deck for another game

	print(Fore.RESET + Style.RESET_ALL + Back.RESET)

def play(number_of_players, game=push_ups):
	players = make_players(number_of_players)
	return game(number_of_players, players)

def reset_deck():
	Player.main_deck = shuffle_deck()

def get_date():
	today_date = datetime.date.today()
	return today_date

class Player:
	main_deck = shuffle_deck()
	def __init__(self, name):
		self.name = name
		self.pushups_done = 0
		self.pullups_done = 0
		self.double = False
		self.multiplying_factor = 1
		self.cards_done = 0

print(Fore.CYAN + Style.BRIGHT)
play(int(input('How many people are playing? (Must be an interger) ')))