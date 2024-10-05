import socket
import threading
import json
import sys


# Define ANSI color codes for text formatting
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_BLUE = "\033[94m"
COLOR_RESET = "\033[0m"
CLEAR_LINE = "\033[K"  # Clears the current line

# Function to get color for each username
def get_color_for_username(username):
    colors = [COLOR_RED, COLOR_GREEN, COLOR_YELLOW, COLOR_BLUE]
    return colors[hash(username) % len(colors)]



# Function to receive messages from the server
def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')

            # Clear the current line before printing the received message
            sys.stdout.write("\r" + CLEAR_LINE)  # Clear the input line
            sys.stdout.flush()  # Ensure the terminal is updated

            print(message)  # Print the received message

            # Reprint the input prompt after receiving a message
            sys.stdout.write(f"Enter your message: ")
            sys.stdout.flush()  # Ensure the prompt is updated
        except:
            print("An error occurred!")
            client.close()
            break  

# Main client code
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 7072))

    # Get the username from the user
    username = input("Enter your username: ")

    # Start a thread to receive messages
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    def send_messages():
        while True:
            # Get the message from the user
            message = input(f"Enter your message: ")

            # Send the message to the server
            data = {'username': username, 'message': message}
            client.send(json.dumps(data).encode('utf-8'))

    # Send messages in the main thread
    send_messages()

if __name__ == "__main__":
    main()
