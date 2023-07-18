import time

def run1(b):
    i = 0
    cont = 0
    while i < a:
        if i > (a - int(b)):
            break
        i += int(b)
        cont += 1
    return i, cont


def run2(q):
    if int(q) > 2:
        print("Desglosaste en billetes de " + str(q) + ", obtenemos " + str(d) + " billetes de " + str(q))
        time.sleep(0.2)
    else:
        print("Desglosaste en monedas de " + str(q) + ", obtenemos " + str(d) + " monedas de " + str(q))
        time.sleep(0.2)
    print("Quedan pendientes de desglosar " + str(a))
    print("")
    time.sleep(0.5)


def run3():
    print("""En que billetes desea desglosar
        hay de:
    -  50 dolares-
    -  20 dolares-
    -  10 dolares-
    -  5 dolares -
    -  2 dolares -""")
    x = input("Cual escoges?: ")
    print("")
    return x


if __name__ == "__main__":
    a = int(input("Digite la cantidad de Dolares: "))
    print("")
    while a > 1:
        print("Tienes " + str(a) + " dolares, para desglosar")
        con = 1 
        while con == 1:
            b = run3()
            if int(b) == 50 or int(b) == 20 or int(b) == 10 or int(b) == 5 or int(b) == 2:
                con = 0
            else:
                print("vuelve a intentarlo")
                time.sleep(0.5)
        c, d = run1(b)
        a = a - c
        run2(b)
    if a == 0:
        print("No tienes Saldo, ADIOS!!!")
        time.sleep(0.2)
    elif a == 1:
        print("Solo te queda 1 dolar, ADIOS!!!")
        time.sleep(0.2)