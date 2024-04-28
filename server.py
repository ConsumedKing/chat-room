import socket as sc
import subprocess
import threading

#ip = subprocess.check_output(r"ip address show eth0 | grep -oP '(?<=inet )[\d.]+(?=/)'", shell=True)
#ip = ip.decode("utf-8").strip()
ip = "localhost"
port = 5050

server = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
server.bind((ip, port))
server.listen()

clients = []

def handle_connection(socket: sc.socket, address: str):
    while True:
        message = socket.recv(1024).decode("utf-8")
        if not message:
            break
        for clinet in clients:
            if clinet != threading.current_thread():
                clinet.socket.sendall(message.encode("utf-8"))
    socket.close()
    clients.remove(threading.current_thread())

while True:
    socket, address = server.accept()
    thread = threading.Thread(target=handle_connection, args=(socket, address))
    clients.append(thread)
    thread.start()
