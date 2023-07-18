def run1(n, u):
    print("El " + n + " numero es: " + u)
    for i in range(1, int(u) + 1):
        print(i)
        i += 1


if __name__ == "__main__":
    cont = 1
    while cont == 1:
        a = input("Digita un numero de 3 cifras: ")
        if int(a) <= 99 or int(a) >= 1000:
            print("Valor invalido")
        else:
            cont = 0
    run1("primer", a[0:1])
    run1("segundo", a[1:2])
    run1("Tercer", a[2:3])