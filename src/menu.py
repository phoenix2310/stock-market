def showHeader():
    print('''                        $$$ WELCOME TO OUR PLACE $$$
                              ***THE STOCK MARKET*** 
                           I AM YOUR STOCK BROKER''')
def showMenu():                           
    print('''HOW MAY I HELP YOU :
    1 - BUY STOCK
    2 - SELL STOCK
    3 - SEE ALL PURCHASED STOCK
    4 - WANT ADIVICE
    5 - SEE TOP STOCK OF MARKET
    6 - EXIT''')
    c=int(input("ENTER YOUR CHOICE: "))
    if c>=1 and c<=6:
        return c
    return showMenu()



