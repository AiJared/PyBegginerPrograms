# Use getpass to hide your password while typing instead of using python's input method which shows it.
from getpass import getpass

username = input("Enter username: ")
password = getpass("Enter password: ")
print(username)
print(password)