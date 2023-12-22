#                                                       INTERFACES GRAFICAS I : Raiz
# librerias: Tkinter es un puente entre python y la libreria TCL/TK
#            WxPython
#            PyQT
#            PyGTK

#son intermediarios entre el programa y los usuarios
# son denominadas GUI y estan formadas por un conjunto de graficos como ventanas,botones,menus,casillas de verificacion,etc.
#
#
'''
from tkinter import *

raiz=Tk() # realizas la primera ventana

raiz.title("Ventana de pruebas") #le damos titulo a la ventana

raiz.resizable(0,0) # redimensiona la ventana (tamaño)... se le pasa 2 parametros (width= ancho, height=alto)

raiz.iconbitmap("imagen-para-ventana.ico") #modifica la imagen del icono de la ventana

raiz.geometry("650x350") # entre comillas el ancho y el alto

raiz.config(bg="red") # damos color al fondo de la ventana con bg=background

raiz.mainloop()  # para q pueda estar en ejecucion infinita y siemporoe al final

#PARA q no abra la consola al abrir la ventana, hay q cambiarle el nombre a .pyw

'''


#                                                       INTERFACES GRAFICAS II : Frame

'''
from tkinter import *

raiz=Tk() # realizas la primera ventana

raiz.title("Ventana de pruebas") #le damos titulo a la ventana

#raiz.resizable(0,0) # redimensiona la ventana (tamaño)... se le pasa 2 parametros (width= ancho, height=alto)

raiz.iconbitmap("imagen-para-ventana.ico") #modifica la imagen del icono de la ventana

#raiz.geometry("650x350") # entre comillas el ancho y el alto

raiz.config(bg="red") # damos color al fondo de la ventana con bg=background

raiz.config(bd=45)  #dandole borde a la raiz

raiz.config(relief="groove") #distintos tipos de bordes ""

raiz.config(cursor="hand2") #el cursor se transforma

miFrame=Frame() #construccion de frame pero hay q empaquetarlo a la raiz

miFrame.pack()    #empaquetando

#miFrame.pack(side="bottom", anchor="w")   # enpaquetamos el frame dentro de la raiz dandole parametros

#miFrame.pack(fill="x")

#miFrame.pack(fill="both", expand="True")  #se expande al nivel de la raiz

miFrame.config(bg="blue")   #color al frame

miFrame.config(width="650",height="350") #cambiamos tamaño del frame

miFrame.config(bd=35)  #dandole borde

miFrame.config(relief="sunken") #distintos tipos de bordes ""

miFrame.config(cursor="pirate") #el cursor se transforma dentro del frame

raiz.mainloop()  # para q pueda estar en ejecucion infinita y siemporoe al final
'''

#                                                       INTERFACES GRAFICAS III :Widget Label

# MOSTRAMOS UN TEXTO o IMAGENES, NO SE PUEDE INTERACTUAR
#SINTAXIS:  Label(contenedor,opciones)
'''
from tkinter import *

root=Tk()

miFrame=Frame(root,width=500,height=400)

miFrame.pack()
#Label(miFrame, text="hola mundo", fg="red", font=("Comic Sans MS",18)).place(x=100,y=200)  # reciclamos lineas.
#miLabel=Label(miFrame, text="hola mundo") #ingresamos el texto y podemos agregar muchas opciones
#miLabel.place(x=100,y=200)   # ubica el texto en cualquier lugar de nuestra interfaz grafica

miImagen=PhotoImage(file="homero.gif") # busco la imagen en el directorio o ingreso el nombre del archivo si se encuentra en la misma carpeta

Label(miFrame,image=miImagen).place(x=100,y=200)  #uso la funcion de label para mostrar la imagen

root.mainloop()
'''

