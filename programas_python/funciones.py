# funcion
def numero_elegido(mensaje):
    print("Hola mundo, elegiste la opcion " + mensaje + " adios.")
eleccion = int(input("Elige la opcion - 1 - 2 - 3 -: "))
if eleccion == 1:
    numero_elegido("1")
elif eleccion == 2:
    numero_elegido("2")
elif eleccion == 3:
    numero_elegido("3")
else:
    print("no elegiste bien.")