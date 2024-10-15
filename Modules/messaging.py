def send_message(connection, message):
    connection.sendall(message)

def receive_message(connection):
    return connection.recv(1024)
