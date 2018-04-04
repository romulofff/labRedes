# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
#Dupla = (Marcus Vinícius Lucas Machado de Andrade, Rômulo Freire Férrer Filho)
#Matrícula = (385207, 385218)

import socket
import requests

#===============Questão 1===============

#Pega o hostname da máquina em que a aplicação está rodando através da função
#"gethostname()" e salva na variável "my_host_name".
my_host_name = socket.gethostname() 

#A função "gethostbyname(host_name)" retorna o endereço de IP de "host_name",
#assim, passo "my_host_name" como parâmetro para encontrar 
my_IP = socket.gethostbyname(my_host_name)

print("===============Questão 1===============")
print("Item A) "+my_IP)
print("Item B) "+my_host_name)
print("Item C) ")

for porta in range(10000): #Para 'porta' variando de 0 a 9999 
    #A função "getserverbyport('porta', 'protocolo') retorna o serviço usado pela
    #'porta' através do 'protocolo' especificado.
    #
    #Porém, é possível que nenhum serviço esteja sendo utilizado na porta 
    #especificada. Se isso ocorrer, a função levanta o erro "OSError". Então 
    #tratamos esse erro através do "try" e "except". Se OSError acontecer, a
    #variável que guarda o nome do serviço recebe "None".
    try:
        servico_tcp = socket.getservbyport(porta, 'tcp')
    except OSError:
        servico_tcp = None
    try:
        servico_udp = socket.getservbyport(porta, 'udp')
    except OSError:
        servico_udp = None
        
    print(porta, servico_tcp, servico_udp)
        
#===============Questão 2===============
print("===============Questão 2===============")

print("Item A) ")
lista_de_sites = ['www.oci.org.br', 'olimpiada.ic.unicamp.br', 'www.wacom.com', 'www.google.com', 'www.youtube.com', 'gshow.globo.com', 'www.lolja.com.br', 'www.lojanba.com.br', 'www.fortaleza.ce.gov.br', 'www.facebook.com.br']

#Utilizando a mesma função do Item A da primeira questão para imprimir na tela o nome do site e seu IP
for indice in range(10):
    print(lista_de_sites[indice], socket.gethostbyname(lista_de_sites[indice]))
    
print("Item B) ")
for indice in range(10):
    #'requisicao' recebe a resposta à requisição HTTP
    requisicao = requests.get('http://freegeoip.net/json/'+lista_de_sites[indice])
    #'dado' recebe o conteúdo .json da requisição
    dado = requisicao.json()
    #Printamos a informação 'country_name' do arquivo json.
    print(lista_de_sites[indice], dado['country_name'])
