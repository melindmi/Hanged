def getName():
	name = input("Enter your name: ")
	return name


def getLetter():
	letter = input("Give a letter: ")
	return letter 

def found(letter, mot):
	if letter in mot:
		return True 
	else:
		return False

def foundPosition(letter, mot):
	return mot.find(letter)

def getNewCachMot(letter, position, cach_mot ):
	newmot = cach_mot[0:position] + letter + cach_mot[position+1:]
	return newmot

def getRestMot(position, mot):
	restmot = mot[0:position] + '*' + mot[position+1:]
	return restmot

def printCachMot(mot):
	cach_mot=''
	for i in mot:
		cach_mot += "*"
	print(cach_mot)
	return cach_mot	
		
