while True:
	A0 = input("População inicial A: ")
	B0 = input("População inicial B: ")
	dA = input("Taxa de crescimento de A (em Porcentagem): ")
	dB = input("Taxa de crescimento de B (em Porcentagem): ")
	try:
		A0 = float(A0)
		B0 = float(B0)
		dA = float(dA)/100
		dB = float(dB)/100
		t = (B0 - A0)/(dA-dB)
		print(f"Demorará {t} intervalos de tempo, para a população A chegar ao mesmo número de habitantes da população B")
		flag = input("Deseja repetir o exercício? (s para sim / n para não) ").lower()
		if flag=="s":
			continue
		else:
			break
	except:
		print("Erro, corrija os dados")



