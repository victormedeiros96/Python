data = str(int(input("Digite um número inteiro entre 0 e 999: "))) # Converter para inteiro para garantir que não há zeros na frente
tamanho=len(data) # e converter para string para obter o tamanho e após as posições
# Verificando se o valor está dentro do exigido
if int(data) not in range(1000):
	print("Valor incorreto")
if tamanho == 1: #Se o número tem um caracter
	print(f"{int(data)} unidades.")
elif tamanho == 2: #Se o número tem dois caracteres
	print(f"{int(data[0])} dezenas e {int(data[1])} unidades.")
else:
	print(f"{int(data[0])} centenas, {int(data[1])} dezenas e {int(data[2])} unidades.")
