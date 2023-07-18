# input 3 numbers
def run(c):
    a = int(c / 100)
    b = c % 10
    if a == b:
        return True
    else:
        return False


def run2(c):
    a = c[2:]
    b = c[0:1]
    if a == b:
        return True
    else:
        return False
    

if __name__ == "__main__":
    digi = int(input("digita un numero de tres digitos: "))
    opc1 = input("""
                 Que tipo de operacion va realizar:
                 Con Slices - 1
                 Con division y mod - 2
                 """)
    if opc1 == 1:
        a = run2(digi)
    else:
        a = run(digi)
    # Show the answer
    if a == True:
        print("Son iguales")
    else:
        print("No son iguales")
    # print(a)