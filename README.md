Peer-to-Peer Chat Application Using Client-Server Model


Introduction

In today’s digital world, real-time communication plays a vital role in education, business, and social interaction. This project demonstrates a network software application that enables text-based communication between two users in real time using the client-server model. The program is implemented using Python and the Tkinter library for GUI. It aims to simulate basic functionalities of a chat system, including message sending and receiving, with a user-friendly interface

 
Tools Used

1-	Programming Language: Python 3
2-	Socket Library: For establishing TCP connections
3-	Tkinter Library: For GUI development
4-	Threading Module: To allow concurrent message receiving without freezing the interface
 
Problem Statement

Many students face difficulties using complex communication platforms, especially when it comes to privacy or internet restrictions. The goal of this project is to design a simple peer-to-peer chat system that:
•	It is lightweight and easy to use.
•	Does not rely on third-party servers.
•	Can be used on local networks for quick communication


System Architecture:

The application follows a Client-Server Model. It operates in two modes:
1-	Server Mode: Listens for incoming connections on a specified port.
2-	Client Mode: Connects to the server using its IP and port.
3-	Once the connection is established, both users can send and receive messages. The receiving process is handled by a separate thread to keep the GUI responsive
 
Features:

1-	Two-way communication between two users
2-	Mode selection (client or server)
3-	Custom IP and port input
4-	Basic error handling and exit command
5-	GUI interface with real-time updates


Explanation of the Code:

1-	Sockets are used to create and manage network connections.
2-	Threading allows the app to receive messages in the background.
3-	Tkinter provides a simple interface where users can type and view messages.
start_chat() initializes the connection based on the chosen mode.
send_message() and receive_messages() manage data exchange.


Testing and Results:

The application was tested on two machines connected over the same network. It successfully allowed real-time chat with minimal latency. The interface was responsive, and users were able to switch modes between server and client


Conclusion:

This project illustrates how basic concepts of networking and GUI development can be combined to create a functional chat application. The implementation serves as a foundation for more complex systems, such as group chats, file sharing, or encrypted messaging.


Challenges faced during development:

•	The firewall prevented the connection
•	The IP were too different meaning the connection came from different routers
•	Python Not Recognized


Future Work:

•	Add support for multiple users
•	Implement file transfer
•	Add encryption for secure communication
•	Improve error handling and reconnection logic


