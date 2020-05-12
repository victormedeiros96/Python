# Gabarito da prova
gabarito = {
1:'a',
2:'b',
3:'c',
4:'d',
5:'e',
6:'a',
7:'b',
8:'e',
9:'d',
10:'c',
}
maiorNota = 0
menorNota = 10
contagem_de_alunos = 0
mediaNotas = 0
while True:
	flag = int(input('Realizar o teste? (1 para sim, 0 para não) '))
	if flag:
		aluno = 0
		contagem_de_alunos += 1
		for i in range(1,11):
			resposta = input(f'Questão {i}: ').lower()
			if resposta==gabarito[i]:
				aluno+=1
		if aluno<menorNota:
			menorNota = aluno
		if aluno>maiorNota:
			maiorNota = aluno
		mediaNotas+=aluno
	else:
		break
print(f'Média das notas: {mediaNotas/contagem_de_alunos:g}')
print(f'Menor nota: {menorNota:g}')
print(f'Maior nota: {maiorNota:g}')
print(f'Total de alunos: {contagem_de_alunos}')
