#Copyright 2025 Algrythm/Mars Cannon
#Eng Dictionary from https://github.com/goldstraw/CommonEnglishDictionary

import random
import os
import threading
import time

vowels = ["a","e","i","o","u"]
consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","r","s","t","v","w","x","y"]
words = []
englishtrans = []
generated = 0
name = None
choice4 = None

def progress():
    while True:
        os.system('cls')
        print("Please wait, this may take a moment! Translating ~61k common English words to your language.")
        print(f"{generated}/~61000 generated.")
        time.sleep(1)
        if generated > 57000:
            os.system('cls')
            print("Finishing up... Please wait...")
            break


while True:
    os.system('cls')
    print("""~~~~~~~~
Welcome to Algrythm's Language Generator!
Generate new languages to use in your projects, or just for fun!
~~~~~~~~\n""")
    choice3 = input("Enter 1 to load an existing language file (.lang), 2 to make a new one: ")

    if choice3 == "1" or choice3 == "2":
        break
    else: 
        os.system('cls')
        print("That is not a valid option!")
        os.system('pause')
if choice3 == "2":
    os.system('cls')
    name = input("Enter the name of your new language: ")
    while True:
        os.system('cls')
        choice5 = input("Enter 1 to use the latin alphabet with optionally added new vowels, or 2 to use a different alphabet entirely: ")
        if choice5 == "1" or choice5 == "2":
            break
        else:
            os.system('cls')
            print("That is not a valid option!")
            os.system('pause')
    if choice5 == "1":
        extravowels = input("Enter extra vowel characters to add to the alphabet, spaced out with a space between each character (OPTIONAL, LEAVE BLANK IF NONE): ").lower()
        for vowel in extravowels.split():
            vowels.append(vowel)
    else:
        vowels = []
        consonants = []
        newVowels = input("Enter the list of your chosen alphabet's vowels, inputted with a space between each one: ").lower()
        newCon = input("Enter the list of your chosen alphabet's consonants, inputted with a space between each one: ").lower()
        for vowel in newVowels.split():
            vowels.append(vowel)
        for con in newCon.split():
            consonants.append(con)
    os.system('cls')
    print("Alphabet creation complete!")
    os.system('pause')
else:
    os.system('cls')
    while True:
        choice4 = input("Enter the name of your language you want to load (*excluding the .lang at the end of the file name): ").lower()
        try:
            lang = open(f"./languages/{choice4}.lang",'r', encoding="utf-8")
            break
        except:
            os.system('cls')
            print("That is not a valid language! This means you do not have the lang file in the directory with the language generator.")
            os.system('pause')
    listlang = lang.readline().split()
    words = listlang
    lang.seek(0)
    listlang2 = lang.readlines()[1].split()
    englishtrans = listlang2
    os.system('cls')
    print("Loaded!")
    os.system('pause')

def generateWord(rootWord): # Word Generation
    while True:
        genChoice = random.randrange(1,5) # Different forms of word generation
        if genChoice == 1:
            word = random.choice(consonants) + random.choice(vowels) + random.choice(consonants) + random.choice(vowels)
        elif genChoice == 2:
            word = random.choice(vowels) + random.choice(consonants) + random.choice(vowels) + random.choice(consonants)
        elif genChoice == 3:
            word = random.choice(vowels) + random.choice(consonants) + random.choice(vowels) + random.choice(consonants) + random.choice(vowels)
        elif genChoice == 4:
            word = random.choice(vowels) + random.choice(consonants) + random.choice(vowels) + random.choice(consonants) + random.choice(vowels) + random.choice(consonants) + random.choice(vowels)
        else:
            word = random.choice(vowels) + random.choice(consonants) + random.choice(vowels) + random.choice(consonants) + random.choice(vowels)
        if word not in words: # Repeat until word is unique
            break
        if rootWord.lower() in englishtrans: # If word has previously been generated, skip
            return words[englishtrans.index(rootWord.lower())]
    return word

