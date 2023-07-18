import time

def run():
    cont1 = 1
    while cont1 == 1:
        a = int(input("Digite el numero de inicio: "))
        b = int(input("Digite el numero de final: "))
        if b > a:
            print("Valor invalido!!! vuelve a intentarlo")
            time.sleep(0.3)
        else:
            cont1 = 0
    
    for i in range(a, b):
        i += 1
        c = i % 2
        if c == 0:
            print(str(i) + " es par")
            time.sleep(0.3)
        else:
            print(str(i) + " es impar")
            time.sleep(0.3)


if __name__ == "__main__":
    cont = 1
    while cont == 1:
        run()
        cont = int(input("Desea continuar - si: 1 - no: 0 : "))