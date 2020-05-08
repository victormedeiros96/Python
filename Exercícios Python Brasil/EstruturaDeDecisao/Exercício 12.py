salario_por_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas = float(input("Quantas horas trabalhou no mês? "))
salario_bruto = salario_por_hora*horas_trabalhadas
flag_IR = 0
if salario_bruto<=900:
	flag_IR = 0
elif salario_bruto<=1500:
	flag_IR = 5
elif salario_bruto<=2500:
	flag_IR = 10
elif salario_bruto>2500:
	flag_IR = 20
sindicato = 0.03*salario_bruto
print(f'''
Salário Bruto: ({salario_por_hora:.2f} * {horas_trabalhadas:g}): R$ {salario_bruto:.2f}
(-) IR ({flag_IR}%)                     : R$ {salario_bruto*flag_IR/100:.2f}
(-) SINDICATO(3%)                      : R$ {salario_bruto*0.03:.2f}
FGTS (11%)                             : R$ {salario_bruto*0.11:.2f}
Total de descontos                     : R$ {(salario_bruto*(flag_IR+3)/100):.2f}
Salário Liquido                        : R$ {salario_bruto*(100-flag_IR-3)/100:.2f}
''')
