# CMPT 120 - Lab#6
# alexander white
# 24-oct-2018
###

cmds=["add","sub","mult","div","pow","quit"]

def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are "+str(cmds)+"\n")
    
def showOutro():
    print("\nThank you for using the Arithmetic Engine…")
    print("\nPlease come back again soon!")

def numbers():
    while True:
        try:
            num1 = int(input("Enter the first  number: "))
            num2 = int(input("Enter the second number: "))
            if type(num1) == int and type(num2) == int:
                break
        except:
            print("unfortunatly you have to enter numbers")
            continue
    
def doLoop():
    while True:
        cmd = input("What computation do you want to perform? ")
        cmd = cmd.lower()
        if cmd == "add":
            numbers()
            result = num1 + num2
        elif cmd == "sub":
            numbers()
            result = num1 - num2
        elif cmd == "mult":
            numbers()
            result = num1 * num2
        elif cmd == "div":
            numbers()
            result = num1 // num2
            numbers()
        elif cmd == "pow":
            numbers()
            result = num1 ** num2
        elif cmd == "quit":
            break
        else:
            print(cmd+" is not a valid command.")
            print("try a valid command, the valid commands are "+str(cmds)+"\n")
            continue
        print("The result is " + str(result) + ".\n")
            
def main():
    showIntro()
    doLoop()
    showOutro()
main()
