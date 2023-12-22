#estudiando POO
'''
class Coche():    #se define la clase
    largochasis=250  #se definen todos sus atributos
    anchochasis=50
    ruedas=4
    enmarcha=False

    def arrancar(self): #definiendo metodo
        self.enmarcha=True

    def estado(self):   # metodo
        if (self.enmarcha): # en marcha true
        
            return "el coche esta en marcha"

        else:

            return "el coche esta parado"


miCoche=Coche() # definiendo un objeto (instancia)

print("el largo del coche es: ",miCoche.largochasis) #muestro el objeto junto con un atributo

print("el coche tiene: ",miCoche.ruedas,"ruedas")   #muestro el objeto junto con un atributo

miCoche.arrancar() #poniendo en marcha mi objeto, tambien estoy llamando al metodo

print(miCoche.estado()) # muestro el estado de mi objeto junto a un metodo

print()
print("-----====SEGUNDO OBJETO====------")
print()

miCoche2=Coche() #creacion del objeto 2

print("el largo del coche es: ",miCoche2.largochasis)

print("el coche tiene: ",miCoche2.ruedas,"ruedas")

print(miCoche2.estado())

'''
#ENCAPSULAMIENTO y CONSTRUCTOR
'''
class Coche(): #ESTADO INICIAL: "CARACTERISTICAS DE FABRICAS"
    def __init__(self):# defino constructor (estado inicial de las cosas) con 2 guiones bajos
      self.largochasis=250                                             #
      self.anchochasis= 50                                             #
      self.__ruedas=4                #ENCAPSULANDO con 2 guiones bajos
      self.__enmarcha=False                                              #

    def arrancar(self,arrancamos): #ingreso otro parametro "arrancamos"

        self.__enmarcha=arrancamos   

        if (self.__enmarcha):
            
            return "el coche esta en marcha"

        else:
            return "el coche esta parado"


    def estado(self):
        print("el coche tiene " , self.__ruedas,"ruedas. un ancho de "
              ,self.anchochasis, "y u largo de: ",self.largochasis,"metros")
        


miCoche=Coche()

print(miCoche.arrancar(True)) #ingreso medoto con parametro
      
miCoche.estado()  

print()
print("-----====SEGUNDO OBJETO====------")
print()


miCoche2=Coche()

print(miCoche2.arrancar(False)) #ingreso medoto con parametro

miCoche2.ruedas=2 # modificando una propiedad


miCoche2.estado()  
'''

#AGREGAMOS UN METODO(Chequeo), se encapsula y se lo llama en el metodo arrancar
'''
class Coche(): 
    
    def __init__(self):
                       
      self.largochasis=250                                             
      self.anchochasis= 50                                             
      self.__ruedas=4                
      self.__enmarcha=False                                              

    def arrancar(self,arrancamos): 

        self.__enmarcha=arrancamos

        if(self.__enmarcha):   
            chequeo1=self.__Chequeo() #comprobamos el estado del coche
            
        if(self.__enmarcha and chequeo1): #preguntamos
            return "el coche esta en marcha"
        
        elif(self.__enmarcha and chequeo1==False):
            
            return "algo a ido mal en el chequeo"
        
        else:
            return "el coche esta parado"


    def estado(self):
        print("el coche tiene " , self.__ruedas,"ruedas. un ancho de "
              ,self.anchochasis, "y u largo de: ",self.largochasis,"metros")

    def __Chequeo(self):   #agregamos metodo
        print("Realizando chequeo interno")

        self.gasolina= "ok"
        self.aceite= "ok"
        self.puertas= "cerradas"

        if (self.gasolina== "ok" and self.aceite== "ok" and self.puertas== "carradas"):
            
            return True
        else:
            return False
        

        
        


miCoche=Coche()

print(miCoche.arrancar(True)) 
      
miCoche.estado()



print()
print("-----====SEGUNDO OBJETO====------")
print()


miCoche2=Coche()

print(miCoche2.arrancar(False)) 


miCoche2.estado()
'''
# HERENCIA I , II y III

'''
class Vehiculos():    #clase padre

    def __init__(self,marca,modelo):  #constrictor

        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):

        self.enmarcha=True

    def acelerar(self):

        self.acelera=True

    def frena(self):

        self.frena=True

    def estado(self):

        print("marca;", self.marca,"\nModelo:", self.modelo,"\nEn Marcha", self.enmarcha,
              "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)


class Furgoneta(Vehiculos):
    
    def Carga(self,cargar):
        self.cargado=cargar
        if(self.cargado):
            return "la furgoneta esta cargada"
        else:
            return "la furgoneta no esta cargada"


class Moto(Vehiculos): #Heredamos dentro del parentesis    
    Hcaballito=""
    def caballito(self):
        self.hcaballito="voy haciendo el caballito"
    def estado(self):

        print("marca;", self.marca,"\nModelo:", self.modelo,"\nEn Marcha", self.enmarcha, # Sobreesscribiendo el metodo estado de la clase padre
              "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.caballito)

class VElectricos():
    def __init__(self,marca, modelo):
        super().__init__(marca,modelo) 
        self.autonomia=100

    def cargarEnergia(self):
        self.cargando=True
        



    
miMoto=Moto("Honda", "Wave") #instancia con parametros entre parentesis

miMoto.caballito()

miMoto.estado() #LLAMANDO AL METODO

print("SEGUNDO OBJETO")

miFurgoneta=Furgoneta("BMW", "Urban")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.Carga(True))

class BicicletaElectrica(VElectricos,Vehiculos): #HERENCIA MULTIPLES ... se le da preferencia al constructor del primer parametro q se ingresa
    pass

miBici=BicicletaElectrica("ANDES", "r26")

'''


# principio de sustitucion: "es siempre un/a ", USO DE la funcion SUPER, uso de "ISINSTANCE"

'''
class Persona():
    def __init__(self,nombre,edad,lugar_residencia):
        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=lugar_residencia

    def descripcion(self):
        print("nombre:", self.nombre, "edad: ",self.edad, "residencia: ",self.lugar_residencia)

class Empleado(Persona):
    def __init__(self,salario,antiguedad,nombre_empleado,edad_empleado,residencia_empleado):
        super().__init__(nombre_empleado,edad_empleado,residencia_empleado)  # Super: estamos llamando al metodo INIT de la clase padre
        self.salario=salario
        self.antiguedad=antiguedad
    def descripcion(self):
        super().descripcion()  
        print("SALARIO: ",self.salario,"ANTIGUEDAD: ",self.antiguedad)

Manuel=Empleado(1500,15, "Manuel", 55,"Argentina")

Manuel.descripcion()

print(isinstance(Manuel,Persona)) # buscamos una instancia en un objeto

'''
        
    























