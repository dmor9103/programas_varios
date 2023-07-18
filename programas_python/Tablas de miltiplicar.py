# contador cutre, pero se que falta o sobra algo
cont = 0
cont2 = 1

while int(cont) < int(cont2):
    n1 = input("digita el numero a multiplicar:" )
    for n2 in range(10):
        # n1 = int(n1)
        n3 = int(n1) * int(n2)
        print(str(n1) + " * " + str(n2) + " = " + str(n3))
    cont = input("Desea continuar - 1 = SI - 0 = NO :")