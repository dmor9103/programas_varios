def run1():
    b = 0
    for i in range(1, a + 1):
        b = b + i
    print(str(b))

if __name__ == "__main__":
    cont = 1
    while cont == 1:
        a = int(input("a: "))
        if a <= 1:
            print("Volver a intentar")
        else:
            cont = 0
    run1()