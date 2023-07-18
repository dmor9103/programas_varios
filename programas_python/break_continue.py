def run():
    contador = input("Digita desde que numero comenzara el contador: ")
    rango = input("digita un rango el rango del contador:")
    for contador in range(int(rango)):
        if contador % 2 != 0:
            continue
        print(contador)

# def run2():
#     for i in range(10000):
#         print(i)
#         if i == 5678:
#             break

# def
#     texto = input("digite un texto: ")
#     for letra in texto:
#         if letra == "o":
#             break
#         print(letra)

if __name__ == "__main__":
    run()