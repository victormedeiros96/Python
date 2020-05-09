valor_por_litro = {"A":1.90,"G":2.50} # PRECO POR LITRO [alcool,gasolina]
descontos = [{"A":0.03,"G":0.04},{"A":0.05,"G":0.06}]
combustivel = input("A para alcool, G para gasolina: ").upper()
litros = int(input("Quantos litros deseja: "))
if litros<20:
	desconto = descontos[0][combustivel]
else:
	desconto = descontos[1][combustivel]
valor = litros*valor_por_litro[combustivel]*(1-desconto)
print(f"Valor a pagar: R$ {valor:.2f}")
