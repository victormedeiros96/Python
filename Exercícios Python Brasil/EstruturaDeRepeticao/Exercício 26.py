n = int(input('Quantos eleitores irão votar? '))
votos=[0,0,0] # Candidato 1, Candidato 2 e Candidato 3
for i in range(n):
	voto = int(input('Qual seu voto (1,2 ou 3): '))
	votos[voto-1]+=1
print(f'''Votação encerrada
Candidato 1: {votos[0]} votos
Candidato 2: {votos[1]} votos
Candidato 3: {votos[2]} votos
''')
