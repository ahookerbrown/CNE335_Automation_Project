# Adam Hooker-Brown
# CNE 335 Final Project
from Server import Server

def print_program_info():
    print("Server Automator v0.1 by Adam Hooker-Brown")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    server = Server("44.246.248.208")
    server.ping()
