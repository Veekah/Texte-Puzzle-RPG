####################################################
# Coder dans Python 3.5.0 #
####################################################
import cmd
import textwrap
import sys
import os
import time
import random
screen_width = 200

#################
# Joueur Donnée #
#################

class player:
    def __init__(self):
        self.nom = ''
        self.ressenti = ''
        self.astrologique = ''
        self.position = 'Millieu'
        self.gagner = False
        self.resolu = 4
player1 = player()


#############################
# COnfiguration de la carte	#
#############################

#Création des variable constante
DESCRIPTION = 'description'
INFO = 'info'
PUZZLE = 'puzzle'
RESOLU = False
SIDE_UP = 'monter'
SIDE_DOWN = 'descendre'
SIDE_LEFT = 'gauche',
SIDE_RIGHT = 'droite',

piece_resolu = {'Haut': False, 'Nord': False, 'Millieu': False, 'Est': False, 'Ouest': False, 'Sud': False,}

cube = {
	'Haut': {
		DESCRIPTION: "Vous avez beaucoup voyager et vous êtes maintenant fatigué...\nCependant, vous voyez au loin un village qui semble animé et qui pourrait beaucoup vous aider...",
		INFO: "Vous entrez dans le Village, et encore plus étrange que de se tenir sur les nuages, un\noiseau commence à vous pointer de l'aile une stèle.\n",
		PUZZLE: "Cette stèle est un engrenage qui semble avoir besoin d'un certain nombre de rotation.\nUne pencarte affiche ces symboles :'(10100) indice 2' Ces signe doivent donc représenter un chiffre, mais lequel?",
		RESOLU: "20 en base 2",
		SIDE_UP: 'Nord',
		SIDE_DOWN: 'Sud',
		SIDE_LEFT: 'Est',
		SIDE_RIGHT: 'Ouest',
	},
	'Nord': {
		DESCRIPTION: "Vous vous trouvez maintenant dans un endroit glacial.\nUn feu de camp brille a coté d'un grotte.",
		INFO: "Vous vous tenez face a face avec un géant Yéti qui ne parle pas votre dialecte.\n(Si vous ne comprenez pas ce langage, une traduction est diaponible ligne 56 :).) ", #Quel est le nom de ce langage?
		PUZZLE: "Le Yeti s'exprime : 01010001 01110101 01100101 01101100\n00100000 01100101 01110011 01110100\n00100000 01101100 01100101 00100000\n01101110 01101111 01101101 00100000\n01100100 01100101 00100000 01100011\n01100101 00100000 01101100 01100001\n01101110 01100111 01100001 01100111\n01100101 00111111",
		RESOLU: "binaire",
		SIDE_UP: 'Haut',
		SIDE_DOWN: 'Millieu',
		SIDE_LEFT: 'Ouest',
		SIDE_RIGHT: 'Est',
	},
	'Millieu': {
		DESCRIPTION: "Vous vous retrouvez dans un champ assez joli et générique.\nQuelque chose ne va pas, comme si c’était le cœur du monde.",
		INFO: "Une clé dorée assez grande, bien que facilement invisible,\nse dresse à la verticale sur le terrain.\nComme c’est étrange.",
		PUZZLE: "La clé se trouve à l’intérieur d’un trou de serrure de taille respective \n masqué par la terre et l’herbe. Elle ne semble pas tourner.",
		RESOLU: False, #fonctionnera quand on aura résolu tout les puzzles.
		SIDE_UP: 'Nord',
		SIDE_DOWN: 'Sud',
		SIDE_LEFT: 'Ouest',
		SIDE_RIGHT: 'Est',
	},
	'Ouest': {
		DESCRIPTION: 'Vous vous retrouvez entouré de vents forts et de dunes de sable.',
		INFO: 'Un homme terrifié se cache parmi des cactus.',
		PUZZLE: "L’homme craintif demande :\n « Qu’est-ce qui peut mesurer le temps, alors que tout finit par s’effondrer? »'",
		RESOLU: "le sable",
		SIDE_UP: 'Nord',
		SIDE_DOWN: 'Sud',
		SIDE_LEFT: 'Haut',
		SIDE_RIGHT: 'Millieu',
	},
	'Est': {
		DESCRIPTION: "Vous vous retrouvez dans des forêts luxuriantes, regorgeant de faune et de gazouillis.",
		INFO: "Un homme d’apparence rugueuse est assis à côté d’une petite cabane. Ses oreilles sont collés à un sonotonne.",
		PUZZLE: "L’homme d’apparence rugueuse demande, n 'A quelle vitesse me parvient le son du vent?'",
		RESOLU: "340 m/s",
		SIDE_UP: 'Nord',
		SIDE_DOWN: 'Sud',
		SIDE_LEFT: 'Millieu',
	},
	'Sud': {
		DESCRIPTION: "Vous vous trouvez à côté d’un étang immobile et apaisant.\nUn vieil homme regarde une table à proximité.",
		INFO: "Vous saluez le vieil homme.\nIl vous invite à regarder la table complexe à douze côtés.",
		PUZZLE: "Chaque cotés de la table a un unique symbole, Il vous semble tous familier.\nQuel signe allez vous choisir?",
		RESOLU: "",#Doit être votre signe astrologique.
		SIDE_UP: 'Millieu',
		SIDE_DOWN: 'Haut',
		SIDE_LEFT: 'Ouest',
		SIDE_RIGHT: 'Est',
	}
}


