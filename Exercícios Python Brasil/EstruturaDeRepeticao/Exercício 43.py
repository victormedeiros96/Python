tabelaPrecos = {
100:('Cachorro Quente',1.20),
101:('Bauru Simples',1.30),
102:('Bauru com ovo',1.50),
103:('Hambúrguer   ',1.20),
104:('Cheeseburguer',1.30),
105:('Refrigerante',1.00)
}
# Impressão do cardápio
print('Cardápio Lanchonete')
print('Código\tNome\t\t \tPreço')
for key in tabelaPrecos:
	print(f'{key} \t{tabelaPrecos[key][0]}    \tR$ {tabelaPrecos[key][1]:.2f}')
# Pedido
print('Entre com o código dos pedidos, e caso queira finalizar, digite \'parar\'')
pedidos = [0,0,0,0,0,0]
while True:
	flag = input('Pedido: ').lower()
	if flag=='parar':
		break
	else:
		flag = int(flag)
		quantidade = int(input('Quantidade: '))
		flag -= 100
		pedidos[flag] = quantidade
# Calcula custo
total = 0
for i in range(len(tabelaPrecos)):
	total += pedidos[i]*tabelaPrecos[100+i][1]
# Imprime pedido
print('\n\n'+'-'*20+'\nComanda de pedidos\n'+'-'*20,end='\n\n')
for i in range(len(tabelaPrecos)):
	if pedidos[i]:
		print(f'{tabelaPrecos[i+100][0]}     \t    {pedidos[i]}x{tabelaPrecos[i+100][1]:.2f} \t R$ {pedidos[i]*tabelaPrecos[i+100][1]:.2f}')
print(f'Total \t\t\t\t\t R$ {total:.2f}')
