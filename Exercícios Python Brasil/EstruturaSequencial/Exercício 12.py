peso = float(input("Peso dos peixes: "))
excesso = peso-50
multa = excesso*4
print(f'''
Peso: {peso:.1f}kg.
Excesso de Peso: {excesso:.1f}kg.
Multa: R${multa:.1f}.
''')
