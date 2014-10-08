#import socket module
from socket import *
serverPort	=	12000
serverSocket = socket(AF_INET, SOCK_STREAM) 
#Prepare a sever socket
#Fill in start
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print 'Ready to receive'
#Fill in end
while True:
	#Establish the connection
	print 'Ready to serve...'
	connectionSocket, addr = serverSocket.accept()
	try:
		message = connectionSocket.recv(1024) 		
		filename = message.split()[1]				
		f = open(filename[1:])						
		outputdata = f.read()
		#Send one HTTP header line into socket
		#Fill in start
		connectionSocket.send('HTTP/1.1 200 OK\r\nContent-Type:text/html\r\n')
		#Fill in end
		#Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i])
		connectionSocket.close()

	except IOError:
    	#Send response message for file not found
		#Fill in start 
		connectionSocket.sendall('HTTP/1.0 200 OK\r\nContent-Type:text/html\r\nConnection:close\r\n\r\n<html><head>404 File Not Found!!!</head></html>\r\n')
		#Fill in end
		#Close client socket 
		#Fill in start
		clientSocket.close()
		serverSocket.close()
		#Fill in end
serverSocket.close()