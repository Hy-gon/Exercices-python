#!/usr/bin/env python

#__Author__ = "Hy-gon"
#__Python__ = "3.6.8"
#__Status__ = "Finished"
#__Emails__ = "mickael.lemieux@outlook.com"

first_number = second_number = ""

while not (first_number.isdigit() and second_number.isdigit()):
    first_number = input("Veuillez entrer votre premier nombre : ")
    second_number = input("Veuillez entrer votre second nombre : ")
    if first_number.isdigit() and second_number.isdigit():
        print(f"Le résultat de l'addition de {first_number} avec {second_number} est égal à {int(first_number) + int(second_number)}")
        break;
    else:
        print("Veuillez entrer deux nombres valides")
