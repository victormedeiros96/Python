letra = input("Digite F para feminino ou M para masculino: ")
letra = letra.lower()
if letra=="f":
	sexo = "feminino"
elif letra=="m":
	sexo = "masculino"
else:
	sexo = "inválido"
print(f"Sexo {sexo}.")
