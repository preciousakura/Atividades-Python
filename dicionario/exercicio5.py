pessoa = {}
grupo = []
stop = soma = femea = 0

while stop == 0:
	pessoa['Nome'] = str(input('Digite o nome da pessoa: '))
	pessoa['Sexo'] = str(input('Digite o sexo da pessoa [F/M]: ')).upper()[0]
	pessoa['Idade'] = int(input('Digite a idade da pessoa: '))
	grupo.append(pessoa.copy())
	keep = str(input("Deseja continuar? [S/N] "))
	if keep in "Nn":
		stop = 1
print(grupo)

print('-=' *40)
print(f'{len(grupo)} pessoas foram cadastradas.')

for i, v in enumerate(grupo):
	soma += v['Idade']
	
media = soma/len(grupo)
print(f'A média de idade do grupo é {media} anos.')

print(f'As mulheres do grupo são: ', end='')
for i, v in enumerate(grupo):
	if v['Sexo'] in "Ff":
		print(f'{v["Nome"]}, ', end='')

print()
print('PESSOAS COM IDADES ACIMA DA MÉDIA: ')
print()
for i in grupo:
	if i['Idade'] > media:
		for k, v in i.items():
			print(f'{k}: {v}')
		print()
