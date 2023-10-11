import socket
import multiprocessing 
import time
import os

def start_socket(protocol:str, address:str, port:int):
    ADDRESS = address
    PROTOCOL = protocol
    HOST = socket.gethostname()
    PORT = port
    DIRECTION = (ADDRESS, PORT)


    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(DIRECTION)
    print(f"\nHOST '{HOST}': PROTOCOL --{PROTOCOL}-- RUNNING ON: '{ADDRESS}' --PORT:{PORT}--")

    # Listen for incoming connections
    sock.listen(5)
    print(f'LISTENING IN THE PORT {PORT}...\n')

    while True:
        connection, address = sock.accept()
        print(f'PING FROM ADDRESS: {address}')
        data = connection.recv(1024)
        if data:        
            print(data.decode("utf-8"))
            connection.sendall(data)
        connection.close()

def launch_process(PROTOCOLS:list):
    PROCESSES = []

    for PROTOCOL in PROTOCOLS:
        ADDRESS = PROTOCOL[1]
        PORT = PROTOCOL[2]
        PROCESS = multiprocessing.Process(target=start_socket, args=(PROTOCOL[0], ADDRESS, PORT))
        PROCESSES.append(PROCESS)
        PROCESS.start()
        time.sleep(1)

    for p in PROCESSES:
        p.join()



if __name__ == "__main__":
    ADDRESS = '192.168.50.12'
    PROTOCOLS = [
        ("HTTP", ADDRESS, 80),
        ("HTTPS", ADDRESS, 443),
        ("FTP", ADDRESS, 20),
        ("SFTP", ADDRESS, 22),
        ("RDP", ADDRESS, 3389),
        ("VPN", ADDRESS, 1194),
        ("PPTP", ADDRESS, 1723),
    ]
    launch_process(PROTOCOLS)
