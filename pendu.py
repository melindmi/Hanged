from fonctions import *
from donnees import *
from random import choice

name = getName()	
print("Your name is: ", name)

mot = choice(mots)
cach_mot = printCachMot(mot)
#print(mot)
rest_mot = mot

nb = 0
bingo = False
while(not bingo and nb < max_essayes):
	letter = getLetter()
	isFound = found(letter, rest_mot)
	if isFound:
		print(":) Bravo!")
		position = foundPosition(letter,rest_mot)
		cach_mot = getNewCachMot(letter, position, cach_mot)
		rest_mot = getRestMot(position, rest_mot)
		if cach_mot == mot:
			bingo = True
			print("Bingo!!!!")
		print(cach_mot)
	else:
		nb = nb + 1
		print(":( Not good, try again. You have ", max_essayes-nb, " tries left!")
		if(max_essayes == nb):
			print("Bye, bye!")
	
