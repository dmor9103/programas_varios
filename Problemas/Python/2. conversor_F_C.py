#2. Realizar la conversión de una temperatura dada en grados Centígrados a grados Fahrenheit
#   La formula para convertir grados Celcius a grados Fahrenheit es: F° = ((C° * 1.8) + 32
#   La formula para convertir grados Fahrenheit a grados Celcius es C° = ((F° - 32) * 5) / 9
import time

def tmp():
    a = input("""
    Que tipo de medicion de temperatura usara
    - F = por grados Fahrenheit
    - C = por grados Centigrados/Celcius
    - : """)
    a = a.lower()
    return a


if __name__ == "__main__":
    tmp1 = tmp()
    print(tmp1)
    while tmp1 != "f" and tmp1 != "c":
        if tmp1 != "f" and tmp1 != "c":
            print("Opcion incorrecta... vuelve a intentarlo")
            time.sleep(1)
        tmp1 = tmp()
        print(tmp1)
    if tmp1 == "f":
        tmp2 = int(input("Digite los grados Celcius que desea convertir a grados Fahrenheit: "))
        tmp3 = ((tmp2 - 32) * 5) / 9
        print(str(tmp2) + "° Celcius, equivalen a " + str(tmp3) + "° Fahrenheit")
    else:
        tmp2 = int(input("Digite los grados Celcius que desea convertir a grados Fahrenheit: "))
        tmp3 = (tmp2 * 1.8) + 32
        print(str(tmp2) + "° Celcius, equivalen a " + str(tmp3) + "° Fahrenheit")
#    print("hola")
