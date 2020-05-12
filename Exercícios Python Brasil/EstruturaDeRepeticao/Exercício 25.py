n = int(input('Quantas idades deseja verificar? '))
somador_idades = 0
for i in range(n):
	somador_idades += int(input('Idade: '))
media = somador_idades/n
if media<25:
	x = 'Jovem'
elif media<60:
	x = 'Adulta'
else:
	x = 'Idosa'
print(f'População {x}')
