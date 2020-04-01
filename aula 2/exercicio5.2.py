alunos = []
stop = para = 0


while stop == 0:
	nomeAluno = str(input("Digite o nome do aluno: "))
	nota1 = float(input("Digite a nota 1 do aluno: "))
	nota2 = float(input("Digite a nota 2 do aluno: "))
	media = (nota1 + nota2)/2
	alunos.append([nomeAluno, [nota1, nota2], media])


	keep = input("Quer continuar? [s/n] ")
	if keep == 'n':
		stop = 1

print(f'=-' *30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print(f'-' *40)

for i, v in enumerate(alunos):
	print(f'{i:<4}{v[0]:<10}{v[2]:>8.1f}')
	
	
while para != 999:

	numAluno = int(input("Mostrar notas de qual aluno? [PARAR: 999] "))
	if numAluno <= len(alunos)-1:
		print(f'As notas da {alunos[numAluno][0]} sao {alunos[numAluno][1]}')
			
	
	
	elif numAluno == 999:
		para = 999

	

	