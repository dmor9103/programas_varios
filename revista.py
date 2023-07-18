# Algoritmo de adquirir una revista
def rev():
    a = input("""
    - Revista Semana = 1
    - Revista carrusel = 2
    - Revista Nintendo = 3
    - Salir = 0
    """)
    return a


if __name__ == "__main__":
    contador = 1
    rev_00 = rev()
    while contador == 0:
        if int(rev_00) == 1:
            print("semana")
            contador = 1
    
#    if rev_00 >= 0 and rev_00<= 4:
#        
#    else:
#        print("nada")
#    in rev_00 == 1:
