numeros = [6,5,2,4,7,1,8,9,3]
soma = 0
menor = 0
maior = 0
for i in numeros:
	soma+=i
	if menor>i:
		menor = i
	if maior<i:
		maior = i
print(menor)
print(maior)
print(soma)
