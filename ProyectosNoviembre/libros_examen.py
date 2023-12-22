import tkinter as tk

root=tk.Tk()


fuente=("Comic Sans MS",11,"bold")
fuente2=("Courier",10,"bold")
fuente3=("bold")
fuente4=("Comic Sans MS",20,"roman")


revista1= ("Olé es un diario argentino de deportes," 
	" editado en Buenos Aires desde el 23 de mayo de 1996, por el Grupo Clarín en formato tabloide.")
revista2=("Cosmopolitan es una revista femenina mensual. Comenzó en los Estados Unidos como una revista familiar y" 
	" su primer número fue publicado en 1886 por Schlicht & Field, bajo el título The Cosmopolitan." 
	" En la actualidad existen numerosas ediciones en distintos idiomas.")
revista3=("Revista Contexto Tucumán es un diario digital de la ciudad de San Miguel de Tucumán, Argentina." 
	" Fundada el 20 de junio de 1997 por el periodista y politólogo porteño Tomás Ezequiel Luciani,"
	" fue impresa en papel semanalmente hasta el año 2010 cuando pasó a estar disponible exclusivamente a través de internet.")

libro1= ("La Biblia. 3.900 millones de copias. La Biblia es el conjunto de libros canónicos del judaísmo y el cristianismo." 
	" La canonicidad de cada libro varía dependiendo de la tradición adoptada. Según las religiones judía y cristiana,"
	" transmite la palabra de Dios.")

libro2=("El Alquimista (de Paulo Coelho) 65 millones de copias. El alquimista es un libro escrito por el escritor brasileño"
	" Paulo Coelho que ha sido traducido a más de 63 lenguas y publicado en 150 países, y que ha vendido un total de 65 millones de copias" 
	" en todo el mundo.1 El libro trata sobre los sueños y los medios que utilizamos para alcanzarlos, sobre el azar en nuestra vida y" 
	" las señales que se presentan a lo largo de esta.")

libro3=(" El diario de Ana Frank (de Anna Frank). 27 millones de copias."
	"Con el título de El diario de Ana Frank se conoce la edición de los diarios personales escritos por la niña judía Ana Frank" 
	" (Annelies Marie Frank) entre el 12 de junio de 1942 y el 1 de agosto de 1944 en un total de tres cuadernos conservados a la" 
	" actualidad, donde relata su historia como adolescente y el tiempo de dos años cuando tuvo que ocultarse de los nazis en Ámsterdam,"
	" durante la Segunda Guerra Mundial.")


def ventanaRevista():
	ventana1=tk.Toplevel(root)
	ventana1.title("REVISTAS")
	etiq2= tk.Label(ventana1,text="Mis Diarios y Revistas",font=fuente,bg="yellow",width=45,height=4,relief="groove").pack()
	botonrevista1= tk.Button(ventana1,text="Revista 1",command=abrirRevista1,width=50,height=3,font=fuente2).pack()
	botonrevista2= tk.Button(ventana1,text="Revista 2",command=abrirRevista2,width=50,height=3,font=fuente2).pack()
	botonrevista3= tk.Button(ventana1,text="Revista 3",command=abrirRevista3,width=50,height=3,font=fuente2).pack()
	ventana1.resizable(0,0)
	btn3=tk.Button(ventana1,text="Cerrar",command=ventana1.destroy,font=fuente2,relief="solid",bg="brown1").pack(fill=tk.BOTH)

def ventanaLibros():
	ventana1=tk.Toplevel(root)
	ventana1.title("Libros")
	etiq2= tk.Label(ventana1,text="Mis Libros",font=fuente,bg="aqua",width=45,height=4,relief="groove").pack()
	botonrevista1= tk.Button(ventana1,text="Libro 1",command=abrirLibro1,width=50,height=3,font=fuente2).pack()
	botonrevista2= tk.Button(ventana1,text="Libro 2",command=abrirLibro2,width=50,height=3,font=fuente2).pack()
	botonrevista3= tk.Button(ventana1,text="Libro 3",command=abrirLibro3,width=50,height=3,font=fuente2).pack()
	ventana1.resizable(0,0)
	btnCerrar=tk.Button(ventana1,text="Cerrar",command=ventana1.destroy,font=fuente2,relief="solid",bg="brown1").pack(fill=tk.BOTH)

