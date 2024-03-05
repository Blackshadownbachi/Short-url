import pyshorteners
from colorama import Fore, Back, Style
print( Fore.YELLOW +
'''___| |__   __ _  __| | _____      __
 / __| '_ \ / _` |/ _` |/ _ \ \ /\ / /
 \__ \ | | | (_| | (_| | (_) \ V  V /
 |___/_| |_|\__,_|\__,_|\___/ \_/\_/''')
  
     
b='Telugu hacks group'
a=b.center(50) 
print(Fore.RED + a)
url = input('Enter your Any Url : ')
shortener = pyshorteners.Shortener()
short_url = shortener.tinyurl.short(url)
print( Fore.GREEN + " Shortened URL:", short_url)
