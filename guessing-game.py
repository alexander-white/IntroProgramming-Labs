def title():
    print ("PYTHON GUESSING GAME.")

def main():
    answer="sheep"
    while answer == "sheep":
        print("I'm thinking of an animal.")
        guess=input("Which animal is it? if you are done enter \"quit\"")
        guess=guess.lower()
        if guess == answer:
            print("congratulations,you win.")
            break
        elif guess == "quit":
            break
        else:
            print("nope, try again please")
title()
main()
