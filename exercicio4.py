valores = []
stop = 0
while stop==0:
	valores.append(int(input("Digite um valor: ")))	
	
	
	keep = input("Quer continuar? (s/n) ")
	
	if keep == "n":
		stop = 1	

print("+=" *30)		
print(f"Há {len(valores)} elementos na sua lista...")
valores.sort(reverse=True)
print(f"Elementos ordenados de forma decrescente: {valores}")

if valores.count(5) > 0:
	print(f"O valor 5 está na sua lista e aparece {valores.count(5)} vezes")
else:
	print("Não há o valor 5 na sua lista")

