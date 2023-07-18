# formulario y gestor de edad
def eleccion(opcion2):
    print("Seleccionaste la opcion " + opcion2)
    print("Nombre completo es: " + name + " " + bname + " y la edad es: " + edad)

print("""
Bienvenido al formulario
Porfavor digita tus datos
""")
name=input("Tu Nombre: ")
bname=input("Tu Apellido: ")
edad=int(input("Tu edad: "))
opcion1=input("""
¿Desea mostrar sus datos?
Si = 1 - No = 0 : 
""")
if opcion1==1:
    eleccion("1")
elif opcion1==0:
    eleccion("0")
    print("adios!")
