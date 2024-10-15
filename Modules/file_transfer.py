# Modules/file_transfer.py

import os
from tqdm import tqdm

def send_file(connection, file_path):
    filesize = os.path.getsize(file_path)
    connection.sendall(f"FILE:{os.path.basename(file_path)}:{filesize}".encode())

    with open(file_path, 'rb') as f:
        progress = tqdm(range(filesize), f"Sending {file_path}", unit="B", unit_scale=True, unit_divisor=1024)
        for chunk in iter(lambda: f.read(4096), b""):
            connection.sendall(chunk)
            progress.update(len(chunk))

def receive_file(connection, save_dir):
    metadata = connection.recv(1024).decode()
    if metadata.startswith("FILE:"):
        _, filename, filesize = metadata.split(":")
        filesize = int(filesize)
        save_path = os.path.join(save_dir, filename)

        with open(save_path, 'wb') as f:
            progress = tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
            bytes_received = 0
            while bytes_received < filesize:
                chunk = connection.recv(4096)
                if not chunk:
                    break
                f.write(chunk)
                bytes_received += len(chunk)
                progress.update(len(chunk))
    else:
        # Handle other types of messages
        pass
