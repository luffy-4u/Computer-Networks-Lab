#server program
import socket
def server_program():
    host = socket.gethostname()
    port = 5000
    server_socket = socket.socket()
    server_socket.bind((host,port))
    server_socket.listen(2)
    conn,address = server_socket.accept()
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user:"+data)
        data = input('->')
        conn.send(data.encode())
    conn.close()

server_program()



#client program
import socket
def client_program():
    print('type bye to terminate')
    host = socket.gethostname()
    port = 5000
    client_socket = socket.socket()
    client_socket.connect((host,port))
    message = input("->")
    while message.lower().strip()!='bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print('received from server:'+data)
        message = input("->")
    client_socket.close()

client_program()

