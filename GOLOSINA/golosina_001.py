import msvcrt
from os import system

def pedir_golosinas(a, b, c, d):
    system("cls")
    print("#############################################################################################################")
    print("#                                         PEDIR GOLOSINAS                                                   #")
    print("#                                          by: Demor9103                                                    #")
    print("#############################################################################################################")
    print("")
    print("-Recuerde que el primer digito indica la fila y el segundo la columna-")
    a = input("Digite que golosina quiere: ")
    b = a[0:1]
    c = a[1:2]
    print("")
    print("Productos: " + str(a[int(b) - 1][int(c)]))
    b[int(b)][int(c)] -= 1
    c[int(b)][int(c)] += 1
    print("")
    print("Precio: " + str(d[int(b) - 1][int(c)]))
    d = d[int(b) - 1][int(c)]
    print("")
    print("Presione una tecla para continuar...")
    msvcrt.getch()
    system("cls")
    return d