import sys

MENU = """
Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément à la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
"""

choice = 0
element = ""
shop_list = []

# Adding element to the list
def add_element(shop_list, element):
    if element:
        if not element in shop_list:
            shop_list.append(element)
            print(f"L'élément {element} a bien été ajouté à la liste.")
        else:
            print(f"L'élément {element} éxiste déjà dans la liste.")
    else:
        print("Veuillez rentrer un élément.")

# Remove element from the list
def remove_element(shop_list, element):
    if element:
        if element in shop_list:
            shop_list.remove(element)
            print(f"L'élément {element} a bien été retiré de la liste.")
        else:
            print(f"L'élément {element} n'est pas dans la liste.")
    else:
        print("Veuillez rentrer un élément.")
        
# Print the list
def print_list(shop_list):
    if len(shop_list) != 0:
        for i in shop_list:
            print(f"{shop_list.index(i) + 1}. {i}")
    else:
        print("Votre liste ne contient aucun élément.")
        
# Clear the list
def clear_list(shop_list):
    if len(shop_list) != 0:
        shop_list.clear()
        print("La liste a été vidée de son contenu.")
    else:
        print("la liste est déjà vide.")
        
def close_program():
    sys.exit("A bientôt !")

# Loop program
def main():
    while True:
        print(MENU)
        choice = input("Votre choix : ")
        
        try:
            choix_int = int(choice)  
            
            if choix_int == 1:
                element = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
                add_element(shop_list, element)
            elif choix_int == 2:
                element = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
                remove_element(shop_list, element)
            elif choix_int == 3:
                print_list(shop_list)
            elif choix_int == 4:
                clear_list(shop_list)
            elif choix_int == 5:
                close_program()
            else:
                print("Veuillez choisir une des 5 options suivantes")
                
            element == ""
            print("_" * 50)
            
        except ValueError:
            print("Veuillez entrer un nombre valide")

if __name__ == "__main__":
    main()