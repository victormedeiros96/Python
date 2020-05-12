n = int(input(f'Fatorial de: '))
contador = 1
print(f'Fatorial de: {n}\n{n}! =',end='')
for i in range(n):
	print(f' {n-i} .',end='')
	contador*=n-i
	
print(f'\b= {contador:d}')
