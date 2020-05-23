from cliente import Cliente
from destino import Destino
from contas import Conta
from conectarAoBancoDeDados import ConectarBandoDeDados
from PyQt5.QtWidgets import QWidget,QApplication,QHBoxLayout,QVBoxLayout,QGroupBox,QLabel,QLineEdit,QSlider,QPushButton,QCheckBox,QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
class Main(QWidget):
	def __init__(self):
		super().__init__()
		self.comprovanteFlag = False
		self.initUI()
		self.show()
	def initUI(self):
		self.layout = QHBoxLayout()
		self.setLayout(self.layout)
		self.formulario_Cliente()
		self.formulario_Deposito()
		self.formulario_Saque()
	def formulario_Cliente(self):
		self.grupoFormulario = QGroupBox("Formulario Novo Cliente")
		self.layout.addWidget(self.grupoFormulario)
		layoutFormulario = QVBoxLayout()
		self.grupoFormulario.setLayout(layoutFormulario)
		###############################################
		layoutFormulario.addWidget(QLabel("Nome do Titular"))
		self.nome_Titular = QLineEdit("Fulano Da Silva Sauro")
		layoutFormulario.addWidget( self.nome_Titular )
		layoutFormulario.addWidget(QLabel("CPF do Titular"))
		self.cpf_Titular = QLineEdit("111.111.111-11")
		layoutFormulario.addWidget( self.cpf_Titular )
		layoutFormulario.addWidget(QLabel("RG do Titular"))
		self.rg_Titular = QLineEdit("11111111111")
		layoutFormulario.addWidget( self.rg_Titular )
		layoutFormulario.addWidget(QLabel("Agencia (Numero da agencia)"))
		self.agencia = QLineEdit("0455")
		layoutFormulario.addWidget( self.agencia )
		layoutFormulario.addWidget(QLabel("Senha"))
		self.senha_Form1 = QLineEdit("")
		self.senha_Form1.setEchoMode(QLineEdit.Password)
		layoutFormulario.addWidget(self.senha_Form1)
		self.botao_Comprovante = QCheckBox("Comprovantes entregues")
		self.botao_Comprovante.stateChanged.connect(self.changeState)
		layoutFormulario.addWidget( self.botao_Comprovante )
		self.botao_Cadastrar_Conta = QPushButton("Submeter")
		layoutFormulario.addWidget( self.botao_Cadastrar_Conta )
		self.botao_Cadastrar_Conta.clicked.connect(self.criar_Conta)
	def formulario_Saque(self):
		self.grupoSaque = QGroupBox("Saque")
		self.layout.addWidget(self.grupoSaque)
		layoutGrupo = QVBoxLayout()
		self.grupoSaque.setLayout(layoutGrupo)
		###############################################
		layoutGrupo.addWidget(QLabel("Agencia"))
		self.saque_Agencia = QLineEdit("")
		layoutGrupo.addWidget(self.saque_Agencia)
		layoutGrupo.addWidget(QLabel("Conta"))
		self.saque_Conta = QLineEdit("")
		layoutGrupo.addWidget(self.saque_Conta)
		layoutGrupo.addWidget(QLabel("Valor"))
		self.saque_Valor = QLineEdit("")
		layoutGrupo.addWidget(self.saque_Valor)
		layoutGrupo.addWidget(QLabel("Senha"))
		self.saque_Senha = QLineEdit("")
		self.saque_Senha.setEchoMode(QLineEdit.Password)
		layoutGrupo.addWidget(self.saque_Senha)
		botao_sacar = QPushButton("Sacar")
		botao_sacar.clicked.connect(self.sacar)
		layoutGrupo.addWidget(botao_sacar)
	def formulario_Deposito(self):
		self.grupoDeposito = QGroupBox("Deposito Bancario")
		self.layout.addWidget(self.grupoDeposito)
		layoutGrupo = QVBoxLayout()
		self.grupoDeposito.setLayout(layoutGrupo)
		###############################################
		layoutGrupo.addWidget(QLabel("Agencia"))
		self.deposito_Agencia = QLineEdit("")
		layoutGrupo.addWidget(self.deposito_Agencia)
		layoutGrupo.addWidget(QLabel("Conta"))
		self.deposito_Conta = QLineEdit("")
		layoutGrupo.addWidget(self.deposito_Conta)
		layoutGrupo.addWidget(QLabel("Nome do titular da conta destino"))
		self.deposito_Nome = QLineEdit("")
		layoutGrupo.addWidget(self.deposito_Nome)
		layoutGrupo.addWidget(QLabel("CPF do titular da conta destino"))
		self.deposito_Cpf = QLineEdit("")
		layoutGrupo.addWidget(self.deposito_Cpf)
		layoutGrupo.addWidget(QLabel("Valor (R$)"))
		self.deposito_Valor = QLineEdit("")
		layoutGrupo.addWidget(self.deposito_Valor)
		botao_depositar = QPushButton("Depositar")
		botao_depositar.clicked.connect(self.depositar)
		layoutGrupo.addWidget(botao_depositar)
	def sacar(self):
		try:
			numero_conta = self.saque_Conta.text()
			numero_agencia = self.saque_Agencia.text()
			senha = self.saque_Senha.text()
		except:
			pass
		try:
			valor = float(self.saque_Valor.text())
		except:
			QMessageBox.warning(self,"Erro","Valor para saque nao pode ser convertido em numeral.")
			return
		try:
			dados = ConectarBandoDeDados.auxiliar_Saque(numero_agencia,numero_conta,senha)
		except Exception as e:
			QMessageBox.warning(
                self, "Erro",
                f"{e}\n"
                "Por favor, verifique."
            )
		# Recriar o objeto de conta
		titular = Cliente(dados[0],dados[1],dados[2],True)
		conta = Conta(titular,dados[3],dados[6],dados[4],dados[5])
		print(conta)
		sacou = conta.sacar(valor)
		if (sacou):
			QMessageBox.information(self, "Saque realizado","Saque realizado com sucesso.")
		else:
			QMessageBox.information(self, "Saque nao pode ser realizado","Saldo insuficiente.")
	def depositar(self):
		try:
			print("Deu")
			agencia = self.deposito_Agencia.text()
			conta = self.deposito_Conta.text()
			nome = self.deposito_Nome.text()
			primeiro_nome = nome.split(" ")[0]
			cpf = self.deposito_Cpf.text()
			try:
				valor = float(self.deposito_Valor.text())
			except:
				QMessageBox.warning(self,"Erro","Valor para deposito nao pode ser convertido em numeral.")
				return
			contaDeposito = ConectarBandoDeDados.pesquisar(conta)
			for conta_encontrada in contaDeposito:
				print("Entrou Aqui no for")
				if agencia==conta_encontrada[3]:
					if primeiro_nome==(conta_encontrada[0].split(" ")[0]):
						if cpf==conta_encontrada[2]:
							titular = Cliente(conta_encontrada[0],conta_encontrada[1],conta_encontrada[2],True)
							conta = Conta(titular,conta_encontrada[3],conta_encontrada[6],conta_encontrada[4],conta_encontrada[5])
							flag = conta.depositar(float(valor))
							if flag:
								QMessageBox.information(self, "Deposito realizado","Deposito realizado com sucesso.")
							ConectarBandoDeDados.ler_tabela()
							break
		except Exception as e:
			QMessageBox.warning(
                self, "Erro",
                f"{e}\n"
                "Por favor, verifique."
            )
	def changeState(self,state):
		if state==Qt.Checked:
			self.comprovanteFlag = True
		else:
			self.comprovanteFlag = False
	def criar_Conta(self):
		if self.comprovanteFlag:
			try:
				nome = self.nome_Titular.text()
				cpf = self.cpf_Titular.text()
				rg = self.rg_Titular.text()
				agencia = self.agencia.text()
				senha = self.senha_Form1.text()
				comprovante = True
				cliente = Cliente(nome,rg,cpf,comprovante)
				conta1 = Conta(cliente,agencia,senha)
				print(conta1)
			except Exception as e:
				print(e)
		else:
			QMessageBox.warning(
                self, "Corrija o cadastro",
                "Necessita de comprovante de renda e residencia.\n"
                "Por favor, conclua o cadastro apos receber os comprovantes e tente novamente."
            )
			print("Comprovante nao entregue")
def main():
	app = QApplication([])
	a = Main()
	sys.exit(app.exec_())
	# cliente1 = Cliente("Victor Israel ANchieta de Medeiros",
	# "123456789",
	# "03050539062",
	# True)
	# conta1 = Conta(cliente1,"0455") #Agencia Caixa Economica Federal - Alegrete (RS)
if __name__ == "__main__":
	main()
