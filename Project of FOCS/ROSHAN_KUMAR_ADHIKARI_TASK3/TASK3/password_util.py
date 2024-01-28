# password_util.py

import hashlib

# Define a function to encrypt passwords using MD5 (for demonstration only)
def encrypt_password(password):
    """
    Encrypts a password using the MD5 hashing algorithm.
    Note: MD5 is not considered secure for password storage in production environments.

    Args:
        password (str): The password to encrypt.

    Returns:
        str: The encrypted password as a hexadecimal string.
    """

    # Encode the password as bytes and apply the MD5 hashing algorithm
    return hashlib.md5(password.encode()).hexdigest()

# Define a function to check if an entered password matches the stored encrypted password
def check_password(current_password, entered_password):
    """
    Checks if the entered password matches the stored encrypted password.

    Args:
        current_password (str): The encrypted password stored for the user.
        entered_password (str): The password entered by the user.

    Returns:
        bool: True if the passwords match, False otherwise.
    """

    # Encrypt the entered password and compare it to the stored encrypted password
    return encrypt_password(entered_password) == current_password
