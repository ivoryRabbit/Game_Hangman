from ps3_hangman import loadWords, chooseWord

# In[]
wordList = loadWords()

chooseWord(wordList)

# In[]

def isWordGuessed(secretWord, lettersGuessed):
    L = [];
    for i in secretWord:
        L += [i]
    if set(L) == set(lettersGuessed):
        return True
    else:
        return False

# In[]

isWordGuessed('apple', ['a','l','p'])

# In[]

isWordGuessed('apple', ['a','l','p','e'])

# In[]

def getGuessedWord(secretWord, lettersGuessed):
    L = []; w = ''
    for i in secretWord:
        L += [i]
    for j in L:
        if j in lettersGuessed:
            w += j
        else:
            w += '_'
    return w

# In[]

getGuessedWord('apple', ['a','l','k'])

# In[]

def getAvailableLetters(lettersGuessed):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    L = []; w = ''
    for i in alphabet:
        L += [i]
    for j in L:
        if j in lettersGuessed:
            w += '_'
        else:
            w += j
    return w

# In[]

getAvailableLetters(['a','b','c','p','z'])

# In[]

def hangman(secretWord):
    l = 0; L = []; M = []; c = 8; x = 0; y = 0
    for i in secretWord:
        l += 1
    print("There are " + str(l) + " letters in here.")
    while c > 0:
        print("\n")
        A = input("Guess a letter: ")
        if A not in secretWord:
            x = 0
        else:
            x = 1
        if A not in L:
            y = 1
        else:
            y = 0
        if y == 1:
            L += [A]
        if (x == 1) and (y == 1):
            M += [A]
        if (x == 0) and (y == 1):
            c += -1
        print("You have " + str(c)+ " guesses left")
        print("Available letters: " + getAvailableLetters(L))
        if (x == 1) and (y == 1):
            print("Good guess: " + getGuessedWord(secretWord,L))
        elif y == 0:
            print("You have already guessed this letter. Please guess another letter: " + getGuessedWord(secretWord,L))
        else:
            print("You missed: " + getGuessedWord(secretWord,L))
        if isWordGuessed(secretWord,M) == True:
            break
    if isWordGuessed(secretWord,M) == True:
        print("\n")
        print("You won!")
    else:
        print("\n")
        print("You lose...")
        print("The answer is " + str(secretWord))

# In[]

secretWord = chooseWord(wordList).lower()

# In[]

hangman(secretWord)