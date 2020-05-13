print("Data por extenso. (formato dd/mm/aaaa)")
meses = {1:"Janeiro",2:"Fevereiro",3:"Março",4:"Abril",5:"Maio",6:"Junho",7:"Julho",8:"Agosto",9:"Setembro",10:"Outubro",11:"Novembro",12:"Dezembro"}
data = input("Data de Nascimento: ")
mes = int(data[3:5])
print(f"Você nasceu em {data[:2]} de {meses[mes]} de {data[-4:]}.")
