# deluser.py
def delete_user(username, passwd_file):
    with open(passwd_file, 'r') as file:
        lines = file.readlines()

    with open(passwd_file, 'w') as file:
        for line in lines:
            if not line.startswith(f'{username}:'):
                file.write(line)
    
    print('User Deleted.')

if __name__ == "__main__":
    passwd_file = 'passwd.txt'
    username = input('Enter username: ')
    
    delete_user(username, passwd_file)
