def no_elegir(nada):
    print("no elegiste la opcion " + nada)
nombre=input("Tu nombre es?: ")
apellido=input("Tu apellido es?: ")
edad=int(input("Tu edad es?: "))
menu="""
Desea mostrar su nombre?
0 - No
1 - Si
"""
eleccion=int(input(menu))
if eleccion==1:
    nombre=nombre.replace("1", " ")
    nombre=nombre.strip()
    print("Nombre: "+nombre.capitalize()+" " +apellido.capitalize())
    print(edad)
elif eleccion==0:
    no_elegir("0")