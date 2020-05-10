from random import randint as sorteio
def craps(vitoria):
	print('Natural. Parabéns. Venceu!!' if vitoria else 'Craps!! Perdeu')
def jogarDados():
	return sorteio(2,12)
def main():
	jogada = 1
	pontos = 0
	dados = jogarDados()
	# Primeira jogada
	if dados in (2,3,12):
		craps(0);return #perdeu
	elif dados in (7,11):
		craps(1);return #ganhou
	else:
		print(f'Ponto: {dados}')
		pontos = dados
		while True:
			jogada+=1 # inicia proxima jogada
			dados = jogarDados()
			print(dados)
			if dados == pontos:
				craps(1);return
			elif dados==7:
				craps(0);return
if __name__ == '__main__':
	main()
