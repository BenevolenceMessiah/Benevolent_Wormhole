# Modules/utils.py

import os
import yaml
import subprocess
import requests

def is_user_online(ip):
    try:
        subprocess.check_call(['ping', '-c', '1', ip], stdout=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def store_offline_message(username, message):
    data = {'messages': [message]}
    user_chat_dir = f"Chats/{username}"
    os.makedirs(user_chat_dir, exist_ok=True)
    offline_file = os.path.join(user_chat_dir, 'offline_messages.yml')
    with open(offline_file, 'w') as file:
        yaml.dump(data, file)

def check_offline_messages(username):
    offline_file = f"Chats/{username}/offline_messages.yml"
    if os.path.exists(offline_file):
        with open(offline_file, 'r') as file:
            data = yaml.safe_load(file)
            messages = data.get('messages', [])
            # Send stored messages
            for message in messages:
                # Implement sending the message
                pass
        # Delete the file after sending
        os.remove(offline_file)

def get_external_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        return response.json()['ip']
    except requests.RequestException:
        return None
