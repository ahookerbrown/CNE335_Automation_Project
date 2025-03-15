import os
import time

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        self.server_ip = server_ip

    def ping(self):
        while True:
            os.system(f"ping -n 5 {self.server_ip}")
            time.sleep(5)