# Mi primer calculadora
print("###########################")
print("########Calculadora########")
print("###########################")
print("Sumar es 1")
print("Restar es 2")
print("Multiplicar es 3")
print("Dividir es 4")
eleccion = int(input("Selecciona una opcion: "))
if eleccion == 1:
    numero1 = int(input("Digita el primer numero a sumar: "))
    numero2 = int(input("Digita el segundo numero a sumar: "))
    respuesta = str(numero1 + numero2)
    print("La operacion es: " + str(numero1) + " + " + str(numero2) + " = " + respuesta)
if eleccion == 2:
    numero1 = int(input("Digita el primer numero a restar: "))
    numero2 = int(input("Digita el segundo numero a restar: "))
    respuesta = str(numero1 + numero2)
    print("La operacion es: " + str(numero1) + " - " + str(numero2) + " = " + respuesta)
if eleccion == 3:
    numero1 = int(input("Digita el primer numero a multiplicar: "))
    numero2 = int(input("Digita el segundo numero a multiplicar: "))
    respuesta = str(numero1 + numero2)
    print("La operacion es: " + str(numero1) + " * " + str(numero2) + " = " + respuesta)
if eleccion == 4:
    numero1 = int(input("Digita el primer numero a dividir: "))
    numero2 = int(input("Digita el segundo numero a dividir: "))
    respuesta = str(numero1 + numero2)
    print("La operacion es: " + str(numero1) + " / " + str(numero2) + " = " + respuesta)