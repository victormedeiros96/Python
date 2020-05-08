nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
media = (nota1+nota2)/2
if media==10: # para realizar a operação booleana de and (verificar se sao iguais) usa-se ==, pois um = apenas, significa atribuição de valor.
	print("Aprovado com distinção")# se a média for maior ou igual a sete (para menor ou igual a ordem é a mesma <=)
elif media>=7:# se a média for maior ou igual a sete (para menor ou igual a ordem é a mesma <=)
	print("Aprovado")
else:
	print("Reprovado")
