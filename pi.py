import math

def pite():
    ans = 0
    n= int(input("On a scale of one to infinity, how accurate do you want your pi?"))
    for x in range (1,n+1):
        pie=4/(2*x-1)
        if x%2==1:
            ans=ans+pie
        elif x%2==0:
            ans=ans-pie
    print(ans)

print(math.pi)

pite()
