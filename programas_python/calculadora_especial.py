# Mi primer calculadora
def run():
    LIMITE = 5

    contador = 0
    while contador < LIMITE:
        print("""
        ###########################
        ########Calculadora########
        ###########################
        Digita la opcion:
        - Sumar es 1 -1
        - Restar es 2 -
        - Multiplicar es 3 -
        - Dividir es 4 -

        Si deseas salir digita 0
        """)
        opcion = input("Elige una opcion: ")
        if (opcion >= 5) == (opcion <= -1):
            print("Opcion erronea!")
        contador = contador + 1


if __name__ == "__main__":
    run()