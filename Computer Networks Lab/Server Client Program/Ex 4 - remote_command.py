#remote sender.py
import socket
UDP_IP = "localhost"
UDP_PORT = 8080
MESSAGE = "notepad"
print("message:",MESSAGE)
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto(bytes(MESSAGE,"utf-8"),(UDP_IP,UDP_PORT))

#remote receiver.py
import socket
import wmi
UDP_IP = "localhost"
UDP_PORT = 8080
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))
while True:
    data,addr = sock.recvfrom(1024)
    str = data.decode("utf-8")
    print("Received message:",str)
    print("opening",str)
conn = wmi.WMI()
pid,returnval = conn.Win32_Process.Create(commandLine = str)

