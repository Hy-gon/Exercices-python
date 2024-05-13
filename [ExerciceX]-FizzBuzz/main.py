#!/usr/bin/env python

#__Author__ = "Hy-gon"
#__Python__ = "3.6.8"
#__Status__ = "Finished"
#__Emails__ = "mickael.lemieux@outlook.com"

def main():
    number = int(input("JEU FIZZBUZZ : Veuillez entrer un nombre : "))
    output = ""
    if number % 3 == 0:
        output += "Fizz"
    if number % 5 == 0:
        output += "Buzz"
    print(output or number)
    
if __name__ == "__main__":
    main()