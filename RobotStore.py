

class Product():

    def __init__(self, name, price, stock):
        
        self.name = name
        self.price = price
        self.stock = stock

    def stocktest(self,numbuy):
        if numbuy > self.stock:
            print ("There are only "+self.stock+" of this item available."
                   " You cannot purchase more.")
        else:
            print ("You can easily buy "+numbuy,self.name+"s.")

    def sayprice(self,numbuy):
        totcost = self.price * numbuy
        print("this purchase will cost $"+"{0:.2f}".format(totcost)+".")
        return totcost

    def stocksold(self,numbuy):
        self.stock -= numbuy

        
products=[ Product("Ultrasonic range finder", 2.50, 4),
        Product("Servo motor",14.99,10),
        Product("Servo controller",44.95,5),
        Product("Microcontroller Board",34.95,7),
        Product("Laser range finder",149.99,2),
        Product("Lithium polymer battery",8.99,8)]

def printStock():
    print()
    print("Available Products")
    print("------------------")
    for i in range(0,len(products)):
        if products[i].stock > 0:
            print(str(i)+")",products[i].name, "$", products[i].price)
    print()
    
def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
        if vals[0] == "quit": break
        prodId = int(vals[0])
        count = int(vals[1])
        if products[prodId].stock >= count:
            if cash >= products[prodId].price * count:
                products[prodId].stock -= count
                cash -= products[prodId].price * count
                print("You purchased", count, products[prodId].name+".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", products[prodId].name)
main()
