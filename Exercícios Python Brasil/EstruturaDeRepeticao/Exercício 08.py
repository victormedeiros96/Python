n = list()
for i in range(5):
	n.append(float(input("Numero: ")))
soma = 0
for i in range(5):
	soma+=n[i]
media = soma/5
print(f"A soma é {soma:g}, e a média é {media:g}.")
# # Extra
#
# print(f"A soma é {sum(n):g}, e a média é {sum(n)/5:g}.")
