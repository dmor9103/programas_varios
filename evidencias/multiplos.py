import time

def run1(i):
    o = 0
    u = 1
    while int(a) > o:
        o = int(i) * u
        u = u + 1
    if o == int(a):
        return True
    else:
        return False
            

def run2(num, r):
    if b == True:
        print(a + " es multiplo de " + num)
        print(r + """
            """)
    else:
        print(a + " no es multiplo de " + num)
        print("")


if __name__ == "__main__":
    a = input("Digita: ")

    b = run1("4")
    c = int(a) / 2
    run2("4", str(c))
    time.sleep(0.5)

    b = run1("5")
    c = int(a) ** 0.5 # tambien se podria usar la funcion "pow" - c = pow( 30, 1/2)
    c = round(c, 2)
    run2("5", str(c))
    time.sleep(0.5)
    
    b = run1("6")
    c = a[0:1]
    run2("6", str(c))