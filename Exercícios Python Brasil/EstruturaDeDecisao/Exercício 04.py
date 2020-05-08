letra = input("Digite uma letrao: ")
letra = letra.lower()
# lista com as possíveis vogais
vogais = ["a","e","i","o","u"]
# utilizar a funcao "in" que verifica se um objeto se encontra dentro de outro, e retorna um booleano "verdadeiro" ou "falso".
e_vogal = letra in vogais # Valores possíveis: True, False
if e_vogal:
	print("A letra digitada é vogal")
else:
	print("A letra digitada é consoante")
