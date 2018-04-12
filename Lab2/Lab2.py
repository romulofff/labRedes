import urllib
import socket
import json

# ==================Questão 1==================
lista_de_sites = ['http://www.oci.org.br', 'http://olimpiada.ic.unicamp.br', 'http://www.wacom.com', 'http://www.google.com', 'http://www.youtube.com', 'http://gshow.globo.com', 'http://www.lolja.com.br', 'http://www.lojanba.com.br', 'http://www.fortaleza.ce.gov.br', 'http://www.facebook.com.br']
print("==================Questão 1==================")
print("Item A)")

for site in range(10):
    informacoes_site = urllib.request.urlopen(lista_de_sites[site])
    print("========"+lista_de_sites[site]+"========")
    print(informacoes_site.info())
    print("=========================================")

print("Item B)")

for site in range(10):
    informacoes_site = urllib.request.urlopen(lista_de_sites[site])
    print(lista_de_sites[site]+" - Código: "+str(informacoes_site.getcode()))

# ==================Questão 2==================
print("==================Questão 2==================")
print("Item A)")
    
lista_de_ceps = ["60326345", "63500478", "62800976", "47808021"]

for cep in range(4):
    try:
        site = urllib.request.urlopen("http://viacep.com.br/ws/"+lista_de_ceps[cep]+"/json")
        informacoes_site = json.load(site)
        print(lista_de_ceps[cep] + " - Logradouro: " + informacoes_site["logradouro"])
    except urllib.error.HTTPError as error:
        print("Erro: ", error)
    except urllib.error.URLError as error:
        print("Error: ", error)

print("Item B)")
try:
    pesquisa = urllib.request.urlopen("https://www.google.com.br/search?q=Luke-Cage")
except urllib.error.HTTPError as error:
    print("Erro: ", error)
except urllib.error.URLError as error:
    print("Erro: ", error)