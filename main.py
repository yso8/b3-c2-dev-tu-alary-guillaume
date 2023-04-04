from modules.calculator import *
from modules.colors import bcolors
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def afficher_logo():
        print("""\
░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗███████╗
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔════╝
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░█████╗░░
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██╔══╝░░
╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░███████╗
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝""")

        print("""\
            
█▄▄ █▄█   █▄▄ ░ █▀▀   █▀▀ ▀█▀   ▄▀█ ░ █░░
█▄█ ░█░   █▄█ ▄ █▄█   ██▄ ░█░   █▀█ ▄ █▄▄""")

        print("")


def afficher_menu():
    print("------------------------------------")
    print("1. Calculer")
    print("2. Crédits")
    print("3. Quitter")
    print("------------------------------------")
    print("")


def main():
    print("Que voulez-vous faire? ")
    choice = input("= ")
    choice = choice.strip()

    if choice == "1":
        print("")
        op = input("Entrez une expression arithmétique: ")
        Calculator.calculate(op)
        main()
    elif choice == "2":
        print("")
        print("( ͡• ͜ʖ ͡•) - github : " + bcolors.OKBLUE + "\033[4myso8\033[0m" + bcolors.ENDC + " & " + bcolors.OKGREEN + "\033[4mlouisalr\033[0m" + bcolors.ENDC)
        print("")
        main()
    elif choice == "3":
        print("")
        print("Fermeture du programme, à bientôt !")
        print("")
    elif choice == "clear":
        cls()
    else:
        print("Choix invalide.")
        main()

afficher_logo()
afficher_menu()
main()
