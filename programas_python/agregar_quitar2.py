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



if __name__ == "__main__":
    rep = "si"
    while rep != "no":
        nom = []
        cont = int(0)
        for i in range(1, 1000):
            print(nom_+str(i))
            nom.append(nom_+str(i))
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
