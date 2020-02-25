import socket

## END OF IMPORTS ##

def client_program():
    host = '' # as both code is running on same pc # enter ip of server
    port = 5000 # socket server port number

    client_socket = socket.socket() # instantiate
    client_socket.connect((host, port))

    message = input("  -->  ") # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode()) # send message
        data = client_socket.recv(1024).decode() # receive response

        print("Received from server: " + data) # show in terminal

        message = input(" --> ") # again take input

    client_socket.close()

if __name__ == "__main__":
    client_program()