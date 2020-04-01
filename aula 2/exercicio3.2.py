numeros = []
linha1 = []
linha2 = []
linha3 = []
soma = 0
somaTerceiraCol = 0
mai = 0

for x in range(0, 9):
	if x <= 2:
		linha1.append(int(input('Digite um valor: ')))
	elif x <=5:
		linha2.append(int(input('Digite um valor: ')))
	elif x <=8:
		linha3.append(int(input('Digite um valor: ')))
		
numeros.append(linha1[:])
numeros.append(linha2[:])
numeros.append(linha3[:])

for i,v in enumerate(numeros):
	for y,z in enumerate(linha1):
		if numeros[i][y] % 2 == 0:
			soma = soma + numeros[i][y]
		if y == 2:
			somaTerceiraCol = somaTerceiraCol + numeros[i][y]
		if i == 1:
			if y == 0:
				mai = numeros[i][y]
			else:
				if numeros[i][y] > mai:
					mai = numeros[i][y]

print('+=' *30)

print('Sua matriz')
for i,v in enumerate(numeros):
	for y,z in enumerate(linha1):
		print(f'{numeros[i][y]}  ', end = '')
	print("")
print(f'A soma dos números pares da matriz é {soma}.')
print(f'A soma dos números da terceira coluna da matriz é {somaTerceiraCol}.')
print(f'O maior valor da segunda linha da matriz é {mai}.')