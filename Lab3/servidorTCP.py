import socket
from datetime import datetime

print("==================Questão 2==================")
print("Item B - Servidor TCP)")

#Utilizamos a porta e o endereço definidos.
port = 5002
adress = '127.0.0.1'

#Criamos o socket TCP e salvamos na variável tcp
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Tupla que contém endereço e porta
ap = (adress, port)

#Vincula nosso socket ao endereço e porta especificados.
tcp.bind(ap)

#Permite que o servidor aceite conexões através desse socket.
tcp.listen()

#Utilizamos while True para manter nossa aplicação rodando o tempo todo,
#sem precisar rodar a aplicação de novo para novas conexões.
while True:
    #Aceita a conexão requerida através do socket 'tcp'. Entretanto, o método
    #.accept() retorna uma tupla, onde 'client' é o endereço vinculado à conexão fim a fim
    #e 'con' é um novo socket, por onde serão trocadas informações.
    con, client = tcp.accept()

    print('Conectado por ', client)

    #Recebe mensagem através do socket 'con', decodifica em utf-8 e salva em 'mensagem'
    mensagem = con.recv(2048).decode('utf-8')

    print("Mensagem recebida: %s" %mensagem)
    # print(str(mensagem))

    #Se o horário atual, detectado através de datetime.now(), for antes de 
    #meio-dia (12 horas), o servidor envia uma mensagem de Bom Dia codificada em utf-8.
    if(int(datetime.now().strftime("%H")) < 12):
        con.send(('Bom dia, %s' %mensagem).encode('utf-8'))
    #Se não, se o horário atual, for depois de meio-dia (12 horas) e antes de 18 horas
    #o servidor envia uma mensagem de Boa Tarde codificada em utf-8.
    elif((int(datetime.now().strftime("%H")) > 12) and int(datetime.now().strftime("%H")) < 18):
        con.send(('Boa Tarde, %s' %mensagem).encode('utf-8'))
    #Se não, então temos que o horário atual é maior que 18 horas, então o servidor envia
    #uma mensagem de Boa noite codificada em utf-8.
    else:
        con.send(('Boa Noite, %s' %mensagem).encode('utf-8'))
    # con.send("Mensagem processada no servidor".encode('utf-8'))
    print("Finalizando conexão ", client)
    #Por fim, fechamos o socket.
    con.close()