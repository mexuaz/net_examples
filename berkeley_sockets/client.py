import socket

# Create the socket
skt = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# Connect to the socket
# or test with localhost
host_adr = input("Enter hostname (quoteserver.seng.uvic.ca): ") or "quoteserver.seng.uvic.ca"
port = int(input("Enter port number (4444): ") or 4444)

print(f"Connecting to {host_adr}:{port} ...")
skt.connect((host_adr, port))

while True:
	# Get a line of text from the user
	# Asking for quote ABC,Jsmith
	fromUser = input("Enter a command/q to send/exit: ") or "ABC,John"
	if (fromUser == "q"):
		break
		
	# Send the user's query
	fromUser = fromUser + "\n"
	skt.send(fromUser.encode())
	
	# Read and print up to 1k of data.
	try:
		data = skt.recv(1024)
	except:
		print ('Connection to server closed.')
		break
	print(data.decode())

# close the connection, and the socket
skt.close()

