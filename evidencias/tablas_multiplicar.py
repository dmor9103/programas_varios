def run():
    print("Tabla del " + str(a))
    for i in range(1, 10 + 1):
        b = int(a) * int(i)
        print(str(a) + " * " + str(i) + " = " + str(b))
        i += 1


if __name__ == "__main__":
    a = int(input("Digite un número para saber su tabla de multiplicar: "))
    run()