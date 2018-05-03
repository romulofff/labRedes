import socket
from datetime import datetime
# port = 25000
# adress = '192.168.15.112'
port = 5002
adress = '127.0.0.1'
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ap = (adress, port)
tcp.bind(ap)
tcp.listen()
while True:
    con, client = tcp.accept()
    print('Conectado por ', client)
    mensagem = con.recv(2048).decode('utf-8')
    print("Mensagem recebida: %s" %mensagem)
    # print(str(mensagem))
    if(int(datetime.now().strftime("%H")) < 12):
        con.send(('Bom dia, %s' %mensagem).encode('utf-8'))
    elif((int(datetime.now().strftime("%H")) > 12) and int(datetime.now().strftime("%H")) < 18):
        con.send(('Boa Tarde, %s' %mensagem).encode('utf-8'))
    else:
        con.send(('Boa Noite, %s' %mensagem).encode('utf-8'))
    # con.send("Mensagem processada no servidor".encode('utf-8'))
    print("Finalizando conexão ", client)
    con.close()