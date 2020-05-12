minimo = float(input('Preço do pão: R$ '))
print('\tPanificadora Pão de Ontem - Tabela de preços')
for i in range(50):
	print(f'{i+1}\t-\tR$ {(minimo*(i+1)):.2f}')

