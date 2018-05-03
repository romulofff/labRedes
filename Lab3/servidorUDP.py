import socket
from datetime import datetime

print("==================Questão 2==================")
print("Item A - Servidor UDP)")

#Criamos o socket UDP e salvamos na variável udp
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Utilizamos a porta e o endereço definidos.
ap = ('127.0.0.1', 5001)

#Tupla que contém endereço e porta especificados.
udp.bind(ap)

print("UDP Server @127.0.0.1-5001")
#Utilizamos while True para manter nossa aplicação rodando o tempo todo,
#sem precisar rodar a aplicação de novo para novas conexões.
while True:
	#Aqui, comparando com o servidor TCP, é interessante notar que não precisamos, antes de
	#receber os dados, aceitar uma conexão. Isso por causa do próprio protocolo UDP, que
	#não requer essa "conexão prévia".

	#Recebe mensagem de, no máximo 2048 bytes. Salvamos a mensagem em 'data'
	#e o endereço de onde recebemos em 'addr'.
	data, addr = udp.recvfrom(2048)

	#Decodificamos a mensagem recebida com utf-8.
	data = data.decode('utf-8')

	print("DATA: %s from: %s" %(data.strip(), addr))
	#Se o horário atual, detectado através de datetime.now(), for antes de 
    #meio-dia (12 horas), o servidor envia uma mensagem de Bom Dia codificada em utf-8.
	if(int(datetime.now().strftime("%H")) < 12):
		udp.sendto(('Bom dia, %s' %data).encode('utf-8'),addr)
	#Se não, se o horário atual, for depois de meio-dia (12 horas) e antes de 18 horas
    #o servidor envia uma mensagem de Boa Tarde codificada em utf-8.
	elif((int(datetime.now().strftime("%H")) > 12) and int(datetime.now().strftime("%H")) < 18):
		udp.sendto(('Boa Tarde, %s' %data).encode('utf-8'),addr)
	#Se não, então temos que o horário atual é maior que 18 horas, então o servidor envia
    #uma mensagem de Boa noite codificada em utf-8.
	else:
		udp.sendto(('Boa Noite, %s' %data).encode('utf-8'),addr)
	