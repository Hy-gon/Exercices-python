# !/usr/bin/env python

# __Author__ = "Hy-gon"
# __Python__ = "3.12.2"
# __Status__ = "Finished"
# __Emails__ = "mickael.lemieux@outlook.com"

import random
NUMBER = random.randint(0, 100)


def main():
    try_number = 5
    print("** Le jeu du nombre mystère **")
    while try_number != 0:
        print(f'Il te reste {try_number} essaie')
        selected_number = input("Devine le nombre : ")
        if selected_number.isdigit():
            if int(selected_number) < NUMBER:
                print("Votre nombre est plus petit que le nombre mystère")
            elif int(selected_number) > NUMBER:
                print("Votre nombre est plus grand que le nombre mystère")
            else:
                print(f"Bravo ! Le nombre mystère était bien {NUMBER}")
                break
            try_number -= 1
        else:
            print("Veuillez rentrer un nombre valide")
    if try_number == 0:
        print(f"Dommage ! Le nombre était {NUMBER}")
    print("Fin du jeu.")


if __name__ == "__main__":
    main()
