def fillinblank():
    global a, v, n, p
    n=input("Enter a noun: ")
    v=input("Enter a verb: ")
    a=input("Enter an adjective: ")
    p=input("Enter a place: ")

def madlibs():
    print("\nTake your "+a+" "+n+" and "+v+" it at the "+p+"!")

def main():
    fillinblank()
    madlibs()

main()
