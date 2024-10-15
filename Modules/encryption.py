from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_message(key, message):
    f = Fernet(key)
    return f.encrypt(message.encode())

def decrypt_message(key, encrypted_message):
    f = Fernet(key)
    return f.decrypt(encrypted_message).decode()
