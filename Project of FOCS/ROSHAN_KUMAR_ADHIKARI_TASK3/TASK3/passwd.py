# passwd.py

# Import necessary functions for password encryption, checking, and secure input
from password_util import encrypt_password, check_password
import getpass

# Define a function to handle password changes
def change_password(username, current_password, new_password, passwd_file):
    """
    Changes the password for the specified user in the password file.

    Args:
        username (str): The username of the user whose password needs to be changed.
        current_password (str): The user's current password.
        new_password (str): The new password to set for the user.
        passwd_file (str): The path to the password file.

    Returns:
        None
    """

    # Read the entire password file into a list of lines
    with open(passwd_file, 'r') as file:
        lines = file.readlines()

    # Iterate through each line, searching for the user's entry
    for i, line in enumerate(lines):
        if line.startswith(f'{username}:'):  # Check if the line starts with the username
            parts = line.strip().split(':')  # Split the line into username, real name, and encrypted password

            # Verify that the line has the expected format
            if len(parts) == 3:
                _, _, current_encrypted_password = parts  # Discard first two parts

                # Check if the provided current password matches the stored encrypted password
                if check_password(current_encrypted_password, current_password):
                    # If password matches, update the line with the new encrypted password
                    lines[i] = f'{username}:{parts[1]}:{encrypt_password(new_password)}\n'
                    with open(passwd_file, 'w') as file:  # Overwrite the file with the updated lines
                        file.writelines(lines)
                    print('Password changed.')
                    return  # Exit the function after successful change
                else:
                    print('Current password is invalid.')
                    return  # Exit if the current password is incorrect
            else:
                print('Invalid entry in password file.')
                return  # Exit if the line format is unexpected

    # If the user is not found in the file, inform the user
    print('User not found.')

# If the script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Specify the password file name
    passwd_file = 'passwd.txt'

    # Prompt the user for their username and passwords
    username = input('User: ')
    current_password = getpass.getpass('Current Password: ')
    new_password = getpass.getpass('New Password: ')
    confirm_password = getpass.getpass('Confirm: ')

    # Ensure the new password matches the confirmation
    if new_password == confirm_password:
        # Call the change_password function to attempt the password change
        change_password(username, current_password, new_password, passwd_file)
    else:
        print('Passwords do not match.')
