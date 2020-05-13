print("Nome na vertical em escada")
nome = input("Digite seu nome: ")
for i in range(len(nome)):
	print(nome[:i+1])
