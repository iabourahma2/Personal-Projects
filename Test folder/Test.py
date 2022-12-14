import random

print("Welcome to the Fifa world cup Hangman!")
print("Last name of players only. GOOD LUCK!")
print("------------------------------------------------")
worddictionary = ["messi" , "martinez", "alvarez", "ronaldo", "kane", "neymar", "muller","mbappe","modric","lewandowski","pedri","ibrahimovic","ibs", "griezmann" ,"valverde","cancelo","vitinha","fernandes","dias","giroud","lloris","tchoameni","dembele","neuer","ginter","gunter","havertz","moukoko","adeyemi","bale","roberts","morrell","sanchez","martin","jimenzez","pogba","riberey","rues","cash","zalewski","kyrchowiak","milik","estrada","valencia","reasco","rodrigues","ake","timber","simons","depay","muneer","alaaeldin","dieng","sarr","gueye","maguire","stones","rice","sterling","pouraliganji","jalali","azmoun","sargent","weah","wright","rodon","mepham","ramsey","nassem","moore","golwi"]

randoword = random.choice(worddictionary)

for x in randoword:
    print("_", end=" ")

def print_hangman(wrong):
    if(wrong == 0):
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ====")
    elif(wrong == 1):
        print("\n+---+")
        print(" o    |")
        print("      |")
        print("      |")
        print("     ====")
    elif(wrong == 2):
        print("\n+---+")
        print(" o    |")
        print(" |    |")
        print("      |")
        print("    ====")
    elif(wrong == 3):
        print("\n+---+")
        print(" o    |")
        print(" |\   |")
        print("      |")
        print("     ====")
    elif(wrong == 4):
        print("\n+---+")
        print(" o    |")
        print("/|\   |")
        print("      |")
        print("     ====")
    elif(wrong == 5):
        print("\n+---+")
        print(" o    |")
        print("/|\   |")
        print("/     |")
        print("    ====")
    elif(wrong == 6):
        print("\n+---+")
        print(" o    |")
        print("/|\  |")
        print("/ \  |")
        print("    ====")

def printword(guessedletters):
    counter=0
    rightletters=0
    for char in randoword:
        if char in guessedletters:
            print(randoword[counter], end=" ")
            rightletters+=1
        else:
            print(" ", end=" ")
        counter+=1
    return rightletters

def printlines():
    print("\r")
    for char in randoword:
        print("\u203E", end=" ")

lengthofwordtoguess = len(randoword)
amountwrong = 0
curretguess = 0
currentlettersguessed = []
currentlettersright = 0

while(amountwrong != 6 and currentlettersright != lengthofwordtoguess):
    print("\nLetters guessed so far: ")
    for letter in currentlettersguessed:
        print(letter, end=" ")
        #prompt input for user
    letterguessed = input("\nGuess a letter: ")
    #check if  right
    #if(randoword[curretguess] in letterguessed):
    if(letterguessed in randoword):
        print_hangman(amountwrong)
        #PRINT THE WORD!!!!!!!!!!!
        curretguess+=1
        currentlettersguessed.append(letterguessed)
        currentlettersright = printword(currentlettersguessed)
        printlines()
        #dude was wrong
    else:
        if(letterguessed not in randoword):
            amountwrong = amountwrong + 1
            print_hangman(amountwrong)
        currentlettersguessed.append(letterguessed)
        #update drwing brooooooo
        #print word
        currentlettersright = printword(currentlettersguessed)
        printlines()
print("Game is over thanks for playing!")
print("word was: ",randoword)