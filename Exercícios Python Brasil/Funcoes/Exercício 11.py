def conversor(d,m,a):
	meses = {1:'Janeiro',2:'Feveiro',3:'Março',4:'Abril',5:'Maio',6:'Junho',7:'Julho',8:'Agosto',9:'Setembro',10:'Outubro',11:'Novembro',12:'Dezembro'}
	return f'{d} de {meses[m]} de {a}'
def main():
	data = input('Data (formato dd/mm/aaaa): ')
	dia=int(data[:2]);mes=int(data[3:5]);ano=int(data[6:])
	print(conversor(dia,mes,ano))
if __name__ == '__main__':
	main()
