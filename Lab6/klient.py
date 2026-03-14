import socket

def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    print("Connecting with a server...")
    client_socket.connect(('127.0.0.1', 65432))
    

    print("What massage do you want to send?")
    message = input()
    print(f"Sending: {message}")
    client_socket.sendall(message.encode('utf-8'))
    
    answer = client_socket.recv(1024).decode('utf-8')
    print(f"Answer from the server: {answer}")
    
    client_socket.close()


run_client()