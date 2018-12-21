import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    # load a list of words from the file 'words.txt'.
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    # choose a word from the list loaded before.
    return random.choice(wordlist)

wordList = loadWords()
chooseWord(wordList)

def isWordGuessed(secretWord, lettersGuessed):
    List = list(secretWord)
    if set(List) == set(lettersGuessed):
        return True
    else:
        return False
# test isWordGuessed.
#isWordGuessed('apple', ['a','l','p'])
#isWordGuessed('apple', ['a','l','p','e'])

def getGuessedWord(secretWord, lettersGuessed):
    # check and show letters you guessed.
    List = list(secretWord); show_word = ''
    for i in List:
        if i in lettersGuessed:
            show_word += i
        else:
            show_word += '_'
    show_word = " ".join(show_word)
    return show_word
# test getGuessedWord.
#getGuessedWord('apple', ['a','l','k'])

def getAvailableLetters(lettersGuessed):
    # check and show letters you entered.
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    List = list(alphabet); show_word = ''
    for i in List:
        if i in lettersGuessed:
            show_word += '_'
        else:
            show_word += i
    show_word = " ".join(show_word)
    return show_word
# test getAvailableLetters.
#getAvailableLetters(['a','b','c','p','z'])

def hangman(secretWord):
    length = len(secretWord); entered_letters = []; yourWord = []; count = 8;
    print("There are {0} letters in here.".format(length))
    while count :
        x, y = 0, 0
        print("\n")
        letter = input("Guess a letter: ")
        if (letter in secretWord) and (len(letter) == 1):
            x = 1
        if letter in entered_letters:
            y = 1
        if y == 0:
            entered_letters += [letter]
        if (x == 1) and (y == 0):
            yourWord += [letter]
        if (x == 0) and (y == 0):
            count += -1
        print("You have {0} guesses left".format(count))
        print("Available letters: " + getAvailableLetters(entered_letters))
        if (x == 1) and (y == 0):
            print("Good guess: " + getGuessedWord(secretWord,entered_letters))
        elif y == 1:
            print("You have already guessed this letter.\nPlease guess another letter: " + getGuessedWord(secretWord,entered_letters))
        else:
            if len(letter) > 1:
                print("Please enter only one letter")
            print("You missed: " + getGuessedWord(secretWord,entered_letters))
        if isWordGuessed(secretWord,yourWord) == True:
            break
    if isWordGuessed(secretWord,yourWord) == True:
        print("\nYou won!")
    else:
        print("\nYou lose...\nThe answer is " + secretWord)
# .lower makes word lower.
secretWord = chooseWord(wordList).lower()
#print(secretWord)
# start hangman game.
hangman(secretWord)