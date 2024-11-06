#Server Coding: 
import socket 
s = socket.socket() 
host = socket.gethostname()
port = 8080 
s.bind((host,port))  
s.listen(1) 
print(host) 

print("Waiting for incoming connection... ") 
conn, addr = s.accept() 
print(addr, "Has connected to the server") 
filename = input(str("Enter the name of the file to be transmitted: ")) 
file = open(filename , 'rb') 
file_data = file.read(1024) 
conn.send(file_data) 
print("File has transmitted successfully")


#Client Coding: 
import socket 
s = socket.socket() 
host = input(str("Please enter the host address of the sender: ")) 
port = 8080 
s.connect((host,port)) 
print("Connected ... ") 
filename = input(str("Please enter a filename for the incoming file: ")) 
file = open(filename, 'wb') 
# Opens a file for writing only in binary format 
file_data = s.recv(1024) 
file.write(file_data) 
file.close() 
print("File has been received successfully.")