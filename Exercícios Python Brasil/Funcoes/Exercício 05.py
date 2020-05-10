def somaImposto(custo,taxaImposto):
	return (custo*(1+taxaImposto/100))
def main():
	custo = float(input('Qual o custo do produto? '))
	taxa_de_imposto = float(input('Qual a taxa de imposto (%) sobre produto? '))
	valor_final = somaImposto(custo,taxa_de_imposto)
	print(valor_final)
# PORQUE UTILIZAR O IF NAME?
# PARA QUE QUANDO IMPORTE O ARQUIVO COMO UM MÒDULO, NAO OCORRA DE EXECUTAR A MAIN AUTOMATICAMENTE 
# EM OUTRAS PALAVRAS, É UMA BOA PRATICA.
if __name__ == '__main__':
	main()
