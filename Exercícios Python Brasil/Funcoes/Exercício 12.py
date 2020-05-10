from random import randint
def embaralhador(texto):
	texto = list(texto)
	saida = ''
	tamanho = len(texto)
	for i in range(tamanho):
		letra = texto[randint(0,tamanho-i-1)]
		saida+=letra
		texto.remove(letra)
	return saida
def main():
	texto = input('Digite algo para embaralhar: ').upper()
	print(embaralhador(texto))
if __name__ == '__main__':
	main()
