import socket
import datetime
print("==================Questão 2==================")
print("Item B - Cliente TCP)")

#Utilizamos a porta e o endereço definidos.
port = 5002
adress = '127.0.0.1'

#Criamos o socket TCP e salvamos na variável tcp
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Tupla que contém endereço e porta
to = (adress, port)

#Conecta nosso socket ao endereço e porta especificados
tcp.connect(to)

print("Cliente conectado ao servidor %s na porta %s" % (adress,port))

#Apresenta essa mensagem na tela e salva o input do usuário em 'msg'
msg = input("Digite algo e aperta ENTER: ")

#Através do nosso socket, envia a mensagem 'msg' para o servidorTCP com codificação utf-8.
tcp.send(msg.encode('utf-8'))

#Recebemos dados através do nosso socket com o método recv de tamanho no máximo 2048 bytes.
#E então decodificamos no formato utf-8.
recebida = tcp.recv(2048).decode('utf-8')

#Printamos os dados recebidos.
print("dados recebidos: %s" %recebida)

#Por fim, fechamos o socket.
tcp.close()