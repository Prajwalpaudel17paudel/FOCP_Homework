import os
from cryptography.fernet import Fernet

FILE_NAME = 'passwd.txt'
KEY_FILE = 'key.key'

def generate_key():
    key = Fernet.generate_key()
    with open("passwd.txt", 'wb') as key_file:
        key_file.write(key)

def load_key():
    return open("passwd.txt", 'rb').read()

def read_file():
    users = []
    with open("passwd.txt", 'r') as file:
        for line in file:
            username, real_name, encrypted_password = line.strip().split(':')
            users.append((username, real_name, Fernet(load_key()).decrypt(encrypted_password.encode()).decode()))
    return users

def write_file(users):
    with open("passwd.txt", 'w') as file:
        for user in users:
            file.write(f'{user[0]}:{user[1]}:{Fernet(load_key()).encrypt(user[2].encode()).decode()}\n')

def add_user(username, real_name, password):
    users = read_file()
    if any(user[0] == username for user in users):
        print('Cannot add. Most likely username already exists.')
        return
    users.append((username, real_name, password))
    write_file(users)
    print('User Created.')

def delete_user(username):
    users = read_file()
    users = [user for user in users if user[0] != username]
    if not users:
        print('User not found.')
    else:
        write_file(users)
        print('User Deleted.')

def change_password(username, current_password, new_password):
    users = read_file()
    user_index = next((i for i, user in enumerate(users) if user[0] == username), None)
    if user_index is None:
        print('Username not found.')
        return
    if users[user_index][2] != current_password:
        print('Current password is invalid.')
        return
    users[user_index] = (username, users[user_index][1], new_password)
    write_file(users)
    print('Password changed.')

def login(username, password):
    users = read_file()
    user = next((user for user in users if user[0] == username), None)
    if user is None or user[2] != password:
        print('Access denied.')
    else:
        print('Access granted.')