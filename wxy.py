import requests, uuid, secrets, json
from time import sleep
from colorama import  Fore
print(Fore.BLUE + """
   
░██╗░░░░░░░██╗██╗░░██╗██╗░░░██╗
░██║░░██╗░░██║╚██╗██╔╝╚██╗░██╔╝
░╚██╗████╗██╔╝░╚███╔╝░░╚████╔╝░
░░████╔═████║░░██╔██╗░░░╚██╔╝░░
░░╚██╔╝░╚██╔╝░██╔╝╚██╗░░░██║░░░
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░░░╚═╝░░░
      """, Fore.GREEN + "Credit @r.rxu - wx#0001")
ur = input(Fore.YELLOW + 'file name : ')

file = open(ur).read().splitlines()
for file in file:
   ue = requests.get(f'https://www.tiktok.com/@{file}?').status_code
   if ue == 200:
       print(Fore.RED + 'user taken: ',file)
   if ue == 404:
       print(Fore.GREEN + 'user  available:' ,file)
