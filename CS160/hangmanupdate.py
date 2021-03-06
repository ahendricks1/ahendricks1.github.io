import random

def makeArt():
    art = []
    art.append('         +---------+')
    art.append('         |         |')
    art.append('                   |')
    art.append('                   |')
    art.append('                   |')
    art.append('                   |')
    art.append('                   |')
    art.append(' ------------------+')
    return art

def readWords():
    wordList = []
    with open('wordlist.10000.txt') as wordFile:
        count = 0
        for line in wordFile:
            if len(line) > 4 and len(line) < 7:
                wordList.append(line[0:-1])
            
    return wordList

def printArt(art):
    for line in art:
        print(line)
        
def setParts():
    parts = {
        1 : head,
        2 : body,
        3 : leftArm,
        4 : rightArm,
        5 : leftLeg,
        6 : rightLeg,
        7 : placeholder,
        }
    return parts

def head(art):
    art.insert(2, '       +---+       |');
    art.insert(2, '       +   +       |');
    art.insert(2, '       +---+       |');

def body(art):
    art.insert(5, '      +-----+      |');
    art.insert(5, '      +     +      |');
    art.insert(5, '      +     +      |');
    art.insert(5, '      +     +      |');
    art.insert(5, '      +-----+      |');
    art.insert(5, '         +         |');

def leftArm(art):
    art[6] = '    --+-----+      |';
    art[7] = '   +  +     +      |';
    art[8] = '  +   +     +      |';
    art[9] = ' +    +     +      |';
    

def rightArm(art):
    art[6] = '    --+-----+--    |';
    art[7] = '   +  +     +  +   |';
    art[8] = '  +   +     +   +  |';
    art[9] = ' +    +     +    + |';

def leftLeg(art):
    art[11] = '        +          |';
    art[12] = '       +           |';
    art[13] = '      +            |';

def rightLeg(art):
    art[11] = '        +  +       |';
    art[12] = '       +    +      |';
    art[13] = '      +      +     |';

def placeholder(art):
    art.insert(13, '');
    
def init():
    bodyParts = setParts()
    art = makeArt()
    word = readWords()
    return bodyParts, art, word

count = 0

bodyParts, art, words = init()
    
printArt(art)

def insertLetter(spaces, letter, pos):
    pos = pos * 2
    spaces = spaces[0:pos] + letter + spaces[pos + 1:]
    return spaces

word = random.choice(readWords())
word = list(word)
print(word)
spaces = "_ " * len(word)

#main loop
'''
for i in range(len(word)):
'''
youWon = "1" * len(word)
youWon = list(youWon)

while word != youWon and count != 6:
    guess = input("Letter? ")
    
    if guess not in word:
        count = count + 1
        misses = count
        bodyParts[misses](art)
        
    for i in range(len(word)):
    
        if guess == word[i]:
            pos = word.index(guess)
            spaces = insertLetter(spaces, guess, pos)
            word[i] = "1"
            print(word)
            
    print(count)
    if youWon == word:
        print("You win!")
    printArt(art)
    print(spaces)
    if count == 6:
        print("You lose! :(")
