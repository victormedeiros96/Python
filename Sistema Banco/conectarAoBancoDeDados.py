import sqlite3
class ConectarBandoDeDados:
	def __init__(self):
		self.__conn = 0
	def inserir(self,tupla):
		self.__conn = sqlite3.connect("ClientesDoBanco.db")
		cursor = self.__conn.cursor()
		sql_msg = """INSERT INTO CLIENTES ("Titular","RG","CPF","NumeroAgencia","NumeroConta","Saldo","Senha") VALUES (?,?,?,?,?,?,?);"""
		cursor.execute(sql_msg,tupla)
		self.__conn.commit()
		self.__conn.close()
	def atualizar_conta(self,cliente,saldo):
		print("Atualizando")
		conn = sqlite3.connect("ClientesDoBanco.db")
		cursor = conn.cursor()
		print(saldo,cliente)
		array = f'UPDATE CLIENTES SET Saldo = {saldo} WHERE NumeroConta = "{cliente}";'
		print(array)
		cursor.execute(array)
		conn.commit()
		conn.close()
	def ler_tabela():
		conn = sqlite3.connect("ClientesDoBanco.db")
		cursor = conn.cursor()
		cursor.execute("SELECT * from CLIENTES")
		retorno = cursor.fetchall()
		conn.close()
		print(retorno)
	def ler_Contas_Existentes(self):
		self.__conn = sqlite3.connect("ClientesDoBanco.db")
		cursor = self.__conn.cursor()
		cursor.execute("SELECT NumeroConta from CLIENTES")
		retorno = cursor.fetchall()
		self.__conn.close()
		return retorno
	@staticmethod
	def pesquisar(conta):
		conn = sqlite3.connect("ClientesDoBanco.db")
		cursor = conn.cursor()
		cursor.execute(f"SELECT * from CLIENTES WHERE NumeroConta = {conta}")
		retorno = cursor.fetchall()
		conn.close()
		return retorno
	@staticmethod
	def auxiliar_Saque(agencia,conta,senha):
		conn = sqlite3.connect("ClientesDoBanco.db")
		cursor = conn.cursor()
		cursor.execute(f"SELECT * from CLIENTES WHERE (NumeroAgencia,NumeroConta,Senha) = (\"{agencia}\",\"{conta}\",\"{senha}\")")
		retorno = cursor.fetchall()[0]
		conn.close()
		return retorno
