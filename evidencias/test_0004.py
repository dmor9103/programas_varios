import tkinter as tk   # Python 2.x
#import tkinter as tk  # Python 3.x


class Recovery(tk.Toplevel):
    def __init__(self, parent=None, *args, **kwargs):
        tk.Toplevel.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.value = tk.IntVar(self)
        self.value.set(2)

        op1 = tk.Radiobutton(self, text="Usuario", variable=self.value,
                             value=1, command=self.selected
                            )
        op2 = tk.Radiobutton(self, text="ContraseÃ±a", variable=self.value,
                             value=2, command=self.selected
                            )
        op1.grid(row=0, sticky=tk.W)
        op2.grid(row=1, sticky=tk.W)

    def selected(self):
        print(self.value.get())


class Login(tk.Frame):
    def __init__(self, parent=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.recovery = tk.Button(self, text="Recuperar Cuenta",
                                  command=self.recover_password
                                 )
        self.data_user = tk.Entry(self)
        self.data_user.pack(side="top")
        self.recovery.pack(side="bottom")

    def recover_password(self):
        Recovery()


if __name__ == "__main__":
    root = tk.Tk()
    Login(root).pack(side="top", fill="both", expand=True)
    root.mainloop()