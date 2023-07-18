import math

w = int(1)

while w == 1:

    z = int(input("""
    Calcular Area de:
    Triangulo - 1
    Triangulo Equilatero - 2
    - :"""))

    if z == 1:
        a = input("Digite la base del triangulo para calcular el area: ")
        b = input("Digite la altura del triangulo para calcular el area: ")
        c = (int(a) * int(b)) / 2
        print("El Area del triangulo es " + str(c))
    elif z == 2:
        a = input("Digite la base y altura del triangulo equilatero para calcular el area: ")
        b = math.sqrt(int(a))
        c = b / 2
        print("El Area del triangulo es " + str(c))
    else:
        print("Opcion incorrecta")
    w = int(input("""Desea continuar
    - Si = 1
    - No = 0
    _ :"""))
