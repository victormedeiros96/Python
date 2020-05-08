# ESTRUTURA DE DECISAO IF (SE) UTILIZA A SEGUINTE SINTAXE
# IF CONDICAO:
#     FAZ ALGO
# ELSE:
#     FAZ OUTRA COISA
# ONDE A CONDICAO É UM VALOR BOOLEANO, VERDADEIRO OU FALSO (True False)
numero_1 = float(input("Digite um número: "))
numero_2 = float(input("Digite outro número: "))
if numero_1>numero_2:
	print(f"O maior é o número 1 {numero_1}.")
elif numero_1<numero_2:
	print(f"O maior é o número 2 {numero_2}.")
else:
	print(f"Os números são iguais. {numero_1}")
