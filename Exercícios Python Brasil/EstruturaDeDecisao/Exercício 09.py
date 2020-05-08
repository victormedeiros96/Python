n1 = float(input("Digite o número 1: "))
n2 = float(input("Digite o número 2: "))
n3 = float(input("Digite o número 3: "))
maior,meio,menor = 0,0,0
if n1>=n2:
	if n1>=n3:
		if n2>n3:
			menor,meio,maior = n3,n2,n1
		else:
			menor,meio,maior = n2,n3,n1
	else:
		menor,meio,maior = n2,n1,n3
else:
	if n3>=n1:
		if n2>n3:
			menor,meio,maior = n1,n3,n2
		else:
			menor,meio,maior = n1,n2,n3
	else:
		menor,meio,maior = n3,n1,n2
print(f"{menor} <= {meio} <= {maior}")
