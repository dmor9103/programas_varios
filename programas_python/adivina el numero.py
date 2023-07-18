# estos son ualgunos de los muchos modulos que ya vienen con python
# "random" trabaja la aleatoriedad
# "os" limpia la pantalla del codigo, segun el sistema
# "ime" controla los tiempos de ejecucion y da la funcion delay
import os
import random
import time


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Digita un numero: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Es un numero mas grande")
            time.sleep(1)
            clear()
        else:
            print("Es un numero mas peqqueño")
            time.sleep(1)
            clear()
        numero_elegido = int(input("Digita un nuevo numero: "))
    print("GANASTE")


if __name__ == "__main__":
    run()