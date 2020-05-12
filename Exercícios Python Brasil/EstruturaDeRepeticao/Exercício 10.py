n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))
if n1<n2:
	for i in range(n1+1,n2):
		print(i)
else:
	for i in range(n2+1,n1):
		print(i)
