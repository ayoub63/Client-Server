import socket

def client_to_load():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try: 
            client_socket.connect("localhost" , port)

            server= input("Geben sie den Server ein: ")
            message = input("Nachricht: ")
            http_method = input("HTTP-Method: ")

            if not server:
                print("Fehler: Server ist erforderlich.")
            if not server_port_input:
                print("Fehler: Server-Portnummer ist erforderlich.")
            if not http_method:
                print("Fehler: HTTP-Methode ist erforderlich.")
            if not message:
                print("Fehler: Nachricht ist erforderlich.")

            payload = f"{http_method} / HTTP/1.1\r\nHost: {server}\r\n\r\n{message}"

            client_socket.sendall(payload.encode("utf-8"))
        except ConnectionRefusedError as e:
            print("connection client refused," , e)
        

            antwort = client_socket.recv(1024).decode("utf-8")