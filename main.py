import requests
import threading
from colorama import Fore, Style
import colorama
import pyfiglet
import os

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

print(Fore.RED)
pyfiglet.print_figlet("Asylum")
print(Style.RESET_ALL)
print("     e.g: https://example.com")
print('')

def make_request(link):
    return requests.get(link)

try:
    target = input("Enter URL ===>: ")

    try:
        test_request = requests.get(target)
        test_request.raise_for_status()
    except requests.RequestException as e:
        raise ValueError(f"Invalid URL or Network: {e}")

    with open("page.txt", 'r') as f:
        for word in f:
            link = f"{target}/{word.strip()}"
            t = threading.Thread(target=make_request, args=(link,))
            t.start()
            t.join()

            result = make_request(link)

            if result.status_code == 200:
                print(Fore.GREEN)
                print("[+] Found", result.url)
                print(Style.RESET_ALL)
            else:
                print(Fore.LIGHTRED_EX)
                print("[-] Not Found", result.url)
                print(Style.RESET_ALL)
except Exception as e:
    print("Please Check URL or Internet: ", str(e))
