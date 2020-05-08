tamanho_do_arquivo = float(input("Tamanho do arquivo em MB: "))
velocidade = float(input("Velocidade da internet em Mbps: "))
tempo = tamanho_do_arquivo/velocidade*8 # 8 bits por byte
print(f"Demorará {(tempo/60):.2f} minutos para baixar o arquivo.")
