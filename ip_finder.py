from colorama import Fore, Style
import socket
print(f"""{Fore.GREEN}\t    ________     _______           __
\t   /  _/ __ \   / ____(_)___  ____/ /__  _____
\t   / // /_/ /  / /_  / / __ \/ __  / _ \/ ___/
\t _/ // ____/  / __/ / / / / / /_/ /  __/ /
\t/___/_/      /_/   /_/_/ /_/\__,_/\___/_/
\n                   [Author : HackersBrain]{Style.RESET_ALL}""")
print()
try:
    url = input(Fore.GREEN + " [" + Fore.RED + 'x' + Fore.GREEN + "]" + Style.RESET_ALL + " Enter URL [ex: example.com] : " +
                Fore.GREEN + Style.RESET_ALL)
    ip = socket.gethostbyname(url)
    print()
    print(f" {Fore.GREEN}[{Fore.RED}x{Fore.GREEN}]{Style.RESET_ALL} IP Address of \"{url}\" is : {Fore.GREEN}{ip}{Style.RESET_ALL}")
except Exception as error:
    print(f"\n {error}\n Error Encountered !!!\t Exiting Code...")
print()
