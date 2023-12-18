import requests
from os import path
from  colorama import Fore

fp = Fore.CYAN


banner = '''{}


,--.   ,--.       ,---.,--.           ,--.               
 \  `.'  /,-----./  .-'`--',--,--,  ,-|  | ,---. ,--.--. 
  .'    \ '-----'|  `-,,--.|      \' .-. || .-. :|  .--' 
 /  .'.  \       |  .-'|  ||  ||  |\ `-' |\   --.|  |    
'--'   '--'      `--'  `--'`--''--' `---'  `----'`--'
                               coded by : @black
\n'''.format(fp)
print(banner)

url = input(Fore.LIGHTYELLOW_EX + "Url desejada: ")
wordlist = input(Fore.LIGHTYELLOW_EX + "Caminho da wordlist: ")


words = path.realpath(wordlist)

file = open(words)

for line in file:
    line = line.strip()
    val = f"https://{line}.{url}"
    try:
       r = requests.get(val)
       print(Fore.GREEN + f"subdominio encontrado: {val}")          
    except Exception as error:
        pass



