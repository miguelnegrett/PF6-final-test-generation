import json
import requests


def dish_fetch(num):
    response = requests.get(f"https://api-colombia.com/api/v1/TypicalDish/{num}")

    dish = json.loads(response.content)

    return dish


def main():
    print("*" * 40)
    print("co    SABORES DE COLOMBIA    co")
    print("*" * 40)

    num = int(input("Ingrese el número del plato: "))

    dish = dish_fetch(num)

  
    print("*" * 40)
    print("ID:", dish["id"])
    print("Nombre:", dish["name"])
    print("Descripción:", dish["description"])
    print("Ingredientes:", dish["ingredients"])
    print("*" * 40)
    

if __name__ == "__main__":
    main()