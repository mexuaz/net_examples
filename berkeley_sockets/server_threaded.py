import socket
import threading


class WorkerThread( threading.Thread ):
	def __init__(self,conn,counter):
		self.conn = conn
		self.number = counter
		self.numstr = str(self.number)
		threading.Thread.__init__(self)
	
	def run(self):
		connected = True
		# If timeouts are required, set timeout to a value greater than zero in seconds. ie: 0.1 would me 100ms
		# self.conn.settimeout(0.1) 
		print ('Thread #'+ self.numstr + ": Started\n")
		while connected:
			try:
				data = conn.recv(1024)
				if (data):
					print ('Thread #' + self.numstr + ' received: ' + data.decode())
					echo_str = 'ECHO: ' + data.decode()
					self.conn.send(echo_str.encode())
				else:
					print ('Thread #' + self.numstr + ': Connection to client closed')
					print ('Thread #' + self.numstr + ': Ending')
					connected = False
			except socket.timeout:
				print  ('Thread #' + self.numstr + ': Listen timeout')
				


# "quoteserver.seng.uvic.ca"
host_adr = input("Enter hostname (localhost): ") or "localhost"

# 44400-44459
port = int(input("Enter port number (4444): ") or 4444)

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skt.bind((host_adr, port))
skt.listen(128)
counter = 0
while 1:
	print ('Main: waiting ...')
	conn, addr = skt.accept()
	counter = counter + 1
	print ('Main: Connection from ' + addr[0])

	try:
		# Keep track of the running threads
		WorkerThread(conn, counter).start()
	except socket.error:
                print ('Main: Lost connection from:'+ addr[0])

