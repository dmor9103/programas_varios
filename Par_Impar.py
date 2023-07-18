def i_par():
    nae = int(input("digite un numero para comprobar si es impar o no: "))
    r = nae % 2
    return nae, r


if __name__ == "__main__":
    nae, r = i_par()
    if r == 0:
        print(str(nae) + " es par.")
    else:
        print(str(nae) + " no es par.")
