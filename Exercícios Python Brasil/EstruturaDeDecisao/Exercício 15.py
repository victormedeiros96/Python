lado1 = float(input("Lados do triângulo\nLado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))
# Para verificar se pode existir um triângulo, todos devem ser verdadeiros
# | b - c | < a < b + c 
# | a - c | < b < a + c 
# | a - b | < c < a + b 
flag1 = (abs(b-c)<a)and(a<(b+c))
flag2 = (abs(a-c)<b)and(b<(a+c))
flag3 = (abs(a-b)<c)and(c<(a+b))
if (flag1 and flag2 and flag3):
	print("Os lados não podem formar um triângulo")
	return
else:
	if (lado1==lado2) and (lado2==lado3):
		print("Triângulo Equilátero")
	elif (lado1==lado2) or (lado1==lado3) or (lado2==lado3):
		print("Triângulo Isóceles")
	else:
		print("Triângulo Escaleno")
