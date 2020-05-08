numero_1 = input("Digite um número: ") # O valor retornado é do tipo String
numero_2 = input("Digite outro número: ")
# Para corrigir vamos converter para ponto flutuante
numero_1,numero_2 = float(numero_1),float(numero_2)
print(f"A soma dos números é {numero_1+numero_2} .")
