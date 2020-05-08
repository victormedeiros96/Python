salario_por_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas = float(input("Quantas horas trabalhou no mês? "))
salario_bruto = salario_por_hora*horas_trabalhadas
imposto_de_renda = 0.11*salario_bruto
inss = 0.08*salario_bruto
sindicato = 0.05*salario_bruto
salario_mensal = salario_bruto-imposto_de_renda-inss-sindicato
print(f"Salário bruto: R${(salario_bruto):.2f} .")
print(f"INSS: R${(inss):.2f} .")
print(f"Sindicato: R${(sindicato):.2f} .")
print(f"Salário líquido: R${(salario_mensal):.2f} .")
