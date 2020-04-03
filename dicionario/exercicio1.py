aluno = {}

aluno['nome'] = str(input('Qual nome do aluno? '))
aluno['media'] = float(input('Qual a média do aluno? '))
if aluno['media'] >= 0 and aluno['media'] < 6:
	aluno['situacao'] = 'reprovado'
elif aluno['media'] >= 6 and aluno['media'] <=10:
	aluno['situacao'] = 'Aprovado'
else:
	print('Nota Inválida!')
	
for k, v in aluno.items():
	print(f'{k} é igual a {v}')