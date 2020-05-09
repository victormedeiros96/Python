print('''                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Código de carnes: (1) Filé Duplo, (2) Alcatra, (3) Picanha''')
tabela_de_valores = [{1:4.9,2:5.9,3:6.9},{1:5.8,2:6.8,3:7.8}]
nome_carne = {1:'File Duplo',2:'Alcatra',3:'Picanha'}
carne = int(input("Escolha a carne que deseja, utilizando o código acima: "))
peso = float(input("Quantos kgs deseja? "))
tipo_pagamento = input("Dinheiro ou cartão? ").lower() # pegar letras minúsculas pra comparar melhor depois
if peso<5:
	aux = 0
else:
	aux = 1
valor = tabela_de_valores[aux][carne]*peso
if tipo_pagamento in ("cartão","cartao"): #verificar com acento e sem acento
	desconto = 0.5*valor # desconto de 5%
else:
	desconto = 0
print(f'{nome_carne[carne]}\tR${tabela_de_valores[aux][carne]:.2f}/kg\t{peso:.2f}kg')
print(f'Preço total: R${(tabela_de_valores[aux][carne]*peso):.2f}\nPagamento em {tipo_pagamento}.\nDesconto R${desconto:.2f}\nValor a pagar R${valor-desconto:.2f}')
