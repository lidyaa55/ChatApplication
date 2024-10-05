import socket
import threading
import json 


# Define ANSI color codes
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_BLUE = "\033[94m"
COLOR_RESET = "\033[0m"

# Function to get color for each username
def get_color_for_username(username):
    colors = [COLOR_RED, COLOR_GREEN, COLOR_YELLOW, COLOR_BLUE]
    return colors[hash(username) % len(colors)]



# Initialize the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 7072))
server.listen()

clients = []
usernames = {}

# Function to handle each client
def handle_client(client):
    while True:
        try:
            # Receive the username from the client
            username = client.recv(1024).decode('utf-8')
            usernames[client] = username  # Store the username

            while True:
                message_data = client.recv(1024)
                if message_data:
                    # Decode the JSON data
                    data = json.loads(message_data.decode('utf-8'))
                    username = data['username']
                    message = data['message']
                    
                    # Format the message with a timestamp and color-coded username
                    formatted_message = f"\n{get_color_for_username(username)}{username}{COLOR_RESET}:{message}"
                    broadcast(formatted_message.encode('utf-8'), client)
        except:
            del usernames[client]
            break

# Function to broadcast messages to all connected clients
def broadcast(message, current_client):
    for client in clients:
        if client != current_client:
            client.send(message)

# Main server loop to accept clients
while True:
    client, address = server.accept()
    print(f"Connected with {str(address)}")

    clients.append(client)

    # Start a new thread for each client
    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()
