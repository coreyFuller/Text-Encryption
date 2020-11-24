import random as r
from os import listdir as dir

def encrypt(filename, shift):
    f1 = open(filename, "r")
    f2= open("encrypted.txt", "w")
    word = f1.read().lower()
    for letter in word:
        if letter.isalpha():
            if ord(letter) + shift <= 122:
                new_letter = chr((ord(letter) + shift))
            else:
                new_letter = chr((ord(letter) - 26+ shift))
            f2.write(new_letter)
        else:
            f2.write(letter)         
    pass
    

def decrypt(filename):
    letters = {}
    f = open(filename, "r")
    text = f.read()
    for letter in text:
        if letter.isalpha():
            if letter not in letters.keys():
                letters[letter] = 1
            else:
                letters[letter] += 1 
    most = max(letters, key= letters.get)
    diff = ord(most) - ord("e")
    for letter in text:
        if letter.isalpha():
                if ord(letter) - diff < 97:
                    new_letter = chr((ord(letter) - diff) + 26)
                else:
                    new_letter = chr((ord(letter) - shift))
                print(new_letter, end = "")
        else:
            print(letter, end = "")   
    pass


def getTextFile():
    files = [ x for x in dir() if ".txt" in x]
    random_index = r.randint(0, len(files) - 1)
    return files[random_index]


shift = r.randint(3, 11)
filename = getTextFile()
encrypt(filename, shift)
decrypt("encrypted.txt")