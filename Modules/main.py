# Modules/main.py

import argparse
import os
from Modules import encryption, connection, messaging, file_transfer, utils, nat_traversal
import threading

def main():
    parser = argparse.ArgumentParser(
        description='Benevolent Wormhole - Secure Messaging and File Transfer',
        usage='BW <username> <key>'
    )
    parser.add_argument('username', help='Recipient username')
    parser.add_argument('key', help='Connection key (IP address or access token)')
    args = parser.parse_args()

    username = args.username
    key = args.key  # IP address of the recipient
    PORT = 65432    # Default port number

    # Create Chats/username directory if not exists
    user_chat_dir = os.path.join('Chats', username)
    os.makedirs(user_chat_dir, exist_ok=True)

    # Check if user is online
    online = utils.is_user_online(key)

    if not online:
        print(f"{username} is offline.")
        send_anyway = input("Do you want to send a message anyway? (y/n): ")
        if send_anyway.lower() == 'y':
            message = input("Enter your message: ")
            utils.store_offline_message(username, message)
            print("Your message has been stored and will be sent when the user is online.")
        else:
            print("Message not sent.")
        exit()

    # Generate encryption key
    enc_key = encryption.generate_key()

    # Open port using NAT traversal
    external_ip = nat_traversal.open_port(PORT)
    print(f"External IP: {external_ip}")

    # Establish connection
    try:
        conn = connection.establish_connection(key, PORT)
        print("Connection established.")
        # Send encryption key to recipient
        conn.sendall(enc_key)
    except Exception as e:
        print(f"Failed to connect to the recipient: {e}")
        exit()

    # Start chat interface
    # Check for offline messages to send
    utils.check_offline_messages(username)

    # Start threads for sending and receiving messages
    def send_messages():
        while True:
            message = input("")
            if os.path.isfile(message):
                # Handle file transfer
                file_transfer.send_file(conn, message)
            else:
                encrypted_message = encryption.encrypt_message(enc_key, message)
                messaging.send_message(conn, encrypted_message)

    def receive_messages():
        while True:
            data = conn.recv(4096)
            if data:
                try:
                    decrypted_message = encryption.decrypt_message(enc_key, data)
                    print(f"{username}: {decrypted_message}")
                except:
                    # Assume it's a file transfer
                    file_transfer.receive_file(conn, user_chat_dir)

    send_thread = threading.Thread(target=send_messages)
    receive_thread = threading.Thread(target=receive_messages)

    send_thread.start()
    receive_thread.start()

    send_thread.join()
    receive_thread.join()

if __name__ == "__main__":
    main()