################
# Title Screen #
################
def ecran_titre_option():
	option = input("> ")
	if option.lower() == ("jouer"):
		setup_game()
	elif option.lower() == ("quitter"):
		sys.exit()
	elif option.lower() == ("aide"):
		menu_aide()
	while option.lower() not in ['jouer', 'aide', 'quitter']:
		print("Commande invalide, réessayer.")
		option = input("> ")
		if option.lower() == ("jouer"):
			setup_game()
		elif option.lower() == ("quitter"):
			sys.exit()
		elif option.lower() == ("aide"):
			menu_aide()

def ecran_titre():
	os.system('cls')

	print('#' * 45)
	print('#  _____          _       __    ___  ___     #')
	print('# /__   \_____  _| |_    /__\  / _ \/ _ \    #')
	print('#   / /\/ _ \ \/ / __|  / \// / /_)/ /_\/    #')
	print('#  / / |  __/>  <| |_  / _  \/ ___/ /_\\     #')
	print('#  \/   \___/_/\_\\__| \/ \_/\/   \____/     #')
	print('#' * 45)
	print('#        Bienvenue sur ce Puzzle-RPG        #')
	print("#    Copyright - Veekah - Alpha-Project!    #")
	print('#' * 45)
	print("                 .:  Jouer  :.                  ")
	print("                 .:   Aide  :.                  ")
	print("                 .: Quitter :.                  ")
	ecran_titre_option()


################
#  Menu d'aide #
################
def menu_aide():
	print("")
	print('#' * 45)
	print("             Copyright - Veekah             ")
	print("            Alpha Version (0.0.1)           ")
	print("~" * 45)
	print("- Vous pouvez utiliser la commande 'voyager'\n suivi du lieu souhaiter 'nord' par exemple")
	print("  Afin vous déplacer et essayer de sortir de\n cet boucle temporel.\n")
	print("- Vous pouvez utiliser la commande 'regarder' ou\n 'examiner'")
	print("  Cette dernière vous permettra d'intéragir\n avec la salle en question.\n")
	print("- Pour vous évader de cette boucle, vous aurez\n besoin de différentes intéraction avec la Console")
	print("  une certaine culture général vous sera donc\n requise, mais surtout de bon raisonnement.\n")
	print("- Enfin, les réponse attendu n'ont pas besoin\n de majuscule, pour plus de facilité.\n")
	print('#' * 45)
	print("\n")
	print('#' * 45)
	print("    Selectionner une action pour continuer.     ")
	print('#' * 45)
	print("                 .:  Jouer  :.                ")
	print("                 .:  Aide   :.                ")
	print("                 .: Quitter :.                ")
	ecran_titre_option()


#################
# Position Jeu  #
#################
quitgame = 'quit'

