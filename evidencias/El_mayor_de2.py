from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def run():
        n1 = numero1.get()
        n2 = numero2.get()
        if int(n1) > int(n2):
            messagebox.showinfo(message="El número mayo es :" + str(n1), title="Lerroy Jenkins")
        elif int(n1) < int(n2):
            messagebox.showinfo(message="El número mayo es :" + str(n2), title="Lerroy Jenkins")
        else:
            messagebox.showinfo(message="Los números son iguales", title="Lerroy Jenkins")
        numero1.delete(0, END)
        numero2.delete(0, END)
   


if __name__ == "__main__":
    v = tk.Tk()
    v.geometry("400x220")
    v.title("El Mayor de dos Números")
    pro = ttk.Label(text="Digita 2 número para comparar cual es el mayor", background="black", foreground="white")
    pro.place(x=80, y=20)
    num1 = ttk.Label(text="Primer número")
    num1.place(x=120, y=80)
    numero1 = ttk.Entry()
    numero1.place(x=220, y=80, width=40)
    num2 = ttk.Label(text="Segundo número")
    num2.place(x=120, y=140)
    numero2 = ttk.Entry()
    numero2.place(x=220, y=140, width=40)
    comparar = tk.Button(text="Comparar", background="yellow", command=run)
    comparar.place(x=300, y=106)
    v.mainloop()