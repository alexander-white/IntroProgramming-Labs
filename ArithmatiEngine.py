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
    
def doLoop():
    while True:
        cmd = input("What computation do you want to perform? ")
        cmd = cmd.lower()
        if cmd == "add":
            num1 = int(input("Enter the first  number: "))
            num2 = int(input("Enter the second number: "))
            result = num1 + num2
        elif cmd == "sub":
            num1 = int(input("Enter the first  number: "))
            num2 = int(input("Enter the second number: "))
            result = num1 - num2
        elif cmd == "mult":
            num1 = int(input("Enter the first  number: "))
            num2 = int(input("Enter the second number: "))
            result = num1 * num2
        elif cmd == "div":
            num1 = int(input("Enter the first  number: "))
            num2 = int(input("Enter the second number: "))
            result = num1 // num2
        elif cmd == "pow":
            num1 = int(input("Enter the first  number: "))
            num2 = int(input("Enter the second number: "))
            result = num1 ** num2
        elif cmd == "quit":
            break
        else:
            print(cmd+" is not a valid command.")
            print("try a valid command, the valid commands are "+str(cmds)+"\n")
        print("The result is " + str(result) + ".\n")
            
def main():
    showIntro()
    doLoop()
    showOutro()
main()
