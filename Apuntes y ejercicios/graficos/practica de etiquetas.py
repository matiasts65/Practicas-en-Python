
'''
import tkinter as tk

root=tk.Tk()

fuente=("Arial",12,"roman")

texto=("El vino es, exclusivamente, la bebida resultante de la fermentación alcohólica, completa o parcial"
	" de uvas frescas, estrujadas o no, o de mosto de uva. Su contenido en alcohol adquirido no puede ser inferior a 8,5% vol."
    "¿Qué beneficios tiene el vino?."
	"  El vino tinto, con moderación, se ha considerado saludable para el corazón durante mucho tiempo."
	"El alcohol y ciertas sustancias en el vino tinto llamadas antioxidantes pueden ayudar" 
	"a prevenir la enfermedad de las arterias coronarias, la afección que provoca los ataques cardíacos.")

root.title("El Vino")

root.config(bg="lightblue",bd=30,height=400)
root.resizable(True,True)
root.geometry("800x250+400+100")

Imagen=tk.PhotoImage(file="vino.gif")
Imagen=Imagen.subsample(2)

etiq1= tk.Label(root,text="Definicion",fg="white",bg="Blue",width=150, height=2).pack(side="top",fill=tk.X)

etiq2= tk.Label(root,text=texto,bg="lightblue",wraplength=570,justify="left",font=fuente,height=9).pack(side="left",fill=tk.Y)

etiq3=tk.Label(root,image=Imagen,bg="black",compound="right",width=135,height=140).pack(side="right",fill=tk.X,expand=True)

root.mainloop()
'''
#######################################################################
'''
import tkinter as tk

root=tk.Tk()

root.title("Destinos")

destino1="  Masa de agua salada que cubre la mayor parte de la superficie terrestre..."
destino2="  Los bosques son ecosistemas imprescindibles para la vida,formados predominantemente por árboles"
destino3="  La nieve son pequeños cristales de hielo, que se forman por congelación del agua en la tropósfera"
fuente=("New Time Roman",12,"roman")

imagenMar=tk.PhotoImage(file="mar.gif")
imagenMar=imagenMar.subsample(2)
imagenNieve=tk.PhotoImage(file="nieve.gif")
imagenNieve=imagenNieve.subsample(2)
imagenBosque=tk.PhotoImage(file="bosque3.gif")
imagenBosque=imagenBosque.subsample(2)


root.config(bg="violet",width=700,height=370,relief="raised")
root.resizable(False,False)
#root.geometry("1000x800+350+100")
root.iconbitmap("mundo.ico")

etiq1=tk.Label(root,text=destino1,bg="black",fg="white",image=imagenMar,
	compound="left",font=fuente).place(x=20,y=30)

etiq2=tk.Label(root,text=destino2,bg="black",fg="white",image=imagenBosque,
	compound="left",font=fuente,width=660,wraplength=400,anchor=tk.W).place(x=20,y=140)

etiq3=tk.Label(root,text=destino3,bg="black",fg="white",image=imagenNieve,
	compound="left",font=fuente,width=660,wraplength=300,anchor=tk.W).place(x=20,y=240)

root.mainloop()
'''
################################################################################################

'''
import tkinter as tk

root=tk.Tk()
root.config(bg="violet")
etiq1=tk.Label(root,text="TABLERO DE AJEDREZ",
	bg="yellow",).grid(row=0,column=0,columnspan=50)
root.geometry("576x635+0+0")
root.resizable(False,False)


#tablero1=tk.Label(root,bg="black",bd=30).grid(row=7,column=7)
#tablero2=tk.Label(root,bg="white",bd=30).grid(row=4,column=4)

for fil in range(1,9):
	for fil2 in range(1,9):
		tk.Label(root,text="fil",relief="ridge",
			bd=30,bg="black",fg="cyan").grid(row=fil,column=fil2,
			sticky=tk.NSEW)
#		    if fil%2=0:
#				tk.Label(root,bg="white",bd=30).grid(row=4,column=4) 


#	for col in r
#		tk.Label(root,bg="white",bd=1).pack()
root.mainloop()
'''