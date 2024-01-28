import sys
import getpass
from password_manager import change_password

def main():
    if len(sys.argv) != 4:
        print('Usage: python passwd.py <username>')
        return
    current_password = getpass.getpass('Current Password: ')
    new_password = getpass.getpass('New Password: ')
    confirm_password = getpass.getpass('Confirm: ')
    if new_password != confirm_password:
        print('Passwords do not match.')
        return
    change_password(sys.argv[1], current_password, new_password)

if __name__ == '__main__':
    main()