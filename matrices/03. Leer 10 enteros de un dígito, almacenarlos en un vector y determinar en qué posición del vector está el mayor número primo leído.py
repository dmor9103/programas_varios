# 03. Leer 10 enteros de un dígito, almacenarlos en un vector y determinar en qué posición del vector está el mayor número primo leído

def run1():
    c = 0
    for i in range (0, 10):
        n = input("digita un numero: ")
        a.append(n)
        c += 1
    return c
        
def run2(k):
    n = 2
    if n >= int(primos[k]):
        print(int(primos[k]) + " Es primo")
        return True
    elif int(primos[k]) % n != 0:
        return run2(n + 1)
    else:
        print(str(primos[k]) + " No es primo")
        return False


if __name__ == "__main__":
    a = []
    primos = []
    cont1 = run1()
    print(a)
    for i in range(0, cont1 - 1):
        print(str(i))
        run2(i)
    max_item = max(a, key=int)
    print(str(max_item))