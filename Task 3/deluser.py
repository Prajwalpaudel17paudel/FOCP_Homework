import sys
from password_manager import delete_user

def main():
    if len(sys.argv) != 2:
        print('Usage: python deluser.py <username>')
        return
    delete_user(sys.argv[1])

if __name__ == '__main__':
    main()