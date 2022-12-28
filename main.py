from dotenv import load_dotenv
load_dotenv()
from src.menu import showHeader,showMenu
from src.stock import wantAdvice,sellStock

showHeader()
ch=showMenu()
print(ch)
if ch==4:
    wantAdvice()
elif ch==2:
    sellStock()
# elif c==1:
#     return buyStock()
