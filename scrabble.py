def scrabble_score(word):
    retValue = 0
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
             "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
             "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
             "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
             "x": 8, "z": 10}
    for x in range(len(word)):
        for a in score:
            if word[x].lower() == a:
                retValue += score[a]
    return retValue
print ("Disclaimer: 0 to exit")
keepGoing = True
while (keepGoing == True):
    word = input("Enter a word you would like to calculate: ")
    if word == "0":
        keepGoing = False
    else:
        print (str(scrabble_score(word)))