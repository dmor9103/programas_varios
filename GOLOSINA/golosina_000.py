# hay 5 unidades de cada golosina

import msvcrt
import getpass
import time
from os import system

def pedir_golosinas():
    system("cls")
    print("#############################################################################################################")
    print("#                                         PEDIR GOLOSINAS                                                   #")
    print("#                                          by: Demor9103                                                    #")
    print("#############################################################################################################")
    print("")
    print("-Recuerde que el primer digito indica la fila y el segundo la columna-")
    a = input("Digite que golosina quiere: ")
    b = a[0:1]
    c = a[1:2]
    print("")
    print("Productos: " + str(nombresGolosinas[int(b) - 1][int(c)]))
    cantidad[int(b)][int(c)] -= 1
    vendidos[int(b)][int(c)] += 1
    print("")
    print("Precio: " + str(precios[int(b) - 1][int(c)]))
    d = precios[int(b) - 1][int(c)]
    print("")
    print("Presione una tecla para continuar...")
    msvcrt.getch()
    system("cls")
    return d


def mostrar_golosinas():
    system("cls")
    print("#############################################################################################################")
    print("#                                        MOSTRAR GOLOSINAS                                                  #")
    print("#                                          by: Demor9103                                                    #")
    print("#############################################################################################################")
    print("")
    a = 0
    while a <= 3:
        print(a)
        b = 0
        while b <= 3:
            print("- Producto: " + str(nombresGolosinas[int(a)][int(b)]))
            print("- Precio: " + str(precios[int(a)][int(b)]))
            print("- Codigo: " + str(int(a) + 1) + str(b))
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            b += 1
        a += 1
    print("")
    print("Presione una tecla para continuar...")
    msvcrt.getch()
    system("cls")
            


def rellenar_golosinas():
    system("cls")
    print("#############################################################################################################")
    print("#                              MENU DE ADMINISTRADOR - RELLENAR GOLOSINA                                    #")
    print("#                                          by: Demor9103                                                    #")
    print("#############################################################################################################")
    print("")
    a = getpass.getpass("Digite la contraseña: ")
    print("")
    if a == "hola":
        a = input("Digite que golosina: ")
        b = a[0:1]
        c = a[1:2]
        print(nombresGolosinas[int(b) - 1][int(c)])
        print("")
        d = input("Que cantidad desea: ")
        cantidad[int(b)][int(c)] += int(d)
        print("")
        print("Se ha agregado la cantidad: " + str(cantidad[int(b)][int(c)]) + " - a la golosina: " + str(nombresGolosinas[int(b) - 1][int(c)]))
    print("")
    print("Presione una tecla para continuar...")
    msvcrt.getch()
    system("cls")
        


def mostrar_cantidad_golosinas():
    system("cls")
    print("#############################################################################################################")
    print("#                                      CANTIDAD DE GOLOSINAS                                                #")
    print("#                                          by: Demor9103                                                    #")
    print("#############################################################################################################")
    print("")
    a = 0
    while a <= 3:
        print(a)
        b = 0
        while b <= 3:
            print("- Producto: " + str(nombresGolosinas[int(a)][int(b)]) + " - Cantidad: " + str(cantidad[int(a)][int(b)]))
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            b += 1
        a += 1
    print("")
    print("Presione una tecla para continuar...")
    msvcrt.getch()
    system("cls")
    

def total_vendido():
    a = round(total, 2)
    print("Se ha vendido un total de: " + str(a))
    print("")
    print("Presione una tecla para continuar...")
    msvcrt.getch()
    system("cls")


def conteo_golosinas_vendidas():
    system("cls")
    print("#############################################################################################################")
    print("#                                    CONTEO DE GOLOSINAS VENDIDAS                                           #")
    print("#                                          by: Demor9103                                                    #")
    print("#############################################################################################################")
    print("")
    a = 0
    while a <= 3:
        print(a)
        b = 0
        while b <= 3:
            c = vendidos[int(a)][int(b)] * precios[int(a)][int(b)]
            print("- Producto: " + str(nombresGolosinas[int(a)][int(b)]))
            print("- Vendidas: " + str(vendidos[int(a)][int(b)]))
            print("- vendido $: " + str(round(c, 2)))
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            b += 1
        a += 1
    print("")
    print("Presione una tecla para continuar...")
    msvcrt.getch()
    system("cls")


if __name__ == "__main__":
    system("cls")
    nombresGolosinas = [("KitKat", "Chicles de fresa", "Lacasitos", "Palotes"), ("Kinder Bueno", "Bolsa variada Haribo", "Chetoos", "Twix"), ("Kinder Bueno", "M&M'S", "Papa Delta", "Chicles de menta"), ("Lacasitos", "Crunch", "Milkybar", "KitKat")]
    precios = [(1.1, 0.8, 1.5, 0.9), (1.8, 1, 1.2, 1), (1.8, 1.3, 1.2, 0.8), (1.5, 1.1, 1.1, 1.1)]
    cantidad = [[5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]]
    vendidos = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    cont = 1
    total = 0
    while cont == 1:
        print("#############################################################################################################")
        print("#                                       MAQUINA DE GOLOSINAS                                                #")
        print("#                                          by: Demor9103                                                    #")
        print("#############################################################################################################")
        print("""
              - 1 : Pedir golosinas
              - 2 : Mostrar golosinas
              - 3 : Apagar maquina
              - 4 : Mostrar cantidad de golosinas (opcion no incluida en el problema)
              - 5 : Total vendido (opcion no incluida en el problema)
              - 6 : Conteo de golosinas vendidas (opcion no incluida en el problema)
              
              - 0 : Rellenar golosinas (accion exclusiva del administrador, requiere contraseña)""")
        print("")
        a = int(input("que desea hacer: "))
        print("")
        if a == 1:
            t = pedir_golosinas()
            total = total + t
        elif a == 2:
            mostrar_golosinas()
        elif a == 3:
            cont = 0
        elif a == 4:
            mostrar_cantidad_golosinas()
        elif a == 5:
            total_vendido()
        elif a == 6:
            conteo_golosinas_vendidas()
        elif a == 0:
            rellenar_golosinas()
        else:
            print("")
            print("OPCION INCORRECTA!!!")
            time.sleep(0.5)
            print("")
            print("Vuelva a intentarlo")
    print("Se vendio un total de: " + str(total))
    print("")
    print("Presione una tecla para salir...")
    msvcrt.getch()
    
    