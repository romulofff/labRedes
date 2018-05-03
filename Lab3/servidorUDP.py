import socket
from datetime import datetime

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ap = ('127.0.0.1',5001)

udp.bind(ap)

print("UDP Server @127.0.0.1-5001")
while True:
	data, addr = udp.recvfrom(2048)
	data = data.decode('utf-8')
	print("DATA: %s from: %s" %(data.strip(), addr))
	if(int(datetime.now().strftime("%H")) < 12):
		udp.sendto(('Bom dia, %s' %data).encode('utf-8'),addr)
	elif((int(datetime.now().strftime("%H")) > 12) and int(datetime.now().strftime("%H")) < 18):
		udp.sendto(('Boa Tarde, %s' %data).encode('utf-8'),addr)
	else:
		udp.sendto(('Boa Noite, %s' %data).encode('utf-8'),addr)
	