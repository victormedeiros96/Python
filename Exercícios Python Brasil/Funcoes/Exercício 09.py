def reverso(numero):
	return numero.__str__()[::-1]
def main():
	num = int(input('Digite um número: '))
	print(reverso(num))
if __name__ == '__main__':
	main()
