# Conversor de monedas
def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿cuantos pesos " + tipo_pesos + " tienes: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $ " + dolares + " dolares")

menu = """
💲💲💲 Bienvenido al coversor de monedas 💲💲💲

1️⃣ = Pesos Colombianos
2️⃣ = Pesos Argentinos
3️⃣ = Pesos mexicanos

Elige una opcion: """
opcion = int(input(menu))
if opcion == 1:
    conversor("Colombianos", 3875)
elif opcion == 2:
    conversor("Argentinos", 65)
elif opcion == 3:
    conversor("Argentinos", 24)
else:
    print("ingresa una opcion correcta")