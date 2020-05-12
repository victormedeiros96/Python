# Eleição
tipoDeVotos = {
0:'Sair',
1:'Candidato 1',
2:'Candidato 2',
3:'Candidato 3',
4:'Candidato 4',
5:'Nulo',
6:'Branco'
}
tabelaVotos = '\tNúmero\tCandidato\n'
for i in tipoDeVotos:
	tabelaVotos = tabelaVotos + f'\t{i}\t{tipoDeVotos[i]}\n'
	
# Contagem de votos
cont = [0,0,0,0,0,0] # candidato 1,candidato 2,candidato 3,candidato 4,nulo,branco
#
while True:
	print(tabelaVotos)
	x = int(input('Em quem deseja votar? '))
	if x:
		cont[x-1]+=1
	else:
		break
# Saída
print(f'Total de votos: {sum(cont)}')
for i in tuple(tipoDeVotos.keys())[1:]:
	print(f'Votos {tipoDeVotos[i]}: {cont[i-1]}')
print(f'Brancos {100*cont[-1]/sum(cont)}%')
print(f'Nulos {100*cont[-2]/sum(cont)}%')
