def run():
    a = 1
    b = 5
    for i in range(int(a), int(b)):
        c = input("Digite un número: ")
        buffer.append(c)
        i += 1
        cont = input("Desea continuar?: ")
        if int(cont) != 1:
            break
    return i


if __name__ == "__main__":
    buffer = []
    i = run()
    print(buffer)
    print(str(i))