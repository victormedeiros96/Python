menor=1e5
maior=-1e5
soma =0
contador=0
print('Para parar de entrar novas temperaturas, digite \'parar\' ')
while True:
	n = input(f'Temperatura: ').lower()
	if n=="parar":
		break
	else:
		try:
			n = float(n)
			contador+=1
			soma+=n
			if menor>n:
				menor=n
			if maior<n:
				maior=n
		except:
			pass
media = soma/contador
print(f'Temperatura média: {media} ')
print(f'Maior temperatura: {maior} ')
print(f'Menor temperatura: {menor} ')
