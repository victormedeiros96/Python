def valorPagamento(valor,dias_de_atraso):
	if dias_de_atraso:
		return valor*(1+dias_de_atraso*0.01+0.03)
	else:
		return valor
def main():
	novo_valor = list() # criar uma lista para armazenar os valores pagos no dia
	while True:
		valor = float(input('Valor da prestação: '))
		if not valor: # Se o valor indicado for zero, encerra o dia e mostra o relatório
			print(f'Foram pagas {len(novo_valor)} contas nos valores de:')
			for i in novo_valor:
				print(f'R$ {i:.2f}')
			return
		dias_de_atraso = int(input('Dias em atraso: '))
		novo_valor.append(valorPagamento(valor,dias_de_atraso)) # calcula o valor do pagamento, e adiciona ao final da lista com o método append
if __name__ == '__main__':
	main()
