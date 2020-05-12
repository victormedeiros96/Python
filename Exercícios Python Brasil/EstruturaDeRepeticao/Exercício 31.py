contador=1
preco_total=0
print('Lojas Tabajara')
while True:
	aux = float(input(f'Produto {contador}: R$ '))
	if not aux:
		break
	else:
		preco_total+=aux
		contador+=1
print(f'Total: R$ {preco_total:.2f}')
dinheiro = float(input(f'Dinheiro: R$ '))
print(f'Troco: R$ {dinheiro-preco_total:.2f}')
