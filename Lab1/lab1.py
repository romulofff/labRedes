import requests
import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
#item a
print(ip)
#item b
print(hostname)

for porta in range(10000):
	try:
		tcp = socket.getservbyport(porta, 'tcp')
	except OSError:
		tcp = None
	try:	
		udp = socket.getservbyport(porta, 'udp')
	except OSError:
		udp = None
	
	
	print(porta, tcp, udp)