def abrirRevista1():
	ventana=tk.Toplevel(root)
	ventana.title("Revista 1")
	etiq2=tk.Label(ventana,text="Diario Olé",bg="yellow",width=100,height=2,font=fuente).pack()
	etiq1=tk.Label(ventana,text=revista1,width=100,height=5,wraplength=500,font=fuente3,bg="lightblue").pack()
	ventana.resizable(0,0)
	btnCerrar=tk.Button(ventana,text="Cerrar",command=ventana.destroy,font=fuente2,relief="solid",bg="brown1").pack(fill=tk.BOTH)


def abrirRevista2():
	ventana=tk.Toplevel(root)
	ventana.title("Revista 2")
	etiq2=tk.Label(ventana,text="Cosmopolitan",width=100,height=2,bg="yellow",font=fuente).pack()
	etiq1=tk.Label(ventana,text=revista2,width=100,height=10,wraplength=500,font=fuente3,bg="lightblue").pack()
	ventana.resizable(False,False)
	btnCerrar=tk.Button(ventana,text="Cerrar",command=ventana.destroy,font=fuente2,relief="solid",bg="brown1").pack(fill=tk.BOTH)

def abrirRevista3():
	ventana=tk.Toplevel(root)
	ventana.title("Revista 3")
	etiq2=tk.Label(ventana,text="Contexto Tucumán",width=100,height=2,bg="yellow",font=fuente).pack()
	etiq1=tk.Label(ventana,text=revista3,width=100,height=10,wraplength=500,font=fuente3,bg="lightblue").pack()
	ventana.resizable(0,0)
	btnCerrar=tk.Button(ventana,text="Cerrar",command=ventana.destroy,font=fuente2,relief="solid",bg="brown1").pack(fill=tk.BOTH)

def abrirLibro1():
	ventana=tk.Toplevel(root)
	ventana.title("Libros 1")
	etiq2=tk.Label(ventana,text="La Biblia",width=110,height=2,bg="aqua",font=fuente).pack()
	etiq1=tk.Label(ventana,text=libro1,wraplength=500,font=fuente3,width=110,height=7,bg="lightgreen").pack()
	ventana.resizable(0,0)
	btnCerrar=tk.Button(ventana,text="Cerrar",command=ventana.destroy,font=fuente2,relief="solid",bg="brown1").pack(fill=tk.BOTH)

def abrirLibro2():
	ventana=tk.Toplevel(root)
	ventana.title("Libros 2")
	etiq2=tk.Label(ventana,text="El Alquimista",width=100,height=2,bg="aqua",font=fuente).pack()
	etiq1=tk.Label(ventana,text=libro2,wraplength=600,font=fuente3,width=100,height=10,bg="lightgreen").pack()
	ventana.resizable(0,0)
	btnCerrar=tk.Button(ventana,text="Cerrar",command=ventana.destroy,font=fuente2,relief="solid",bg="brown1").pack(fill=tk.BOTH)

def abrirLibro3():
	ventana=tk.Toplevel(root)
	ventana.title("Libros 3")
	etiq2=tk.Label(ventana,text="Ana Frank",width=120,height=2,bg="aqua",font=fuente).pack()
	etiq1=tk.Label(ventana,text=libro3,wraplength=600,font=fuente3,width=120,height=10,bg="lightgreen").pack()
	ventana.resizable(0,0)
	btnCerrar=tk.Button(ventana,text="Cerrar",command=ventana.destroy,font=fuente2,relief="solid",bg="brown1").pack(fill=tk.BOTH)



etiq1=tk.Label(root,text="Libreria",relief="ridge",bg="black",fg="yellow",height=4,width=50,font=fuente4).pack()

root.title("Libros - Revistas")

#root.resizable(0,0)

boton1=tk.Button(root,text="REVISTAS",fg="black",height=3,width=88,command=ventanaRevista,font=fuente,bg="yellow").pack()

boton2=tk.Button(root,text="LIBROS",fg="black",height=3,width=88,command=ventanaLibros,font=fuente,bg="aqua").pack()

botonSalir=tk.Button(root,text="Salir",command=root.quit,font=fuente2,relief="solid",bg="brown1").pack(side="bottom")

root.mainloop()