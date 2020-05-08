from math import ceil
area_pintura = float(input("Tamanho da área a ser pintada (em metros quadrados): "))
litros = area_pintura/6
# 10% de folga
litros = 1.1*litros
latas = ceil(litros/18)
galoes = ceil(litros/3.6)
# mix[latas,galoes,custo]
mix = [0,0,0]
# CÁLCULO MISTURANDO LATAS E GALOES
if litros<=3.6:
	mix[1] = 1
elif litros<=18:
	mix[0] = 1
	mix[1] = 0
else:
	aux = litros/18
	mix[0] = int(aux)
	aux = aux*18
	mix[1] = ceil(aux/3.6)
mix[2] = mix[0]*80+mix[1]*25
print(f"Poderá comprar {latas} latas no valor de R$ {80*latas} .")
print(f"Poderá comprar {galoes} galões no valor de R$ {25*galoes} .")
print(f"Poderá comprar {mix[0]} latas e {mix[1]} galões no valor de R$ {mix[2]:.2f} .")