def afficher_localisation():

	print('\n' + ('#' * (4 +len(player1.position))))
	print('# ' + player1.position.upper() + ' #')
	print('#' * (4 +len(player1.position)))
	print('\n' + (cube[player1.position][DESCRIPTION]))

def demande():
	if player1.resolu == 5:
		print("Quelque choses dans le monde semble avoir changé. Hmm...")
	print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("Que voulez-vous faire?")
	action = input("> ")
	acceptable_actions = ['voyager', 'aller', 'marcher', 'quitter', 'inspecter', 'examiner', 'chercher']
	#Forces the player to write an acceptable sign, as this is essential to solving a puzzle later.
	while action.lower() not in acceptable_actions:
		print("Votre commande est éronner, réessayer.\n")
		action = input("> ")
	if action.lower() == quitgame:
		sys.exit()
	elif action.lower() in ['voyager', 'aller', 'marcher']:
		mouvement(action.lower())
	elif action.lower() in ['inspecter', 'examiner', 'regarder', 'chercher']:
		examine()

def mouvement(Mon_Action):
	askString = "Ou voulez-vous "+Mon_Action+"?\n> "
	destination = input(askString)
	if destination == 'nord':
		mouvement_destination = cube[player1.position][SIDE_UP] #if you are on ground, should say north
		mouvement_joueur(mouvement_destination)
	elif destination == 'ouest':
		mouvement_destination = cube[player1.position][SIDE_LEFT]
		mouvement_joueur(mouvement_destination)
	elif destination == 'est':
		mouvement_destination = cube[player1.position][SIDE_RIGHT]
		mouvement_joueur(mouvement_destination)
	elif destination == 'sud':
		mouvement_destination = cube[player1.position][SIDE_DOWN]
		mouvement_joueur(mouvement_destination)
	else:
		print("Action invalide Voyageur... Essayer de vous déplacer pour résoudre d'autres enigmes pour vous évader de ces lieux...\n")
		mouvement(Mon_Action)

def mouvement_joueur(mouvement_destination):
	print("\nVous vous êtes déplacer vers l'/le " + mouvement_destination + ".")
	player1.position = mouvement_destination
	afficher_localisation()

def examine():
	if piece_resolu[player1.position] == False:
		print('\n' + (cube[player1.position][INFO]))
		print((cube[player1.position][PUZZLE]))
		puzzle_reponse = input("> ")
		verifier_puzzle(puzzle_reponse)
	else:
		print("Il n'y a rien de nouveau dans cette zone...")

