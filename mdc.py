max = 0
x = 2
maiorM = 1
maiorD = 1
mmc=[]
mdc = []
valores = int(input("Número de casos: "))
p1 = int(input("quantas cartas p1: "))
p2 = int(input("quantas cartas p2: "))


if p1 > p2:
	max = p1
	
else:
	max = p2
	
while x!=max+1:
	while p1%x==0 or p2%x==0:
		if p1%x==0 and p2%x==0:
			print(f'{p1:.0f},{p2:.0f}:{x}')
			mmc.append(x)
			mdc.append(x)
			p1 = p1/x
			p2 = p2/x
		elif p1%x==0:
			print(f'{p1:.0f},{p2:.0f}:{x}')
			p1 = p1/x
			mmc.append(x)
		elif p2%x==0:
			print(f'{p1:.0f},{p2:.0f}:{x}')
			p2 = p2/x
			mmc.append(x)
		
	x+=1
		

for z in mmc:
	maiorM = z * maiorM
for y in mdc:
	maiorD = y * maiorD
	
print(f'O maior múltiplo comum (MMC) é {maiorM}')
print(f'O máximo divisor comum (MDC) é {maiorD}')
	

