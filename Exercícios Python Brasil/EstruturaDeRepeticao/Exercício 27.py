alunos_totais = 0
num_turmas = int(input("Quantas turmas tem? "))
for i in range(num_turmas):
	alunos = int(input(f'Quantos alunos tem na turma {i+1}? '))
	if alunos<=40 and alunos>0:
		alunos_totais+=alunos
	else:
		print('Erro: Número de alunos deve estar entre 1 e 40')
		exit()
print(f"Media de alunos por turma: {alunos_totais/num_turmas}.")
