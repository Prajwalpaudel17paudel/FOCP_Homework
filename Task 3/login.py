import sys
import getpass
from password_manager import login

def main():
    if len(sys.argv) != 3:
        print('Usage: python login.py <username>')
        return
    password = getpass.getpass('Password: ')
    login(sys.argv[1], password)

if __name__ == '__main__':
    main()