import requests,time,sys
from colorama import Fore as fg


def intro():
    text = """     ________                                                                   __                         
    /        |                                                                 /  |                        
    $$$$$$$$/  _______   __    __  _____  ____    ______    ______   ______   _$$ |_     ______    ______  
    $$ |__    /       \ /  |  /  |/     \/    \  /      \  /      \ /      \ / $$   |   /      \  /      \ 
    $$    |   $$$$$$$  |$$ |  $$ |$$$$$$ $$$$  |/$$$$$$  |/$$$$$$  |$$$$$$  |$$$$$$/   /$$$$$$  |/$$$$$$  |
    $$$$$/    $$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$    $$ |$$ |  $$/ /    $$ |  $$ | __ $$ |  $$ |$$ |  $$/ 
    $$ |_____ $$ |  $$ |$$ \__$$ |$$ | $$ | $$ |$$$$$$$$/ $$ |     /$$$$$$$ |  $$ |/  |$$ \__$$ |$$ |      
    $$       |$$ |  $$ |$$    $$/ $$ | $$ | $$ |$$       |$$ |     $$    $$ |  $$  $$/ $$    $$/ $$ |      
    $$$$$$$$/ $$/   $$/  $$$$$$/  $$/  $$/  $$/  $$$$$$$/ $$/       $$$$$$$/    $$$$/   $$$$$$/  $$/\n
            [+] Creator :- N4kb4\n\t\t\b\b\b\b[+] Instagram :- hackersarena0\n\n[1] Subdomain Enumeration\n[2] Directory Enumeration\n\n"""
    
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.005)

    try:
        userOption = int(input("Enter your choice here: "))
    except Exception:
        print(fg.LIGHTMAGENTA_EX+"Please enter a valid input."+fg.RESET)
        exit()

    if ((userOption == 1) or  (userOption == 2)):
        userDomain = input(fg.RED+"[+] Enter domain: "+fg.RESET)
        userWordList = input(fg.RED+"[+] Enter Path to wordlist: "+fg.RESET)
    else:
        print(fg.CYAN+"Not a valid input.\n"+fg.RESET)
        exit()
        

    if userOption == 1:

        domainCheck(userDomain,userWordList)

    elif userOption==2:
        directoryTraversal(userDomain,userWordList)

def domainCheck(userDomain,userWordList):
    with open(userWordList,'r') as f:
        for line in f:
            subdomain = line.strip()
            finalUrl = subdomain+"."+userDomain
            response = subFinder(finalUrl)
            if response:
                print(fg.GREEN+finalUrl)


def subFinder(finalUrl):
    try:
        return requests.get("https://"+finalUrl)
    except requests.exceptions.ConnectionError:
        pass

def directoryTraversal(userDomain,userWordList):
    with open(userWordList) as f:
        for line in f:
            directory = line.strip()
            finalUrl = "http://" + userDomain + "/" + directory
            response = dirFinder(finalUrl)
            if response:
                print(finalUrl)
                # print(response)

def dirFinder(finalUrl):
    try:
        return requests.get(finalUrl)
    except requests.exceptions.ConnectionError:
        pass

intro()
