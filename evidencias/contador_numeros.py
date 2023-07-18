from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font

A = 0

# def run():
#     a = []
#     con = 1
#     con_n = 0
#     con_s = 0
#     while int(con) == 1:
#         b = int(input("Introducir un número: "))
#         a.append(b)
#         print(str(b))
#         con_n = int(con_n) + 1
#         con_s = int(con_s) + int(b)
#         con = input("Desea continuar: ")
#     if int(con) == 0:
#         print(str(con_n))
#         print(str(con_s))


# if __name__ == "__main__":
#     run()

def run():
    ven_no = Toplevel()
    ven_no.grab_set()
    ven_no.focus_set()
    ven_no.geometry("300x160")
    ven_no.title("Nop")
    add = ttk.Label(ven_no, text="Conteo de números ingresados:", foreground="black", font=Font(size=14))
    add.place(x=16, y=10)
    add = ttk.Label(ven_no, text=str(b), foreground="red", font=Font(size=20))
    add.place(x=140, y=40)
    add = ttk.Label(ven_no, text="Suma de números ingresados:", foreground="black", font=Font(size=14))
    add.place(x=20, y=80)
    add = ttk.Label(ven_no, text=str(c), foreground="red", font=Font(size=20))
    add.place(x=140, y=110)
        

def ven_sec():
    ven_sec = Toplevel()
    ven_sec.grab_set()
    ven_sec.focus_set()
    ven_sec.geometry("280x150")
    ven_sec.title("SI & NO")
    A = numero1.get()
    add = ttk.Label(ven_sec, text="AGREGADO!", foreground="green", font=Font(size=20))
    add.place(x=56, y=10)
    si_1 = tk.Button(ven_sec, text="Si", height = 2, width = 2, background="yellow", command=ven_sec.destroy)
    si_1.place(x=80, y=100)
    no_1 = tk.Button(ven_sec, text="No", height = 2, width = 2, background="red", command=run)
    no_1.place(x=180, y=100)
    global b
    global c
    if A != "":
        a.append(A)
        b += 1
        c += int(A)
        numero1.delete(0, END)
    print('dato ingresado: ' + str(a) + ", conteo: " + str(b) + ", suma total de la lista: " + str(c))
    return a, b, c


if __name__ == "__main__":
    v = tk.Tk()
    v.geometry("400x200")
    v.title("Contador de Números")
    a = []
    b = 0
    c = 0
    num1 = ttk.Label(text="Ingresa un número", font=Font(size=20))
    num1.place(x=80, y=20)
    numero1 = ttk.Entry()
    numero1.place(x=160, y=80, width=80)
    comparar = tk.Button(v, text="Agregar", command= ven_sec)
    comparar.place(x=175, y=120)
    v.mainloop()