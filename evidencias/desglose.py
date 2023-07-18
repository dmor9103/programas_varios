def run1(b):
    i = 0
    cont = 0
    while i < a:
        if i > (a - b):
            break
        i += b
        cont += 1
    return i, cont


def run2(q):
    if int(q) > a:
        print("Desglosaste en billetes de " + str(q) + ", obtenemos " + str(c) + " billetes de " + str(q))
    else:
        print("Desglosaste en monedas de " + str(q) + ", obtenemos " + str(c) + " monedas de " + str(q))
    print("Quedan pendientes de desglosar " + str(a))


if __name__ == "__main__":
    a = 446
    print("Tienes " + str(a) + " dolares, para desglosar")
    cincuenta = 50
    b, c = run1(cincuenta)
    a = a - b
    run2(cincuenta)
    veinte = 20
    b, c = run1(veinte)
    a = a - b
    run2(veinte)
    diez = 10
    b, c = run1(diez)
    a = a - b
    run2(diez)
    cinco = 5
    b, c = run1(cinco)
    a = a - b
    run2(cinco)
    dos = 2
    b, c = run1(cinco)
    a = a - b
    run2(dos)