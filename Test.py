from colorama import Fore
import random

x = random.ramdit(1, 100)

while True:
    number = input("Entrer un nombre (1 - 100) : ")
    
    if number < x:
        print("c'est +")
    elif number > x:
        print("c'est -")
    else:
        print("Vous avez Trouver le bon nombre")
        print(Fore.GREEN + "Résultat correct" + Fore.WHITE)
