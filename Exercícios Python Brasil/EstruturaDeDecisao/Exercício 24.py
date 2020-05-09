n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))
op = input("Entre com o símbolo da operação desejada: ") # *,/,+,-
resultado = eval(f"{n1}{op}{n2}") # a função eval roda a string de parâmetro como um comando (evaluate)
par = "Par" if not(resultado%2) else "Impar"
positivo = "Positivo" if (resultado>=0) else "Negativo"
inteiro = "Inteiro" if (resultado == int(resultado)) else "Decimal"
print(f"O resultado é {resultado}. {par}. {positivo}. {inteiro}.")
