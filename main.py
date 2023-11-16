def isMutant(matriz: list) -> bool:
	contador = 0
	letras = ["T"*4,"A"*4,"G"*4,"C"*4]
	columnas = [ "".join([x[y] for x in matriz]) for y in range(len(matriz[0]))]
	diagonales = [["".join([matriz[y+i][x+i] for i in range(4)]) for x in range(3)] for y in range(3)]
	#Intento fallido de diagonal inversa:
    #diagonalSecundaria = [["".join([matriz[y+i][x-1] for i in len(matriz)]) for x in range(3)] for y in range(3)]
	ant=len(letras)
	for i in range(3):
		for col in columnas:
			if(col[0+i:4+i] in letras):
				contador+=1

	for i in range(3):
		for row in matriz:
			if(row[0+i:4+i] in letras):
				contador+=1

	for x in diagonales:
		for j in x:
			if(j in letras):
				contador+=1
	if(contador >= 2):
		return True
	else:
		return False


if __name__ == "__main__": 
    
	adn_mutante = []
	cadenaactual = 1
	
	print("Ingrese 6 cadenas de ADN (6 caracteres cada una)")
	while True:
		if len(adn_mutante) == 6:
			break
		print("ingrese la cadena numero", cadenaactual)
		cadena = input().upper()
		if (len(cadena) != 6): #Intente hacer que reconociera numeros y los negara, pero no pude
			print("cadena de adn invalida, ingresela de nuevo")
			continue
		cadenaactual += 1
		adn_mutante.append(cadena)
	print("--------------------------")
	for i in adn_mutante:
		for j in i:
			print(j,end=" ")
		print("")
	print("--------------------------")
	if(isMutant(adn_mutante) == True):
		print("el paciente es un mutante (Hay 2 o mas iteraciones de 4 caracteres consecutivos de alguna/s de las siguientes letras \n 'T,A,G,C')")
	else:
		print("el paciente no es un mutante (Para que lo sea debe poseer 2 o mas iteraciones de 4 caracteres consecutivos \n de alguna/s de las siguientes letras \n 'T,A,G,C')")
	print("--------------------------")	
	