while True: # Main loop
    os.system('cls')
    if len(words) == 0:
        print("!!! THIS LANGUAGE IS EMPTY! NO WORDS HAVE BEEN GENERATED. GENERATE THE LANGUAGE TO GET REAL TRANSLATIONS. !!!")
    choice = input("Enter 1 for translator, 2 for dict, 3 to generate language from English dict, 4 to overwrite / add a word to your language dictionary, 5 to save your language: ")
    if choice == "2":
        os.system('cls')
        for word in words:
            print(f"{word} is equivalent to {englishtrans[words.index(word)]} in English.")
        os.system('pause')
    elif choice == "5":
        save = open(f"./languages/{name}.lang",'w', encoding="utf-8")
        for word in words:
            save.write(word + " ")
        save.write('\n')
        for word in englishtrans:
            save.write(word + " ")
        save.close()
        os.system('cls')
        print("Saved!")
        os.system('pause')
    elif choice == "4":
        os.system('cls')
        enter = input("Enter a single word (no spaces) in English that you would like to overwrite in your language (no punctuation, apostrophes, question marks, etc): ").lower()
        try: 
            englishtrans.index(enter)
            print(f"That word, in your language, currently is: {words[englishtrans.index(enter)]}")
            enter2 = input("What would you like to overwrite the word to in your language (no punctuation, apostrophes, question marks, spaces, etc): ").lower()
            words[englishtrans.index(enter)] = enter2
            os.system('cls')
            print("Complete!")
            os.system('pause')
        except:
            enter2 = input("What would you like to overwrite the word to in your language (no punctuation, apostrophes, question marks, spaces, etc): ").lower()
            englishtrans.append(enter)
            words.append(enter2)
            os.system('cls')
            print("Complete!")
            os.system('pause')
    elif choice == "3":
        os.system('cls')
        if name == None:
            print("Sorry, this language was loaded. It can not be re-generated. Create a new language to generate again.")
            os.system('pause')
        else:
            progressT = threading.Thread(target=progress)
            progressT.start()
            dictionary = open('./bin/dictionary.txt','r')
            englishWords = dictionary.read().splitlines()
            for word in englishWords:
                newWord = generateWord(word)
                words.append(newWord)
                englishtrans.append(word)
                generated = generated + 1
            os.system('cls')
            print("Complete!")
            os.system('pause')
    elif choice == "1":
        os.system('cls')
        choice2 = input("1 for from English, 2 for from your generated language: ")
        if choice2 == "2":
            os.system('cls')
            enter = input("Enter a sentence in your language to translate (put a space before question marks, punctuation, and exclamation points. Do not use apostrophes): ").lower()
            final = ""
            unT = False
            for word in enter.split():
                if word in words:
                    final = final + englishtrans[words.index(word)] + " "
                else:
                    final = final + word + " "
                    if word != "." or word != "?" or word != "!":
                        unT = True
            os.system('cls')
            if unT:
                print("One word was not found, therefore it is untranslated. If you included a name, or specific place, etc that can not be translated, disregard this alert.")
            print(f"In English: {final}")
        else:
            os.system('cls')
            print("Instead of using conjunctions like 'I'm', use 'I am'")
            enter = input("Enter your english sentence to translate (put a space before question marks, punctuation, and exclamation points. Do not use apostrophes): ").lower()
            final = ""
            unT = False
            for word in enter.split():
                if word in englishtrans:
                    final = final + words[englishtrans.index(word)] + " "
                else:
                    final = final + word + " "
                    if word != "." or word != "?" or word != "!":
                        unT = True
            os.system('cls')
            if unT:
                print("A word, or words, was not found, therefore it is untranslated. If you included a name, or specific place, etc that can not be translated, disregard this alert.")
            if name == None:
                print(f"In {choice4}: {final}")
            else:
                print(f"In {name}: {final}")
        os.system('pause')
    else:
        os.system('cls')
        print("That is not a valid option!")
        os.system('pause')