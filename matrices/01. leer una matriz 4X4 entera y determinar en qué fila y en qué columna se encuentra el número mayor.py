# leer una matriz 4X4 entera y determinar en qué fila y en qué columna se encuentra el número mayor
import random

def run1(n1):
    if n1 % 2 == 0:
        print("Fila: " + str(cont2) + ", Columna: " + str(n + 1) + ", Es par")
    else:
        print("Fila: " + str(cont2) + ", Columna: " + str(n + 1) + ", No es par")


if __name__ == "__main__":
    n = 0
    cont1 = 1
    cont2 = 1
    
    print("#######################################################################################################")
    print("#  leer una matriz 4X4 entera y determinar en qué fila y en qué columna se encuentra el número mayor  #")
    print("#######################################################################################################")
    print("")
    a = [[1 ,2 , 3, 4], [2, 4, 1, 3], [3, 2, 4, 1], [4, 3, 1, 2]]
    print(a)
    print("")
    
    while cont1 == 1:
        b = run1(a[0][n])
        n += 1
        if n == 4:
            cont1 = 0
            cont2 += 1
    print("")
    
    
    n = 0
    cont1 = 1
    while cont1 == 1:
        b = run1(a[1][n])
        n += 1
        if n == 4:
            cont1 = 0
            cont2 += 1
    print("")

    n = 0
    cont1 = 1
    while cont1 == 1:
        b = run1(a[2][n])
        n += 1
        if n == 4:
            cont1 = 0
            cont2 += 1
    print("")
    
    n = 0
    cont1 = 1
    while cont1 == 1:
        b = run1(a[3][n])
        n += 1
        if n == 4:
            cont1 = 0
            cont2 += 1
    print("")