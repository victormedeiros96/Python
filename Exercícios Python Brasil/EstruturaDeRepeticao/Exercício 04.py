# Segundo a questão, o crescimento das populações é linear
# Dessa forma, pode-se encarar as curvas de crescimento como retas.
# Da equação da reta y(x) = ax+b, onde b é o estado inicial da função, e a é o coeficiente angular (ou taxa de variação)
# Logo podemos modelar nossos crescimentos do exercício assim:
# População(t) = taxa*t+PopulaçãoInicial
# O exercício pede que seja descoberto o tempo onde as populações se igualam, portanto é só igualarmos as populações
# P1= P2
# taxa1 * tempo + populacao_inicial_1 = taxa2 * tempo + populacao_inicial_2
# Isolando o tempo, temos:
# taxa1*tempo - taxa2*tempo = populacao_inicial_2-populacao_inicial_1
# tempo = (populacao_inicial_2-populacao_inicial_1)/(taxa1-taxa2)

A0 = 80e3 # habitantes
dA = 0.03 # taxa de crescimento
B0 = 200e3
dB = 0.015

t = (B0 - A0)/(dA-dB)

print(f"Demorará {t} intervalos de tempo, para a população A chegar ao mesmo número de habitantes da população B")
