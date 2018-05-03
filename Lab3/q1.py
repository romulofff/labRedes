import socket

print('='*20 + " Questão 1 " + '='*20)
print("Item a)")
#Escolhendo o site e criando requisição GET
request = b"GET / HTTP/1.1\nHost: www.youtube.com\n\n"
#Criando o cliente socket utilizando TCP, especificado em "SOCK_STREAM"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Conecta com o host
s.connect(("youtube.com", 80))
#Envia requisição
s.send(request)
#Recebe resposta
result = s.recv(4096)
#Printa resposta
print(result)

'''

O código recebido é 301, ou seja, a página buscada foi movida permanentemente. 
No campo "location" encontra-se o novo endereço da página

'''