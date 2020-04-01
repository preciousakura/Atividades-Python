num = []
maior = 0;
menor = 0;

for x in range(0,5):
	num.append(int(input("Digite um número: ")))
	if x == 0:
		maior = menor = num[x]
		
	else:
		if num[x] > maior:
			maior = num[x]
		if num[x] < menor:
			menor = num[x]

			
	
print("+=" *30)	
print(f'Sua lista é {num}')
print(f'O maior número é {maior} e está nas posições', end='')

for i,v in enumerate(num):
	if v == maior:
		print(f" {i}...", end='')
		
print(' ')
	
print(f'O menor número é {menor} e está nas posições', end='')

for i,v in enumerate(num):
	if v == menor:
		print(f" {i}...", end='')
	


		

	
	