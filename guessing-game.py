def title():
    print ("PYTHON GUESSING GAME.")

def main():
    answer="sheep"
    while answer == "sheep":
        print("I'm thinking of an animal.")
        guess=input("Which animal is it?")
        if guess == answer:
            print("congratulations,you win.")
            break
        else:
            print("nope, try again please")
title()
main()
