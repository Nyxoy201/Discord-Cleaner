from Functions import *

banner = f"""
    ____  _                          __   ________                          
   / __ \(_)_____________  _________/ /  / ____/ /__  ____ _____  ___  _____
  / / / / / ___/ ___/ __ \/ ___/ __  /  / /   / / _ \/ __ `/ __ \/ _ \/ ___/
 / /_/ / (__  ) /__/ /_/ / /  / /_/ /  / /___/ /  __/ /_/ / / / /  __/ /    
/_____/_/____/\___/\____/_/   \__,_/   \____/_/\___/\__,_/_/ /_/\___/_/   

                                                    CREATED BY NYXOY

"""
choices = f"""          [{white}1{blue}] Check + Clean                   [{white}4{blue}] Help
          [{white}2{blue}] Check Injections                [{white}5{blue}] Exit     
          [{white}3{blue}] Clean Injections

"""  

def menu():
    clear()
    print(blue + banner)
    print(choices)

while True:  
    menu()

    choice = input(f"[{white}!{blue}] {white}Enter Choice: ")

    if choice == "1":
        clear()
        print(blue + banner + white)
        check_clean_discord()
        input(f"[{blue}FINISHED{white}] Press Enter to return to the main menu...")

    elif choice == "2":
        clear()
        print(blue + banner + white)
        check_injection_discord()
        input(f"[{blue}FINISHED{white}] Press Enter to return to the main menu...")

    elif choice == "3":
        clear()
        print(blue + banner + white)
        print(f"{blue}[{white}1{blue}] {white}Discord")
        print(f"{blue}[{white}2{blue}] {white}Discord Canary")
        print(f"{blue}[{white}3{blue}] {white}Discord PTB\n")
        version = input(f"[{blue}VERSION{white}] {white}Version You Want To Clean (1/2/3): ")
        if version == "1":
            clear()
            print(blue + banner + white)
            clean_discord_version("1")
        elif version == "2":
            clear()
            print(blue + banner + white)
            clean_discord_version("2")
        elif version == "3":
            clear()
            print(blue + banner + white)
            clean_discord_version("3")
        else:
            print(f"[{red}ERROR{white}] Invalid Choice")
        input(f"[{blue}FINISHED{white}] Press Enter to return to the main menu...")

    elif choice == "4":
        clear()
        print(blue + banner + white)
        print(help)
        input(f"[{blue}FINISHED{white}] Press Enter to return to the main menu...")

    elif choice == "5":
        clear()
        print(blue + banner + white)
        print(f"[{blue}FINISHED{white}] Press Enter To Exit...")
        input()
        break  

    else:
        print(f"[{red}ERROR{white}] Invalid Choice")
        input(f"\n[{blue}FINISHED{white}] Press Enter to return to the main menu...")
