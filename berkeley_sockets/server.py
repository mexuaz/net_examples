import socket


# "quoteserver.seng.uvic.ca"
host_adr = input("Enter hostname (localhost): ") or "localhost"
port = int(input("Enter port number (4444): ") or 4444)

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skt.bind((host_adr, port))
skt.listen(1)
while True:
	print ('Main: waiting ...')
	conn, addr = skt.accept()
	print ('Connection from: ' + addr[0])

	while True:
		data = conn.recv(1024)
		if (data):
			print ('Received: ' + data.decode())
			
			echo_str = 'ECHO: ' + data.decode()
			conn.send(echo_str.encode())
		else:
			break

