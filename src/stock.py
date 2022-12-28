def wantAdvice():
    print('''Random Advice
    1)Sensex
    2)Nifty
    3)Tata steel                       ''')

def sellStock():
    g=input("Is this the stock u want to buy : y/n")
    if g=='y':
        print("your stock has been sold")
    else:
        print("Re-enter your stock to sell")

def buyStock():
    bYe=input("Enter the number/name of the stock u want to buy : ")
    if bYe=="":
        print("Confirmation ALert : ",bYe,"is the stock u gonna purchase")


