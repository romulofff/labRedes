import socket
from datetime import datetime

#Criando socket
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Recebendo entrada
data = input("Type your message and press ENTER: ")
#Endereço de envio
addr = ("127.0.0.1",5001)
#Enviando:
udp.sendto(data.encode('utf-8'),addr)

#Recebendo Resposta
msg, server = udp.recvfrom(2048)
msg = msg.decode('utf-8')
print("Answer: %s" %msg)
udp.close()