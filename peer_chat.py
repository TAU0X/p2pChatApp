import socket
import threading
import tkinter as tk
from tkinter import messagebox

# Common global variable to share the socket
connection = None

# Function to receive messages from peer
def receive_messages(sock, text_area):
    while True:
        try:
            message = sock.recv(1024).decode()
            if not message:
                text_area.insert(tk.END, "\n[Connection closed]\n")
                break
            text_area.insert(tk.END, f"\nPeer: {message}\nYou: ")
        except Exception as ex:
            text_area.insert(tk.END, f"\n[!] Error receiving message: {ex}\n")
            break

# Function to send messages to peer
def send_message(sock, message_entry, text_area):
    msg = message_entry.get()
    if msg.lower() == "exit":
        text_area.insert(tk.END, "\n[Exiting chat]\n")
        sock.close()
        message_entry.delete(0, tk.END)
        return
    try:
        sock.send(msg.encode())
        text_area.insert(tk.END, f"You: {msg}\n")
    except Exception as ex:
        text_area.insert(tk.END, f"[!] Failed to send message: {ex}\n")
    message_entry.delete(0, tk.END)

# Mode selection (server or client)
def start_chat():
    mode = mode_var.get().strip().lower()

    # Server mode
    if mode == "server":
        host = "0.0.0.0"
        port = int(port_entry.get())
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((host, port))
            server.listen(1)
            text_area.insert(tk.END, f"[Waiting for connection on port {port}]\n")
            global connection
            connection, addr = server.accept()
            text_area.insert(tk.END, f"[Connected to {addr}]\n")
        except Exception as e:
            messagebox.showerror("Error", f"Server failed: {e}")
            return

    # Client mode
    elif mode == "client":
        peer_ip = ip_entry.get().strip()
        peer_port = int(port_entry.get())
        try:
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection.connect((peer_ip, peer_port))
            text_area.insert(tk.END, f"[Connected to {peer_ip}:{peer_port}]\n")
        except Exception as e:
            messagebox.showerror("Error", f"Connection failed: {e}")
            return

    else:
        messagebox.showerror("Error", "Invalid mode. Choose 'server' or 'client'.")
        return

    # Start receiver thread
    threading.Thread(target=receive_messages, args=(connection, text_area), daemon=True).start()

# Set up the GUI window
root = tk.Tk()
root.title("Chat App")

# Set up UI elements
mode_var = tk.StringVar(value="server")

# Mode selection radio buttons
mode_frame = tk.Frame(root)
mode_frame.pack(pady=10)
tk.Radiobutton(mode_frame, text="Server", variable=mode_var, value="server").grid(row=0, column=0, padx=10)
tk.Radiobutton(mode_frame, text="Client", variable=mode_var, value="client").grid(row=0, column=1, padx=10)

# IP and Port entry fields
ip_label = tk.Label(root, text="Server IP (for client mode):")
ip_label.pack(pady=5)
ip_entry = tk.Entry(root)
ip_entry.pack(pady=5)

port_label = tk.Label(root, text="Port:")
port_label.pack(pady=5)
port_entry = tk.Entry(root)
port_entry.pack(pady=5)

# Text area for displaying chat messages
text_area = tk.Text(root, height=15, width=50, wrap=tk.WORD)
text_area.pack(pady=10)
text_area.config(state=tk.DISABLED)

# Message input field
message_entry = tk.Entry(root, width=40)
message_entry.pack(pady=5)

# Send button
send_button = tk.Button(root, text="Send", command=lambda: send_message(connection, message_entry, text_area))
send_button.pack(pady=10)

# Start chat button
start_button = tk.Button(root, text="Start Chat", command=start_chat)
start_button.pack(pady=10)

# Run the GUI loop
root.mainloop()
