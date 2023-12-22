 
# simulacion de cajero electronico

saldo = 1000

print(" .:MENU:. ")
print("1.ingresar dinero en la cuenta")
print("2.retirar dinero de la cuenta")
print("3.mostrar dinero disponible")
print("4. salir")

opcion = int(input("digite su opcion: "))

print()

if opcion==1:
    n1 = float(input("cuanto dinero desea ingresar: -> "))
    saldo = saldo + n1
    print(f"su dinero disponiible es de {saldo} pesos")

elif opcion==2:
    n2 = float(input("cuanto dinero desea retirar: -> "))
    if n2>saldo:
        print("no tienes esa cantidad de dinero")
    else:
        saldo = saldo - n2
        print(f"su dinero disponiible es de {saldo}")
elif opcion==3:
    print(f"su dinero disponnible es de: {saldo}")

elif opcion==4:
    print("gracias por utilizar su cajero automatico")

else:
    print("opcion incorrecta")
    
    
        
    
    
