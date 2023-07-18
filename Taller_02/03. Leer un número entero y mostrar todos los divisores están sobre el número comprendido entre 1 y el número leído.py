def run1():
    b = 2
    while int(a) > b:
        c = int(a) % b
        if int(c) == 0:
            print(str(b))
            b = int(b) + 1
        else:
            b = int(b) + 1


if __name__ == "__main__":
    cont = 1
    while cont == 1:
        a = input("Digite un numero entero mayor a 4: ")
        if int(a) >= 4:
            cont = 0
        else:
            print("Valor invalido")
    run1()