from dotenv import load_dotenv
from src.stock import wantAdvice, sellStock
from src.menu import showHeader, showMenu
from src.database import connect

load_dotenv()

connect()
showHeader()
ch = showMenu()
print(ch)
if ch == 4:
    wantAdvice()
elif ch == 2:
    sellStock()
# elif c==1:
#     return buyStock()
