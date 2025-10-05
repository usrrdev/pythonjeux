from colorama import Flore
import random

x = random.randit(1, 100)

while True:
    number = input("Entrer un nombre (1 - 100) : ")
    
    if number < x:
        print("c'est +")
    elif number > x:
        print("c'est -")
    else:
        print("Vous avez Trouver le bon nombre")
        print(Flore.GREEN + "Résultat correct" + Flore.WHITE)
