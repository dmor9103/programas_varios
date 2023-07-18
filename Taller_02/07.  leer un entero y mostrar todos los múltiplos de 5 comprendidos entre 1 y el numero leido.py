def run1():
    b = 0
    for i in range(1, a + 1):
        b = 5 * i
        print("5 * " + str(i) + " = " + str(b))
        i += 1


if __name__ == "__main__":
    a = int(input("a = "))
    run1()