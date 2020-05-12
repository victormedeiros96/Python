tabelaJuros = {1:0,3:10,6:15,9:20,12:25}
valor_divida = float(input('Valor da dívida: R$ '))
tabela = list()
for key in tabelaJuros:
	juro = valor_divida*tabelaJuros[key]/100
	tabela.append((juro,(valor_divida+juro)/key))
# Imprimir tabela
print(f'''
   Valor   \tValor   \tQuantidade   \t Valor
     da    \t dos     \t  de          \t da 
   Dívida  \tJuros    \tParcelas    \t Parcela
''')
for i in range(len(tabelaJuros)):
	print(f'R$ {tabela[i][0]+valor_divida:.2f} \t {tabela[i][0]:.2f}\t\t{tuple(tabelaJuros.keys())[i]:d}\t \t {tabela[i][1]:.2f}')
