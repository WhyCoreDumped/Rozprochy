import socket

def run_server():
    serwer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    serwer_socket.bind(('127.0.0.1', 65432))
    
    serwer_socket.listen()
    print("Waiting for connection with client...")

    conection, address = serwer_socket.accept()
    
    with conection:
        print(f"Connected with server: {address}")
        
        data = conection.recv(1024).decode('utf-8')
        print(f"Received message: {data}")
        
        answer = "Message received"
        conection.sendall(answer.encode('utf-8'))


run_server()