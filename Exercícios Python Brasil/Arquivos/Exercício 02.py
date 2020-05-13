#print(f"{nome:15s}.")
def organizar_usuarios(lista):
	lista2=list()
	for usuario in lista:
		aux = usuario.split(" ")
		dados = aux[-1]
		nome = " ".join(aux[:-1])
		lista2.append([nome,round(int(dados)/1024/1024,2)])
	return lista2
with open("usuarios.txt", "r") as obj:
	arquivo = obj.read()
	arquivo = arquivo.split("\n")[:-1]
arquivo = organizar_usuarios(arquivo)

espaco_total = 0
for usuario in arquivo:
	espaco_total+=usuario[1]
espaco_total = espaco_total
espaco_medio = espaco_total/len(arquivo)

# converter dados para string
for i in range(len(arquivo)):
	arquivo[i].append(arquivo[i][1]/espaco_total*100)
	inteiro = int(arquivo[i][1])
	decimal = int(100*(arquivo[i][1]-inteiro))
	if decimal<10:
		decimal = f"0{decimal}"
	auxiliar = f"{inteiro},{decimal}"
	arquivo[i][1] = auxiliar
	

relatorio = f"""ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso
"""
cont = 1
for usuario in arquivo:
	relatorio+=f"\n{cont:<3d}  {usuario[0]:20s}{usuario[1]:>7s} MB        {usuario[2]:>2.2f}%"
	cont+=1
relatorio+=f"\nEspaço total ocupado: {espaco_total:.2f} MB"
relatorio+=f"\nEspaço médio ocupado: {espaco_medio:.2f} MB"
with open("relatorio.txt","w") as obj:
	obj.write(relatorio)
