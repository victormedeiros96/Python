salario = float(input("Salario atual: "))
flag = ''
if salario<=280:
	reajuste = salario*1.20
	flag = 20
elif salario<=700:
	reajuste = salario*1.15
	flag = 15
elif salario<=1500:
	reajuste = salario*1.10
	flag = 10
elif salario>1500:
	reajuste = salario*1.05	
	flag = 5
print(f'''Salario antes do ajuste: R$ {salario:.2f}.
Aumento de {flag}% no valor de R$ {(reajuste-salario):.2f}.
Novo salário: R$ {reajuste:.2f}.''')
