import socket
from datetime import datetime

print("==================Questão 2==================")
print("Item A - Cliente UDP)")

#Criamos o socket UDP e salvamos na variável 'udp'
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Apresenta essa mensagem na tela e salva o input do usuário em 'data'
data = input("Type your message and press ENTER: ")

#Utilizamos a porta e o endereço definidos.
addr = ("127.0.0.1",5001)

#Através do nosso socket, envia a mensagem 'data' para o servidorUDP com codificação utf-8.
udp.sendto(data.encode('utf-8'),addr)

#Recebemos dados através do nosso socket com o método recvfrom de tamanho no máximo 2048 bytes.
msg, server = udp.recvfrom(2048)

#E então decodificamos no formato utf-8.
msg = msg.decode('utf-8')

print("Answer: %s" %msg)

#Por fim, fechamos o socket.
udp.close()