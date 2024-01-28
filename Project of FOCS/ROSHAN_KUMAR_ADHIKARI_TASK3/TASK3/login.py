# login.py

# Import the password checking function and getpass for secure password input
from password_util import check_password
import getpass

# Define a function to handle user login
def login(username, password, passwd_file):
    """
    Attempts to log in the user with the specified credentials.

    Args:
        username (str): The username entered by the user.
        password (str): The password entered by the user.
        passwd_file (str): The path to the password file.

    Returns:
        None
    """

    # Open the password file for reading
    with open(passwd_file, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Split the line into username, real name (discarded), and encrypted password
            stored_username, _, stored_encrypted_password = line.strip().split(':')

            # Check if the entered username matches the stored username and if the password matches
            if stored_username == username and check_password(stored_encrypted_password, password):
                print('Access granted.')  # Notify of successful login
                return  # Exit the function

    # If no match is found, deny access
    print('Access denied.')

# If the script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Specify the password file name
    passwd_file = 'passwd.txt'

    # Prompt the user for their username
    username = input('User: ')

    # Prompt for password using getpass for hidden input
    password = getpass.getpass('Password: ')

    # Call the login function to attempt authentication
    login(username, password, passwd_file)
