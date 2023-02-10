#i`ll edit soon for more func
import requests
import os
import time
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

def get_dorks():
    response = requests.get("https://raw.githubusercontent.com/TUXCMD/Google-Dorks-Full_list/master/googledorks_full.txt")
    if response.status_code == 200:
        return response.text
    else:
        return "Error: Could not retrieve dorks list."

def parse_dorks(dorks, domain):
    parsed_dorks = []
    for dork in dorks.split("\n"):
        parsed_dorks.append(f"{dork} site:{domain}")
    return parsed_dorks

def save_dorks(dorks):
    with open("dorks.txt", "w", encoding="utf-8") as file:
        for dork in dorks:
            file.write(f"{dork}\n")

def scan_dorks_from_file():
    with open("dorks.txt", "r", encoding="utf-8") as file:
        dorks = file.readlines()
    ua = UserAgent()
    headers = {"User-Agent": ua.random}
    for dork in dorks:
        dork = dork.strip()
        response = requests.get(f"https://www.google.com/search?q={dork}", headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            results = soup.find_all("div", class_="r")
            print(f"Results for dork: {dork}")
            for result in results:
                print(result.a.text)
        else:
            print(f"Error: Could not retrieve results for dork: {dork}")

def main_menu():
    print("\n")
    print("""             ██████╗  ██████╗  ██████╗ ██████╗  ██████╗ ██████╗ ██╗  ██╗███████╗
            ██╔════╝ ██╔═████╗██╔═████╗██╔══██╗██╔═████╗██╔══██╗██║ ██╔╝██╔════╝
            ██║  ███╗██║██╔██║██║██╔██║██║  ██║██║██╔██║██████╔╝█████╔╝ ███████╗
            ██║   ██║████╔╝██║████╔╝██║██║  ██║████╔╝██║██╔══██╗██╔═██╗ ╚════██║
            ╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝╚██████╔╝██║  ██║██║  ██╗███████║
            ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ """)
    print("\n")
    print("\t" + "[1] Specify dorks for user input domain")
    print("\t" + "[2] Scan dorks from file")
    choice = input("\t" + "Enter your choice: ")
    if choice == "1":
        dorks = get_dorks()
        if type(dorks) == str:
            domain = input("Enter the domain to use: ")
            parsed_dorks = parse_dorks(dorks, domain)
            save_dorks(parsed_dorks)
            print("Dorks saved to dorks.txt.")
            time.sleep(1)
            os.system("cls || clear")
            main_menu()
        else:
            print(dorks)
    elif choice == "2":
        scan_dorks_from_file()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()