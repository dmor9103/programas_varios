def run1():
    for i in range(1, a):
        i += 1
        if (i % 2) == 0:
            print(str(i) + " es par")


if __name__ == "__main__":
    a = int(input("a: "))
    run1()