valores = []
stop = 0
while stop==0:
	valores.append(int(input("Digite um valor: ")))			
	if valores.count(valores[len(valores)-1]) == 2:
		valores.pop()
		print("O Elemento não foi adicionado...")	
	else:
		print("O Elemento foi adicionado...")					
	keep = input("Quer continuar? (s/n) ")
	
	if keep == "n":
		stop = 1	
print("+=" *30)
valores.sort()
print("Você digitou os valores ",valores)

		

	

			
