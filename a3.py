# a3.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Kellan Yamamoto
# kellany@uci.edu
# 28388886

from ds_client import *
from ds_protocol import *
from Profile import *
from ui import *

if __name__ == "__main__":
    server = "168.235.86.101"
    port = 3021
    username = "kellany"
    password = "Kellan2"
    message = "Hello World!"
    bio = "Kellan"
    send(server, port, username, password, message, bio)
    run()
    
    