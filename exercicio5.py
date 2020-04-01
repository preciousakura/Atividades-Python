valores = []
pares=[]
impares=[]
stop = 0

while stop == 0:
	n = int(input("Digite um número: "))
	valores.append(n)

	
	if n % 2 == 0:
		pares.append(n)
	else:
		impares.append(n)
		
	keep = input("você quer continuar? (s/n) ")
	
	if keep == "n":
		stop = 1
		
print("+=" *30)
print(f"Sua lista completa {valores}")
print(f"Sua lista com número pares {pares}")
print(f"Sua lista com número ímpares {impares}")