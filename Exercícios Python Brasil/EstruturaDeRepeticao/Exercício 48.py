num = int(input('Entre com um número inteiro: '))
num_emTexto = num.__str__()
num_emTexto = int(num_emTexto[::-1])
print(num_emTexto)
