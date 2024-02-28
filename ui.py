# ui.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# NAME
# EMAIL
# STUDENT ID

import ds_client

class Profile:
    def __init__(self, username, password, bio, dspserver):
        self.username = username
        self.password = password
        self.bio = bio
        self.dspserver = dspserver

    def save_profile(self, filename):
        with open(filename, 'w') as f:
            f.write(f"username={self.username}\n")
            f.write(f"password={self.password}\n")
            f.write(f"bio={self.bio}\n")
            f.write(f"dspserver={self.dspserver}\n")

def run():
    print("Welcome to the journal program!")
    print("Type 'admin' to enter admin mode or any other key to start.")
    choice = input("Choice: ")
    if choice.strip().lower() == "admin":
        admin_mode()
    else:
        user_mode()

def admin_mode():
    while True:
        command = input("Admin command: ")
        process_admin_command(command)

def user_mode():
    print("Journal Menu:")
    print("1. Create a new journal")
    print("2. Load an existing journal")
    print("3. Post entry to DSP server")
    print("4. Exit")
    choice = input("Choice: ")
    if choice == "1":
        create_journal()
    elif choice == "2":
        load_journal()
    elif choice == "3":
        post_entry()
    elif choice == "4":
        exit()
    else:
        print("Invalid choice")

def create_journal():
    while True:
        directory = input("Enter directory to create journal in: ")
        name = input("Enter journal name: ")
        filename = os.path.join(directory, name + ".dsu")
        
        if os.path.exists(filename):
            print("Journal already exists. Please choose a different name or directory.")
            continue
        
        username = input("Enter username: ")
        password = input("Enter password: ")
        bio = input("Enter bio: ")
        dspserver = input("Enter DSP server IP address: ")
        
        if not all([directory, name, username, password, bio, dspserver]):
            print("All fields are required. Please try again.")
            continue
        
        profile = Profile(username, password, bio, dspserver)
        profile.save_profile(filename)
        
        print("Journal created successfully.")
        break

def load_journal(filename=None):
    if filename is None:
        filename = input("Enter path to journal file: ")
    if os.path.exists(filename):
        print("Journal loaded successfully.")
    else:
        print("Journal file not found.")

def post_entry():
    filename = input("Enter path to journal file: ")
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
            username = lines[0].strip().split('=')[1]
            password = lines[1].strip().split('=')[1]
            bio = lines[2].strip().split('=')[1]
            dspserver = lines[3].strip().split('=')[1]

        message = input("Enter message to post: ")

        # Replace these values with server IP address and port
        server = dspserver
        port = 8080

        success = ds_client.send(server, port, username, password, message, bio)
        if success:
            print("Entry posted successfully.")
        else:
            print("Failed to post entry.")
    else:
        print("Journal file not found.")

def process_admin_command(command):
    command_parts = command.split()
    action = command_parts[0].upper()

    if action == 'Q':
        print("Quitting admin mode.")
        return

    if action == 'C':
        ui.create_journal()
    elif action == 'O':
        if len(command_parts) > 1:
            filename = command_parts[1]
            ui.load_journal(filename)
        else:
            print("Invalid command. Usage: O [filename]")
    else:
        print("Invalid admin command.")

if __name__ == "__main__":
    run()
