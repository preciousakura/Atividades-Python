from random import randint
jogos = []
palpites = []
qts = int(input('Quantos jogos você quer fazer? '))
while qts!=0:
	random = randint(0,60)
	for x in range(0,6):
		if random not in palpites:
			palpites.append(random)
		else:
			while random in palpites:
				random = randint(0,60)
			palpites.append(random)
			
	jogos.append(palpites[:])
	palpites.clear()
			
	qts -= 1

print("------------------- SEUS JOGOS -------------------")
for x in range(0, len(jogos)):
	print(f"Jogo {x+1}: {jogos[x]}")
print("------------------- BOA SORTE --------------------")