def quantidade(numero):
	return len(numero.__str__())
def main():
	num = int(input('Digite um número: '))
	print(quantidade(num))
if __name__ == '__main__':
	main()
