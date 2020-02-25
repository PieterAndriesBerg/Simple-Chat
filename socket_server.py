import socket

## END OF IMPORTS ##

def server_program():
    # get the hostname
    host = ''
    port = 5000 # initiate port number above 1024

    server_socket = socket.socket() # get instance
    #look closely. the bind() fucntion takes tuple as an argument
    server_socket.bind((host, port))

    # configure how many client the server can listen sumultanously
    server_socket.listen(2)
    conn, address = server_socket.accept() # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream, it won't accept data packet greater than 1024 bytes
        data =conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("From connected User: " + str(data))
        data = input('  -> ')
        conn.send(data.encode()) # send data to the client

    conn.close() # close the connection

if __name__ == '__main__':
    server_program()