#                                                       INTERFACES GRAFICAS IV: Widget Entry
'''
#utilizado para ingresar texto

from tkinter import *

raiz=Tk()

miFrame=Frame(raiz,width=1200, height=600) #creacion del frame...(lugar , tamaño)

miFrame.pack()

cuadroNombre=Entry(miFrame)   #cuadro de ingreso de texto
#cuadroTexto.place(x=100, y=100)   #ubicacion del cuadro
cuadroNombre.grid(row=0, column=1,padx=10, pady=10)   #dividimos en una grilla con grid y damos ubicacion
cuadroNombre.config(fg="red", justify="center") #ingresamos texto de color y alineamos texto al centro

cuadroPass=Entry(miFrame)  
cuadroPass.grid(row=1, column=1,padx=10, pady=10)
cuadroPass.config(show="*") # muestra el caracter entre comillas
                
cuadroApellido=Entry(miFrame)  
cuadroApellido.grid(row=2, column=1,padx=10, pady=10)


cuadroDireccion=Entry(miFrame)   
cuadroDireccion.grid(row=3, column=1,padx=10, pady=10) 

nombreLabel=Label(miFrame, text="Nombre:") #creacion de un texto a mostrar
#nombreLabel.place(x=100,y=100) #ubicacion
nombreLabel.grid(row=0, column=0,padx=10, pady=10)  #ubicamos el texto en el primer lugar de la grilla

ApellidoLabel=Label(miFrame, text="Apellido:")  
ApellidoLabel.grid(row=2, column=0, sticky="w")  #sticky me alinea el texto a la derecha (east en ingles)

DireccionLabel=Label(miFrame, text="Direccion de casa:") 
DireccionLabel.grid(row=3, column=0, padx=10, pady=10) #con padx y pady sirve para ubicar a determinada cantidad de pixeles 

PassLabel=Label(miFrame, text="Contraseña:")  
PassLabel.grid(row=1, column=0, padx=10, pady=10)

raiz.mainloop()
'''

#                                                       INTERFACES GRAFICAS V: Widget Text y Button
# Text: para introduccion de textos largos
# Button: sirve para construir botones e interactuar con la interfaz

'''
from tkinter import *

raiz=Tk()

miFrame=Frame(raiz,width=1200, height=600) 

miFrame.pack()

# ENTRYS
minombre=StringVar() # se trata de una cadena de caracteres
cuadroNombre=Entry(miFrame,textvariable=minombre) #se asocia a la variable minombre  
cuadroNombre.grid(row=0, column=1,padx=10, pady=10)  
cuadroNombre.config(fg="red", justify="center") 

cuadroPass=Entry(miFrame)  
cuadroPass.grid(row=1, column=1,padx=10, pady=10)
cuadroPass.config(show="*") 
                
cuadroApellido=Entry(miFrame)  
cuadroApellido.grid(row=2, column=1,padx=10, pady=10)

cuadroDireccion=Entry(miFrame)   
cuadroDireccion.grid(row=3, column=1,padx=10, pady=10)

textoComentario=Text(miFrame, width=16,height=5)     #ingresamos un text grande
textoComentario.grid(row=4, column=1,padx=10, pady=10)

scrollvert=Scrollbar(miFrame, command=textoComentario.yview) #  le decimos que pertenece al Text y funciona de manera vertical
scrollvert.grid(row=4, column=2, sticky="nsew") # agregamos el scroll con grid y lo adaptamos al tamaño del cuadro comentarios
textoComentario.config(yscrollcommand=scrollvert.set)  # posiciona la barra donde voy escribiendo

#LABELS
nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0,padx=10, pady=10)  

ApellidoLabel=Label(miFrame, text="Apellido:")  
ApellidoLabel.grid(row=2, column=0, sticky="w")  

DireccionLabel=Label(miFrame, text="Direccion:") 
DireccionLabel.grid(row=3, column=0, padx=10, pady=10)  

PassLabel=Label(miFrame, text="Contraseña:")  
PassLabel.grid(row=1, column=0, padx=10, pady=10)

ComentariosLabel=Label(miFrame, text="Comentarios:")  
ComentariosLabel.grid(row=4, column=0, padx=10, pady=10, sticky="e")

#BOTONES

def codigoBoton():  #se crea una funcion del boton
    minombre.set("Juan") #se establece un valor a una variable utilizando .set
    
botonEnvio=Button(raiz, text="Enviar", command= codigoBoton) # raiz es contenedor padre, texto del boto y accion del boton
botonEnvio.pack()
'''
'''














