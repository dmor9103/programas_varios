# def numero_primo(numero):
#     numero_primo1 = numero % 1
#     numero_primo2 = numero % numero
#     if numero_primo1 == 0 and numero_primo2 == 0:
#         return True
#     else:
#         return False


# def run():
#     numero = int(input("digita un numero para comprobar si es primo o no"))
#     if numero_primo(numero):
#         print("es primo")
#     else:
#         print("no es primo")


# if __name__ == "__main__":
#     run()
numero = int(input("digita un numero para comprobar si es primo o no"))
for rango in range(1, numero + 1):
    if rango == 0:
        numero_primo1 = numero % rango
#numero_primo2 = numero_primo3 % numero
    print(str(numero_primo1))