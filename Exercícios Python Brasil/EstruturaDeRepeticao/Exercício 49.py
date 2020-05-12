soma = 0
termo = 0
n = int(input('Digite o termo N: '))
print('S = ',end='')
for i in range(1,n+1):
	print(f'{i}/{2*i-1} +',end='')
	soma += i/(2*i-1)
print('\b.')
print(f'Soma: {soma:g}')
