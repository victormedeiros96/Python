def checkIP(ip):
	ip = ip.split(".")
	for i in ip:
		if int(i)>255:
			return False
	return True
with open("arquivoExercicio1.txt", "r") as obj:
	arquivo = obj.read()
	IPs = arquivo.split("\n")[:-1]
IPs_validos = list()
IPs_invalidos = list()
for ip in IPs:
	a = checkIP(ip)
	if a:
		IPs_validos.append(ip)
	else:
		IPs_invalidos.append(ip)
print("[Endereços válidos:]")
for ip in IPs_validos:
	print(ip)
print("[Endereços inválidos:]")
for ip in IPs_invalidos:
	print(ip)
