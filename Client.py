import socket
import threading

# Server configuration
SERVER = '127.0.0.1'  # Server IP address
PORT = 5555

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Server: {message}")
            else:
                break
        except:
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))

    # Start a thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    while True:
        message = input("You: ")
        if message.lower() == 'exit':
            break
        client.send(message.encode('utf-8'))

    client.close()

if __name__ == "__main__":
    main()

