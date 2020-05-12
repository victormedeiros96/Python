n = int(input("Termo: "))
fibonacci = [1,1]
for i in range(n-2):
	fibonacci.append(sum(fibonacci[-2:]))
for numero in fibonacci:
	print(numero)
