import socket

host = raw_input("Enter IP address: ")
port = 8088

MSG= raw_input("Enter message:")
#print ("lol", MSG)

#creating the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connecting to the server
s.connect((host, port))

#sending data 
s.send(MSG)

print s.recv(1024)
s.close
