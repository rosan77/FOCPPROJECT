# adduser.py

# Import the password encryption function from a separate module
from password_util import encrypt_password

# Define a function to add a new user to the password file
def add_user(username, real_name, password, passwd_file):
   """
   Adds a new user to the specified password file. The password is encrypted before being stored.

   Args:
       username (str): The username for the new user.
       real_name (str): The real name of the new user.
       password (str): The password for the new user.
       passwd_file (str): The path to the password file.

   Returns:
       None
   """

   # Open the password file in append mode to add a new line
   with open(passwd_file, 'a') as file:
       # Encrypt the password using the imported function
       encrypted_password = encrypt_password(password)
       # Write the user information to the file in a colon-separated format
       file.write(f'{username}:{real_name}:{encrypted_password}\n')

   # Print a message to confirm user creation
   print('User Created.')

# If the script is being run directly (not imported as a module)
if __name__ == "__main__":
   # Specify the password file name
   passwd_file = 'passwd.txt'

   # Prompt the user to enter the new user's information
   username = input('Enter new username: ')
   real_name = input('Enter real name: ')
   password = input('Enter password: ')

   # Check for existing usernames to prevent duplicates
   with open(passwd_file, 'r') as file:
       existing_users = [line.split(':')[0] for line in file]  # Extract usernames from each line

   if username in existing_users:
       print('Cannot add. Most likely username already exists.')
   else:
       # Call the add_user function to create the new user
       add_user(username, real_name, password, passwd_file)
