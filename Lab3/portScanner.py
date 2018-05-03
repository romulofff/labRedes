import socket
import sys
from datetime import datetime
#Site a ser testado
remoteServer    = "ufc.br"
#Pegando endereço IP do site
remoteServerIP  = socket.gethostbyname(remoteServer)
print(remoteServer + " hosted @"+remoteServerIP)
#Apenas deixando bonito
x = ' '
print("="*60)
print(25*'-' + " Scanning " + 25*'-')
print('='*60)
#Lista de portas a serem testadas + porta 80
portsToTry = [20,21,22,25,53,80,110,443,8080,3306]
#Laço para testes
for port in portsToTry:  
    try:
        #Cria o socket TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Conectando a porta: {}".format(port))
        #Conectando ao servidor
        sock.connect((remoteServerIP, port))
        try:
            #Obtendo serviço da porta em questão
            servico_tcp = socket.getservbyport(port, 'tcp')
        except OSError:
            servico_tcp = None
        print("A porta: {} pertence ao serviço: {}".format(port,servico_tcp))
        #Fechando o socket
        sock.close()
#Possíveis exceções levantadas.
    except KeyboardInterrupt:
        print ("Você pressionou Ctrl+C")
        sys.exit()

    except socket.error:
        print ("Não pode conectar ao servidor")
        