from random import randint
from operator import itemgetter

jogo = {
'jogador1': randint(1, 6),
'jogador2': randint(1, 6),
'jogador3': randint(1, 6),
'jogador4': randint(1, 6),
}
ordem = []

print("Valores sorteados: ")

for k, v in jogo.items():
	print(f'O {k} tirou {v}.')

ordem = sorted(jogo.items(), key=itemgetter(1), reverse = True)		
print("Ranking dos Jogadores: ")
for i, v in enumerate(ordem):
	print(f'{i+1}º Lugar: {v[0]} com {v[1]}')