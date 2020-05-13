print("Palíndromo.")
texto = input("Digite uma sequência palíndroma: ").lower()
texto = texto.replace(" ","")
if texto==texto[::-1]:
	print("Palíndromo")
else:
	print("Não é palíndromo")
