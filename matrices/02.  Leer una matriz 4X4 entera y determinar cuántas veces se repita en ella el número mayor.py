# Leer una matriz 4X4 entera y determinar cuántas veces se repita en ella el número mayor

def run1(n):
    na, nb, nc, nd = a[n][0], a[n][1], a[n][2], a[n][3]
    print(str(na) + " " + str(nb) + " " + str(nc) + " " + str(nd))
    mayor_1 = nb
    if (na > nb):
        mayor_1 = na
    mayor_2 = nd  
    if (nc > nd):
        mayor_2 = nc
    
    if mayor_1 > mayor_2:
        return mayor_1
    else:
        return mayor_2


def run2():
    na, nb, nc, nd = list[0], list[1], list[2], list[3]
    print(str(na) + " " + str(nb) + " " + str(nc) + " " + str(nd))
    mayor_1 = nb
    if (na > nb):
        mayor_1 = na
    mayor_2 = nd  
    if (nc > nd):
        mayor_2 = nc
    
    if mayor_1 > mayor_2:
        return mayor_1
    else:
        return mayor_2


if __name__ == "__main__":
    print("#######################################################################################################")
    print("#       Leer una matriz 4X4 entera y determinar cuántas veces se repita en ella el número mayor       #")
    print("#######################################################################################################")
    print("")
    a = [(1, 1, 6, 5), (2, 4, 8, 3), (2, 1, 5, 1), (4, 5, 1, 2)]
    print(a)
    print("")
    n1 = run1(0)
    n2 = run1(1)
    n3 = run1(2)
    n4 = run1(3)
    list = (n1, n2, n3, n4)
    b = run2()
    print(str(b))