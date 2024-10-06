# Overview

This Python chat application is a simple real-time messaging program that allows multiple clients to communicate through a server. It uses a client-server architecture where each client connects to a central server, sends messages, and receives messages from other clients.

[Software Demo Video] https://www.loom.com/share/56473642e90d4de6847c0344ab017a8b?sid=2efee2c2-4e5c-4eb5-88d2-514eabb93d1b

### How to Use

1. **Start the Server**:
   - Run `chat_server.py` to start the server. The server listens on port 7072 for incoming client connections.
2. **Start the Clients**:
   - Run `client.py` on multiple terminals or machines. Each client will be asked to enter a username and can start sending messages after connecting to the server.

### Purpose

The purpose of this software is to create a basic real-time chat system using network communication in Python. It demonstrates client-server architecture, socket programming, and threading to allow multiple users to chat simultaneously.

# Network Communication

### Architecture

This program uses a **client-server** architecture. One central server handles the communication between multiple clients.

### Protocol

- The program uses **TCP (Transmission Control Protocol)** for reliable data transmission.
- The default port number used for communication is **7072**.

### Message Format

Messages are exchanged between clients and the server in **JSON format**, containing two fields:

- **username**: The username of the client sending the message.
- **message**: The text of the message being sent.

---

# Development Environment

### Tools Used

- **IDE/Editor**:Basic text editor VS code
- **Platform**: Developed on Python 3.x.

### Programming Language

- **Python**: Used for socket programming and multithreading.
- **Libraries**:
  - `socket`: For network communication.
  - `threading`: To handle multiple clients simultaneously.
  - `json`: To format messages for easy reading and parsing.

# Useful Websites

{Make a list of websites that you found helpful in this project}

- [Web Site Name](http://url.link.goes.here)
- [Web Site Name](http://url.link.goes.here)

# Future Work

- **Item 1**: Improve message formatting for better readability (e.g., separating usernames and messages).
- **Item 2**: Add support for message encryption to enhance security.
- **Item 3**: Implement a user authentication system (login/register) to track users.
