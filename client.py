import socket as sc
import subprocess
import threading

ip = "localhost"
port = int(input("Enter port number : "))

my_socket = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
my_socket.bind((ip, port))
my_socket.connect((ip, 5050))

name = "Default"

while True:
    message = input()
    if message == "change name":
        name = input("Enter New Name : ")
        continue
    if message.isspace() or len(message) == 0:
        print(my_socket.recv(1024).decode("utf-8"))
        continue
    my_socket.sendall(f"{name} : {message}".encode("utf-8"))
    print(my_socket.recv(1024).decode("utf-8"))