def verifier_puzzle(puzzle_reponse):
	if player1.position == 'Millieu':
		if player1.resolu >= 5:
			discourt_fin = ("Without you having done anything, the key begins to rotate.\nIt begins to rain.\nAll of the sides of the box begin to crumble inwards.\nLight begins to shine through the cracks in the walls.\nA blinding flash of light hits you.\nYou have escaped!")
			for character in discourt_fin:
				sys.stdout.write(character)
				sys.stdout.flush()
				time.sleep(0.05)
			print("\nFELICITATION !")
			sys.exit()
		else:
			print("Rien ne semble se produire...")
	elif player1.position == 'Sud':
		if puzzle_reponse == (player1.astrologique):
			piece_resolu[player1.position] = True
			player1.resolu += 1
			print("Vous avez résolu l'énigme. Continuons !")
			print("\nEnigme Résolus : " + str(player1.resolu))
		else:
			print("Mauvaise réponse ! Réessayer.\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
			examine()
	else:
		if puzzle_reponse == (cube[player1.position][RESOLU]):
			piece_resolu[player1.position] = True
			player1.resolu += 1
			print("Vous avez résolu l'énigme. Bravo !")
			print("\nEnigme Résolu: " + str(player1.resolu))
		else:
			print("Mauvaise réponse ! Réessayer.\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
			examine()

def main_game_loop():
	total_puzzles = 6
	while player1.gagner is False:
		#print_location()
		demande()


################
# Execute Game #
################
def setup_game():
	#Supprimer l'historique CMD.
	os.system('cls')

	#QUESTION NOM : Obtenir le nom du joueur.
	question1 = "Bonjour voyageur, quel est votre nom?\n"
	for character in question1:
		#This will occur throughout the intro code.  It allows the string to be typed gradually - like a typerwriter effect.
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	player_nom = input("> ")
	player1.nom = player_nom

	#QUESTION RESSENTI: Obtenir le ressenti du joueur.
	question2 = "Bien, mon chère " + player1.nom + ", comment allez-vous?\n"
	for character in question2:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	ressenti = input("> ")
	player1.ressenti = ressenti.lower()

	#Création de liste d'adjectif pour les ressentis.
	good_adj = ['good', 'great', 'rohit', 'happy', 'aight', 'understanding', 'great', 'alright', 'calm', 'confident', 'not bad', 'courageous', 'peaceful', 'reliable', 'joyous', 'energetic', 'at', 'ease', 'easy', 'lucky', 'k', 'comfortable', 'amazed', 'fortunate', 'optimistic', 'pleased', 'free', 'delighted', 'swag', 'encouraged', 'ok', 'overjoyed', 'impulsive', 'clever', 'interested', 'gleeful', 'free', 'surprised', 'satisfied', 'thankful', 'frisky', 'content', 'receptive', 'important', 'animated', 'quiet', 'okay', 'festive', 'spirited', 'certain', 'kind', 'ecstatic', 'thrilled', 'relaxed', 'satisfied', 'wonderful', 'serene', 'glad', 'free', 'and', 'easy', 'cheerful', 'bright', 'sunny', 'blessed', 'merry', 'reassured', 'elated', '1738', 'love', 'interested', 'positive', 'strong', 'loving']
	hmm_adj = ['idk', 'concerned', 'lakshya', 'eager', 'impulsive', 'considerate', 'affected', 'keen', 'free', 'affectionate', 'fascinated', 'earnest', 'sure', 'sensitive', 'intrigued', 'intent', 'certain', 'tender', 'absorbed', 'anxious', 'rebellious', 'devoted', 'inquisitive', 'inspired', 'unique', 'attracted', 'nosy', 'determined', 'dynamic', 'passionate', 'snoopy', 'excited', 'tenacious', 'admiration', 'engrossed', 'enthusiastic', 'hardy', 'warm', 'curious', 'bold', 'secure', 'touched', 'brave', 'sympathy', 'daring', 'close', 'challenged', 'loved', 'optimistic', 'comforted', 're', 'enforced', 'drawn', 'toward', 'confident', 'hopeful', 'difficult']
	bad_adj = ['bad', 'meh', 'sad', 'hungry', 'unpleasant', 'feelings', 'angry', 'depressed', 'confused', 'helpless', 'irritated', 'lousy', 'upset', 'incapable', 'enraged', 'disappointed', 'doubtful', 'alone', 'hostile', 'discouraged', 'uncertain', 'paralyzed', 'insulting', 'ashamed', 'indecisive', 'fatigued', 'sore', 'powerless', 'perplexed', 'useless', 'annoyed', 'diminished', 'embarrassed', 'inferior', 'upset', 'guilty', 'hesitant', 'vulnerable', 'hateful', 'dissatisfied', 'shy', 'empty', 'unpleasant', 'miserable', 'stupefied', 'forced', 'offensive', 'detestable', 'disillusioned', 'hesitant', 'bitter', 'repugnant', 'unbelieving', 'despair', 'aggressive', 'despicable', 'skeptical', 'frustrated', 'resentful', 'disgusting', 'distrustful', 'distressed', 'inflamed', 'abominable', 'misgiving', 'woeful', 'provoked', 'terrible', 'lost', 'pathetic', 'incensed', 'in', 'despair', 'unsure', 'tragic', 'infuriated', 'sulky', 'uneasy', 'cross', 'bad', 'pessimistic', 'dominated', 'worked', 'up', 'a', 'sense', 'of', 'loss', 'tense', 'boiling', 'fuming', 'indignant', 'indifferent', 'afraid', 'hurt', 'sad', 'insensitive', 'fearful', 'crushed', 'tearful', 'dull', 'terrified', 'tormented', 'sorrowful', 'nonchalant', 'suspicious', 'deprived', 'pained', 'neutral', 'anxious', 'pained', 'grief', 'reserved', 'alarmed', 'tortured', 'anguish', 'weary', 'panic', 'dejected', 'desolate', 'bored', 'nervous', 'rejected', 'desperate', 'preoccupied', 'scared', 'injured', 'pessimistic', 'cold', 'worried', 'offended', 'unhappy', 'disinterested', 'frightened', 'afflicted', 'lonely', 'lifeless', 'timid', 'aching', 'grieved', 'shaky', 'victimized', 'mournful', 'restless', 'heartbroken', 'dismayed', 'doubtful', 'agonized', 'threatened', 'appalled', 'cowardly', 'humiliated', 'quaking', 'wronged', 'menaced', 'alienated', 'wary']

	#Donner une réponse précise en fonction du ressenti.
	if player1.ressenti in good_adj:
		feeling_string = "je suis désolé que vous vous sentiez"
	elif player1.ressenti in hmm_adj:
		feeling_string = "c'est intéréssant que vous vous sentiez"
	elif player1.ressenti in bad_adj:
		feeling_string = "je suis désolé de vous savoir"
	else:
		feeling_string = "je ne sais pas ce que ca fais de se sentir"

	#Combiner toutes les parties récoltés.
	question3 = "Je vois, " + player1.nom + ", " + feeling_string + " " + player1.ressenti + ".\n"
	for character in question3:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)

	#QUESTION SIGN: Obtains the player's astrological sign for a later puzzle.
	question4 = "Maintenant dis moi, quel est ton signe astrologique?\n"
	for character in question4:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)

	#Prints the astrological sign guide for the player.  Also converts text to be case-insensitive, as with most inputs.
	print("#####################################################")
	print("# Please print the proper name to indicate your sign.")
	print("# ♈ Aries")
	print("# ♉ Taureau")
	print("# ♊ Gemeau")
	print("# ♋ Cancer")
	print("# ♌ Lion")
	print("# ♍ Vierge")
	print("# ♎ Balance")
	print("# ♏ Scorpion")
	print("# ♐ Sagitaire")
	print("# ♑ Capricorne")
	print("# ♒ Aquarius")
	print("# ♓ Poisson")
	print("#####################################################")
	astrologique = input("> ")
	acceptable_signs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']
	#Forces the player to write an acceptable sign, as this is essential to solving a puzzle later.  Also stores it in class.

	while astrologique.lower() not in acceptable_signs:
		print("Ce signe n'existe pas, Ressayer, s'il vous plait.")
		astrologique = input("> ")
	player1.astrologique = astrologique.lower()

	#Leads the player into the cube puzzle now!
	speech1 = "Oh, " + player1.astrologique + ", intéréssant. Je garde précieusement cette information...\nElle pourrait être très utile dans un futur proche...  Cependant,\n"
	speech2 = "Il semble que c’est ici que nous devons nous séparer, " + player1.nom + ".\n"
	speech3 = "Malheureusement...\n"
	speech4 = "Oh, vous ne savez pas ou vous vous trouvez?  Je vois...\n"
	speech5 = "Heureusement, je peux vous conseillez de vous rendre au village le plus proche...\n"
	speech7 = "J'espère que vous arriverez à retrouver votre chemin...\n"
	speech6 = "Heh. Heh.. Heh...\n"
	for character in speech1:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	for character in speech2:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	for character in speech3:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.1)
	for character in speech4:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	for character in speech5:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	for character in speech7:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	for character in speech6:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.2)
	time.sleep(1)

	os.system('cls')
	print("                        #############################################                                 ")
	print("                        # Ici commence votre adventure, Voyageur... #                                 ")
	print("                        #############################################\n                               ")
	print("Vous vous trouvez au centre d’un endroit étrange. On dirait que vous êtes coincé dans une petite boîte.\n    ")
	print("Chaque face intérieure de la boîte semble avoir un thème différent. Comment pouvez-vous sortir de cet endroit...\n       ")
	print("Vous remarquez des objets debout de côté sur les murs. La gravité ne s’applique pas? Il y a des nuages cependant...")
	main_game_loop()


ecran_titre()
