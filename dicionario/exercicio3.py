from datetime import date
pessoa = {}
pessoa['nome'] = str(input("Digite o nome: "))
dataN = int(input('Digite a data de nascimento: '))
data_atual = date.today()
ano = data_atual.year
pessoa['idade'] = ano - dataN
ctps = int(input('Carteira de Trabalho (0 não tem): '))

if ctps != 0:
	pessoa['ctps'] =  ctps
	anoContr = int(input("Digite o ano de contratação: "))
	pessoa['salario'] = int(input("Digite o salário: R$ "))
	pessoa['contratação'] = anoContr
	pessoa['aposentadoria'] = pessoa['idade'] + (35-(ano - anoContr))

	
for k,v in pessoa.items():
	print(f'{k}: {v}')