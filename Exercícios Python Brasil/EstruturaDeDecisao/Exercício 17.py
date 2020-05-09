ano = int(input("Digite um ano: "))
if ano%4==0:
	if (ano%400) and not(ano%100):
		pass # NAO FAZ NADA POIS SERA IMPRESSO NO FINAL
	else:
		print("O ano é bissexto")
		exit() # SAIR POIS QUALQUER OUTRO CASO NAO E BISSEXTO
print("O ano não é bissexto")
