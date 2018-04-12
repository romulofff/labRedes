import urllib.request
import urllib.error
import json
# Dupla: (Marcus Vinícius L. M. de Andrade, 385207)
#        (Rômulo Freire Férrer Filho, 385218)

# ==================Questão 1==================
lista_de_sites = ['http://www.oci.org.br', 'http://olimpiada.ic.unicamp.br', 'http://www.wacom.com', 'http://www.google.com', 'http://www.youtube.com', 'http://gshow.globo.com', 'http://www.lolja.com.br', 'http://www.lojanba.com.br', 'http://www.fortaleza.ce.gov.br', 'http://www.facebook.com.br']
print("==================Questão 1==================")
print("Item A)")

for site in range(10): #"site" varia de 0-9
    #urlopen(url) abre a URL url e salva em alguma variável.
    #
    #Aplicamos urlopen() no índice atual da lista_de_sites e salvamos na variável
    #informacoes_site.
    informacoes_site = urllib.request.urlopen(lista_de_sites[site])
    print("========"+lista_de_sites[site]+"========")
    #Aqui printamos na tela as informações que conseguimos salvar em informacoes_sites
    #através do .info()
    print(informacoes_site.info())
    print("=========================================")
'''
    http://www.oci.org.br
    Date: É a data de acesso ao site. Contém data e horário do acesso;
    
    http://olimpiada.ic.unicamp.br
    Content-Type: Tipo de conteúdo da página, no caso é um arquivo html;
    
    http://www.wacom.com
    Set-Cookie: Serve para enviar cookies do servidor para o usuário;
    
    http://www.google.com
    Cache-Control: É utilizado para criar regras nos mecanismos de requisição
    e resposta que utilizam cache;
    
    http://www.youtube.com
    X-Content-Type-Options: É usado para dizer que os "MIME types", que são um modo
    padronizado de ditar a natureza e o formato de um documento, devem ser seguidos
    e não alterados.
    
    http://gshow.globo.com
    Server: Contém dados sobre o software utilizado no servidor.
    
    http://www.lolja.com.br
    Transfer-Encoding: Dita o modo de codificação para transferir o Entity Header para
    o usuário. Entity Header é um cabeçalho que descreve o conteúdo da mensagem.
    
    http://www.lojanba.com.br
    Expires: Contém a data e horário em que a requisição passa a ser considerada
    ultrapassada.
    
    http://www.fortaleza.ce.gov.br
    Connection: Define se a conexão atual cliente-servidor continua aberta ou 
    se é fechada depois que a troca de informação atual termina.
    
    http://www.facebook.com.br
    Vary: Determina como as futuras requisições vão decidir se é melhor utilizar
    uma resposta que está em cache ou pedir uma nova do servidor.
    
'''
print("Item B)")

for site in range(10): #"site" varia de 0-9
    #Aplicamos urlopen() no índice atual da lista_de_sites e salvamos na variável
    #informacoes_site.
    informacoes_site = urllib.request.urlopen(lista_de_sites[site])
    #Aqui printamos o site e logo após o código de resposta da requisição HTTP
    print(lista_de_sites[site]+" - Código: ", informacoes_site.getcode())
'''
    Sim, os códigos são iguais. Todos os códigos foram 200, que é o código de
    resposta HTTP para dizer que foi tudo OK e a requisição foi sucedida.
'''

# ==================Questão 2==================
print("==================Questão 2==================")
print("Item A)")
    
lista_de_ceps = ["60326345", "63500478", "62800976", "47808021"]

for cep in range(4): #"cep" varia de 0-3
    #Abrimos a url especificada através de urlopen() e salvamos em site. Após isso
    #salvamos como um arquivo .json em informacoes_site.
    #Depois exibimos a informação "Logradouro" presente em informacoes_site.
    #
    #Porém, é possível que ocorra algum problema com nossa requisição e algum erro
    #seja levantado. Por isso tratamos HTTPError e URLError com o except. Caso
    #algum erro ocorra, o nome do erro será printado na tela.
    try:
        site = urllib.request.urlopen("http://viacep.com.br/ws/"+lista_de_ceps[cep]+"/json")
        informacoes_site = json.load(site)
        print(lista_de_ceps[cep] + " - Logradouro: " + informacoes_site["logradouro"])
    except urllib.error.HTTPError as error:
        print("Erro: ", error)
    except urllib.error.URLError as error:
        print("Error: ", error)

print("Item B)")
    #Tentamos abrir a URL de pesquisa do Google e tratamos os possíveis erros
    #HTTPError e URLError.
try:
    pesquisa = urllib.request.urlopen("https://www.google.com.br/search?q=Luke-Cage")
except urllib.error.HTTPError as error:
    print("Erro: ", error)
except urllib.error.URLError as error:
    print("Erro: ", error)
    
'''
    Da primeira vez obtivemos o erro 403 Forbidden, que significa que o cliente não
    possui direito de acesso ao conteúdo, então o servidor rejeita a requisição do
    cliente.
    Essa rejeição acontece porque o servidor do Google detecta que é um bot quem
    está fazendo a requisição e faz esse bloqueio para evitar um possível ataque.
    
    O que podemos fazer para contornar esse problema é criar uma requisição com o
    header de algum browser conhecido, como o Mozilla. Nesse caso o servidor do Google
    identificará nossa requisição como sendo de um browser conhecido e irá liberar o
    acesso
'''
    #Criamos o objeto 'requisicao', com o Request(), adicionando o parâmetro
    #"headers" para mascarar nossa "identidade".
requisicao = urllib.request.Request("https://www.google.com.br/search?q=Luke-Cage", headers={'User-Agent': 'Mozilla/5.0'})
print("Item B) Segunda tentativa:")
try:
    #Passamos nosso objeto 'requisicao' como parâmetro em urlopen() e salvamos
    #a resposta na variável 'pesquisa'.
    pesquisa = urllib.request.urlopen(requisicao)
    
    #Se não houver erro, irá ser printado na tela o código de resposta HTTP
    #e as informações sobre a pesquisa.
    print("Código de Resposta HTTP: ", pesquisa.getcode())
    print("Info: ")
    print(pesquisa.info())
except urllib.error.HTTPError as error:
    print("Erro: ", error)
except urllib.error.URLError as error:
    print("Erro: ", error)