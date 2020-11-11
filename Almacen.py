from tkinter import *
from tkinter import messagebox
#from funciones import *
import time
import datetime
import sqlite3


#-------------Interfaz grafica------------

raiz=Tk()
raiz.geometry("750x510")
raiz.config(border=7, bg="#3300CC")
raiz.resizable(0, 0)

raiz.title("VARIEDADES MARY")
raiz.config()

miFrame=Frame(raiz, width=120)
miFrame.config(bg="#0066CC") 
miFrame.pack(fill="both", expand=1)

Nombre=Label(miFrame, text="VARIEDADES MARY", fg="red", font=("Verdana",24), justify="right", bg="lightblue")
Nombre.grid(row=0, column=0, pady=30, columnspan=2)

#-------------Funciones--------------------------

def conexionBBDD():

	miConexion=sqlite3.connect("Ventas")

	miCursor=miConexion.cursor()

	try:

		miCursor.execute('''
			CREATE TABLE REGISTRO_VENTAS (
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			ARTICULO VARCHAR(50),
			PRECIO VARCHAR(50),
			CLIENTE VARCHAR(10),
			VENDEDOR VARCHAR(50),
			FECHA TIMESTAMP,
			OBSERVACIONES VARCHAR (100))
			''')

		messagebox.showinfo("BBDD", "BBDD creada con exito")

	except:

		messagebox.showwarning("¡Atencion!", "La BBDD ya existe")


def salirAplicacion():

	valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")

	if valor=="yes":
		raiz.destroy()

def Registrar():

	miConexion=sqlite3.connect("Ventas")

	miCursor=miConexion.cursor()

	
	datos=miArticulo.get(),miPrecio.get(),miCliente.get(),miVendido.get(),miFecha.get(),textObservaciones.get(1.0, END)

	miCursor.execute("INSERT INTO REGISTRO_VENTAS VALUES(NULL,?,?,?,?,?,?)",(datos))

	miConexion.commit()

	messagebox.showinfo("BBDD", "Registro insertado con exito")

def borrarCampos():

	miId.set("")
	miFecha.set("")
	miArticulo.set("")
	miPrecio.set("")
	miCliente.set("")
	miVendido.set("")
	textObservaciones.delete(1.0, END)


#-------------Aqui van los label y los cuadros de texto---------------
miId=StringVar()
miArticulo=StringVar()
miPrecio=StringVar()
miCliente=StringVar()
miVendido=StringVar()
miFecha=StringVar()

#var=time.strftime ("%x""-""%X")

Id=Label(miFrame, text="ID", font=20).grid(row=1, column=0)

cuadroId=Entry(miFrame, fg="red", textvariable=miId).grid(row=2, column=0, padx=120, pady=20)

fecha=Label(miFrame, text="FECHA", font=20).grid(row=1, column=1)

cuadroFecha=Entry(miFrame, textvariable=miFecha).grid(row=2, column=1)

Articulo=Label(miFrame, text="ARTICULO", font=20, justify="right").grid(row=3, column=0)

cuadroArticulo=Entry(miFrame, textvariable=miArticulo).grid(row=4, column=0, sticky="w", padx=120, pady=20)

Precio=Label(miFrame, text="PRECIO", font=20).grid(row=3, column=1)

cuadroPrecio=Entry(miFrame, textvariable=miPrecio).grid(row=4, column=1, padx=10, pady=20)

Cliente=Label(miFrame,text="NOMBRE DEL CLIENTE", font=20).grid(row=5, column=0)

cuadroCliente=Entry(miFrame, textvariable=miCliente).grid(row=6, column=0, padx=120, pady=20)

vendidopor=Label(miFrame, text="VENDIDO POR", font=20).grid(row=5, column=1)

cuadroVendidoPor=Entry(miFrame, textvariable=miVendido).grid(row=6, column=1, padx=120, pady=20)

Obervaciones=Label(miFrame, text="OBSERVACIONES", font=20).grid(row=7, column=0)

textObservaciones=Text(miFrame, width=16, height=5)
textObservaciones.grid(row=8, column=0, padx=1, pady=10)

#---------------Aqui van los botonnes-----------

botonRegistro=Button(miFrame, text="REGISTRAR VENTA", font=24, pady=8, padx=40, command=Registrar).grid(row=8, column=1)

#-----------------Menu-------------------------

barraMenu=Menu(raiz)
raiz.config(menu=barraMenu)

Archivomenu=Menu(barraMenu, tearoff=0)
Archivomenu.add_command(label="Conectar", command=conexionBBDD)
Archivomenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=borrarCampos)

barraMenu.add_cascade(label="Archivo", menu=Archivomenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)




raiz.mainloop()

