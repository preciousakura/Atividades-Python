pessoas = []
dados = []
stop = 0
mai = men = 0

while stop == 0:
	dados.append(input('Digite o nome: '))
	dados.append(int(input('Digite o peso: ')))
	pessoas.append(dados[:])
	dados.clear()

	keep = input('Quer continuar?[S/N]')
	if keep == "n":
		stop = 1
		

for i,v in enumerate(pessoas):
	if i == 0:
		mai = men = pessoas[0][1]
	else:
		if pessoas[i][1] > mai:
			mai = pessoas[i][1]
		if pessoas[i][1] < men:
			men = pessoas[i][1]
	
		
		
print('=+' * 30)		
print(f'Você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {mai}kg. Esse é o peso de: ', end = '')

for i,v in enumerate(pessoas):
	if pessoas[i][1] == mai:
		print(f"{pessoas[i][0]} ", end='')
print('')
print(f'O menor peso foi de {men}kg. Esse é o peso de: ', end = '')
for i,v in enumerate(pessoas):
	if pessoas[i][1] == men:
		print(f"{pessoas[i][0]}, ", end='')

		