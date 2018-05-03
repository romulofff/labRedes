import socket
import datetime

# port = 25000
# adress = '192.168.15.112'
port = 5002
adress = '127.0.0.1'
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
to = (adress, port)
tcp.connect(to)
print("Cliente conectado ao servidor %s na porta %s" % (adress,port))
msg = input("Digite algo e aperta ENTER: ")
tcp.send(msg.encode('utf-8'))
recebida = tcp.recv(2048).decode('utf-8')
print("dados recebidos: %s" %recebida)
tcp.close()