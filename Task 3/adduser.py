import sys
import getpass
from password_manager import add_user

def main():
    if len(sys.argv) != 4:
        print('Usage: python adduser.py <username> <real_name> <password>')
        return
    add_user(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == '__main__':
    main()