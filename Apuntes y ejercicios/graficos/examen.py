import random
continuar=1

while continuar ==1:
	print("===---[ Bienvenido/a MasterMind ]===---")
	print("Elija la dificultad del juego <1=Facil, 2=Dificil, 3=Muy Dificil")
	Dificultad= int(input("Digite el nivel de dificultad: "))
#Asignamos cantidad de digitos para cada dificultad
	if Dificultad == 1:
		cant_digitos=3
	elif Dificultad ==2:
		cant_digitos=4
	elif Dificultad==3:
		cant_digitos=5

digitos = ('0','1','2','3','4','5','6','7','8','9') #Tupla para especificar los simbolos validos para el codigo

codigo= ''  #Variable para guardar el codigo

for i in range(cant_digitos):      # 
	elegido=random.choice(digitos) # Asignamos con choice lo q tenemos en nuestra tupla de manera aleatoria

	while elegido in codigo:    #mientras el numero elegido se encuentra en el codigo
		elgido=random.choice(digitos)

	codigo= codigo+elegido

print("Tienes q adivinar un codigo de ",cant_digitos, "digitos distintos")

propuesta= input("Q codigo propones:?")

intentos=1

while propuesta != codigo:
	intentos+=1
	aciertos=0
	coincidencias=0
	for i in range(cant_digitos):
		if propuesta[i] == codigo[i]:
			aciertos+=1

		elif propuesta[i] in codigo:
			coincidencias=coincidencias +1

		print("Tu propuesta(",propuesta,")tiene",aciertos,
			"aciertos y ",coincidencias," coincidencias")
		propuesta= input("Propon otro codigo: ")
Print("FELICIDADES! adivinaste el codigo en",intentos,"intentos")
continuar= int(input("Deseas seguir jugando? <1=Si, 0=No>: "))






