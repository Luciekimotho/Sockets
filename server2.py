import socket
import sys


port = 8088
host = '127.0.0.1'
BUFFER_SIZE = 20

#creating the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#binding the socket to host ip & port
try:
	s.bind((host, port))
except socket.error, msg:
	print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
	sys.exit()
print ('Socket bind completed')

#start listening on socket
s.listen(5)
print ('Socket now listening')


#connecting with the client
conn, addr = s.accept()
#print ('Got connection from', addr)
while True:

#receiving the data from the clent
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print ("Message from client: "+ data)
    conn.send(data)
    #conn.send('Thank you for connecting')
conn.close()
