def title():
    print ("PYTHON GUESSING GAME.")

def main():
    answer="sheep"
    while answer == "sheep":
        print("I'm thinking of an animal.")
        guess=input("Which animal is it? if you are done enter a word starting with\"q\"")
        guess=guess.lower()
        if guess == answer:
            print("congratulations,you win.")
            intrest=input("do you like this animal? y or n")
            if intrest[0] == "y":
                print("that's great")
            elif intrest[0] == "n":
                print("not fond of them eh?")
            break
        elif guess[0] == "q":
            break
        else:
            print("nope, try again please")
title()
main()
