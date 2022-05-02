

from tkinter import *
import random

class SieteAfortunado:
    def __init__(self):
        self.crear_interfaz()
    def crear_interfaz(self):
        ventana = Tk()
        ventana.minsize(340,450)
        ventana.geometry('340x430')

        boton = Button(ventana,text="JUGAR", command=self.jugar, font="arial 18 bold")
        boton.pack()

        foto = PhotoImage(file= r'images/dinero.png', width="300", height="280" )
        self.gano = Label(ventana,image=foto)

        self.campos = [StringVar() for elemento in range(3)]
        posicion=10
        for campo in self.campos:
            label = Label(ventana,  textvariable=campo, background="white", foreground="black",font="arial 22 bold")
            label.place(x=posicion, y=100, width=100, height=100)
            posicion +=110 
        mainloop()

    def genera_aleatorios(self):
        return random.randint(0,9)
    def jugar(self):
        existe_siete= False
        for i in range(3):
            valor = self.genera_aleatorios()
            self.campos[i].set(valor)
            if(valor == 7):
                existe_siete=True
        if(existe_siete):
            self.gano.pack(side=BOTTOM)
        else:
            self.gano.pack_forget()
jugar = SieteAfortunado()