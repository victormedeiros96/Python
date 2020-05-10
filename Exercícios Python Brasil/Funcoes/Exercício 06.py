def conversor(hora,minuto):
	if hora in range (13,24):
		x = 'PM'
		hora -= 12
	elif hora == 12:
		x = 'PM'
	elif hora == 0:
		hora = 12
		x = 'AM'
	else:
		x = 'AM'
	return hora,minuto,x
def main():
	hora = int(input('Hora: '))
	minuto = int(input('Minuto: '))
	print(conversor(hora,minuto))
if __name__ == '__main__':
	main()
