print("Nome na vertical em escada invertida")
nome = input("Digite seu nome: ")
for i in range(len(nome)-1,-1,-1):
	print(nome[:i+1])
