# Modules/connection.py

import socket
import ssl

def establish_connection(ip, port):
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    # If using self-signed certificates, set verify_mode
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    secure_socket = context.wrap_socket(s, server_hostname=ip)
    secure_socket.connect((ip, port))
    return secure_socket
