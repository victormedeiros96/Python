fibonacci = [1,1]
while fibonacci[-1]<500:
	fibonacci.append(sum(fibonacci[-2:]))
for numero in fibonacci[:-1]: # Tirei o último pois pelo que entendi não era para ser incluído
	print(numero)
