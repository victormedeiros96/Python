from math import ceil # ARREDONDAR PARA CIMA
area_pintura = float(input("Tamanho da área a ser pintada (em metros quadrados): "))
litros = area_pintura/3
latas = ceil(litros/18)
print(f"Precisará comprar {latas} latas no valor de R$ {80*latas} .")
