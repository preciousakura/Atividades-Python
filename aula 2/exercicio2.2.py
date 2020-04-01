numeros = []
pares = []
impar = []

for x in range(0,7):
	n = int(input('Digite um valor: '))
	if n % 2 == 0:
		pares.append(n)
		
	else:
		impar.append(n)
		
		
numeros.append(pares[:])
numeros[0].sort()
numeros.append(impar[:])
numeros[1].sort()
print('+=' *30)
print(f'Sua lista é {numeros}')
print(f'Números pares: {numeros[0]}')
print(f'Números ímpares: {numeros[1]}')