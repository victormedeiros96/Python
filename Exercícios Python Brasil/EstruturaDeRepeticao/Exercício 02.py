# Para esse exercício vamos utilizar o módulo getpass, para a senha não aparecer
from getpass import getpass
while True:
	user_name = input("Nome de usuário: ")
	print('Senha:',end=' ')
	password = getpass()
	if user_name==password:
		print('Erro, nome de usuário e senha não podem ser iguais')
	else:
		exit()
