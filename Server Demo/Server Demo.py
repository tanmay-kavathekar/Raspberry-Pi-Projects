"""
This code is used to demonstrate how to create a live server 
The following link will give you information on the socket interfacing
https://docs.python.org/2/library/socket.html
The following link will give you information on system parameters and functions
https://docs.python.org/2/library/sys.html?highlight=sys#module-sys
"""
import socket
import sys 

host=""
port=8888

rpisock=socket.socket(socket.AF_INET,scoket.SOCK_STREAM)

try:
	rpisock.bind((host,port)) #input is a tuple
except socket.error:
	print("Failed to bind!")
	sys.exit()
rpisock.listen(5) #the number of queued connections (5)(max=system dependent,min=0)

while True:
	conn, addr=rpisock.accept()
	data=conn.recv(1000) #max bytes received (1000) 
	if not data:
		break
	conn.sendall(b"Connection is established!") #b is used to convert string to byte array
conn.close()
rpisock.close()
