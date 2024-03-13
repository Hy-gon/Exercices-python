nombre_1 = input("Veuillez entrer votre premier nombre positif : ")
nombre_2 = input("Veuillez entrer votre second nombre positif : ")
operator = input("Veuillez entrer votre opérateur (+, -, *, /, %) : ")

if nombre_1.isdigit() and nombre_2.isdigit():
    nombre_1 = int(nombre_1)
    nombre_2 = int(nombre_2)

    if operator == "+":
        result = nombre_1 + nombre_2
        
    elif operator == "-":
        result = nombre_1 - nombre_2
        
    elif operator == "*":
        result = nombre_1 * nombre_2
        
    elif operator == "/":
        result = nombre_1 / nombre_2
        
    elif operator == "%":
        result = nombre_1 % nombre_2
        
    else:
        result = "Votre opérateur n'est pas correcte, veuillez reesayer"
else:
    result = "Le premier ou second nombre n'est pas un nombre ou n'est pas positif"

print(result)