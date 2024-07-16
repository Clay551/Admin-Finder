import requests
import threading
from colorama import Fore
import colorama
import pyfiglet
import os

os.system('cls' if {os.name} == 'nt' else 'clear')
print(colorama.Fore.RED)
pyfiglet.print_figlet("Asylum")
print(colorama.Fore.RESET)
print("     e.g: https://example.com")
print('')

def make_request(link):
    return requests.get(link)

try:
    target = input("Enter URL===> ")

    try:
        test_request = requests.get(target)
        test_request.raise_for_status()
    except requests.RequestException as e:
        raise ValueError(f"Invalid URL or Network: {e}")

    with open("page.txt", 'r') as f:
        for word in f:
            link = target + "/" + word.strip()
            t = threading.Thread(target=make_request, args=(link,))
            t.start()
            t.join()

            result = make_request(link)

            if result.status_code == 200:
                print(colorama.Fore.GREEN)
                print("[+] Found", result.url)
                print(colorama.Fore.RESET)
            else:
                print(colorama.Fore.LIGHTRED_EX)
                print("[-] Not Found", result.url)
                print(colorama.Fore.RESET)
except Exception as e:
    print("Please Check URL or Internet: ", str(e))