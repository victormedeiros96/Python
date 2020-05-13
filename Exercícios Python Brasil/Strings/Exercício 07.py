import re
print("Conta espaços e vogais.")
frase = input("Frase: ")
conta_espacos = len([m.start() for m in re.finditer(' ', frase)])
contagem = 0
for vogal in ["a","e","i","o","u"]:
	contagem+=len([m.start() for m in re.finditer(vogal, frase)])
print(f"Tem {conta_espacos} espaços.")
print(f"Tem {contagem} vogais")
