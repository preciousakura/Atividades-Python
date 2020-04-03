jogador = {}
jogador['nome'] = str(input('Digite o nome do jogador: '))
jogos = int(input("Total de jogos do jogador: "))
gols = []
total = 0

for x in range(jogos):
	gol = int(input(f"Quantos gols o jogador {jogador['nome']} fez no jogo {x+1}? "))
	gols.append(gol)
	total += gol
	
jogador['gols'] = gols
jogador['total'] = total
print('=-'*30)
for k,v in jogador.items():
	print(f'{k}: {v}')
print('=-'*30)
print(f'O jogador {jogador["nome"]} jogou {jogos} jogos.')
for i, v in enumerate(gols):
	print(f'{"=>":>5} Na partida {i+1}, fez {v} gols.')
print(f'Fez um total de {jogador["total"]} gols.')