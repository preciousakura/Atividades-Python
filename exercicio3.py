num = []

for x in range(0,5):
	n = int(input("Digite um valor: "))
	
	if n not in num:
	
		if x == 0 or n > num[-1]:
			num.append(n)
			print("O elemento foi adicionado no final da lista")

			
		else:
			for i,v in enumerate(num):
				if n <= v:
					num.insert(i, n)
					print(f"O elemento foi adicionado na posição {i}")
					break
	else:
		print("Esse valor já existe na lista! Portanto, não foi adicionado.")
		
		
print("+=" *30)
print(f"Sua lista é {num}")

			
