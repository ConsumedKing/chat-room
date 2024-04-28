import socket as sc
import subprocess
import threading

ip = "localhost"
port = 5054

my_socket = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
my_socket.bind((ip, port))
my_socket.connect((ip, port))

name = "Default"

while True:
    message = input()
    if message == "change name":
        name = input("Enter New Name : ")
        continue
    if message.isspace() or len(message) == 0:
        continue
    my_socket.sendall(f"{name} : {message}".encode("utf-8"))
    print(my_socket.recv(1024).decode("utf-8"))
