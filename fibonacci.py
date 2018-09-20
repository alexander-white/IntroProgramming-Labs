def fibb():
    n1=1
    n2=1
    ans=0
    nth=int(input("pick a number: "))
    for x in range(nth):
        ans = n1+n2
        n1=n2
        n2=ans
    print("The "+str(nth)+"th term of the Fibonacci sequence is "+str(ans)+".")
        
fibb()
