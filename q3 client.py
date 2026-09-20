import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect(("localhost", 5000))

    message = "Hello from client!"

    client_socket.send(message.encode())

    print("Message sent successfully.")

except socket.error as error:
    print("Network error:", error)

finally:
    client_socket.close()
