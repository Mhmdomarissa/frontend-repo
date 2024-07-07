
import os
from dotenv import load_dotenv

load_dotenv('../config.env')  

class Client:
    def __init__(self):
        self.server_ip = os.getenv('ServerIPAddress', '127.0.0.1')

    def connect(self):
        print(f"Connecting to server at {self.server_ip}")

if __name__ == "__main__":
    client = Client()
    client.connect()
