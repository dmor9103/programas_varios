import time

def run():
    nom = input("Digita un nombre: ")
    nom = nom.capitalize()
    return nom

def trufa():
    if cont == 0:
        a = input("""
    Desea mostrar su nombre?
    - Si - No: """)
    else:
        a = input("""
    Desea borrar su nombre de la lista
    - Si - No: """)
    a = a.lower()
    if a == "si":
        return True
    else:
        return False
    

# def ver_nom():
#     b = input("""
#     Desea mostrar su nombre?
#     - Si - No: """)
#     b = b.lower()
#     if b == "si":
#         return True
#     else:
#         return False

# def mos_nom():
#     c = input("""
#     Desea borrar su nombre de la lista
#     - Si - No: """)
#     c = c.lower()
#     if c == "si":
#         return True
#     else:
#         return False
    # si, no = True, False
    # if a == True:
    #     a = [1, True]
    # else:
    #     a = [0, False]
    # return a




if __name__ == "__main__":
    rep = "si"
    while rep != "no":
        nom = []
        cont = int(0)
        nom_1 = run()
        print(nom_1)
        nom.append(nom_1)
        a = trufa()
        cont = cont + 1
        if a == True:
            print(nom)
            time.sleep(1)
        a = trufa()
        if a == True:
            nom.pop(cont)
            print("Tu nombre ya no est en la lista " + str(nom))
            cont = cont - 1
        else:
            print("Tu nombre sigue en la lista " + str(nom))
        rep = input("""
        Desea continuar?
        - Si - No: """)
        rep = rep.lower()
    time.sleep(1)
    print("-- Adios!!! --")
    time.sleep(1)
    # print(str(nom))