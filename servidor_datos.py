import socket, json, os
import sqlite3, smtplib, ssl
from modulesPython.my_logging import create_logger
from modulesPython.http_header_builder import HttpProtocolBuilder

db_logger = create_logger('db_logger')

http = HttpProtocolBuilder().add_created_status().add_ok_status().obtain_http_headers()
print(http)


HOST = '127.0.0.1'  # Dirección del servidor
PORT = 65432         # Puerto para el servidor JSON

CABECERAHTTPOK= 'HTTP/1.1 200 OK'

try:
    dbConection = sqlite3.connect('gestor_tareas.db')
    dbConection.execute('''CREATE TABLE usuarios(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT,
               apellidos TEXT,
               correo TEXT,
               contrasenya TEXT,
               listaTareas TEXT
               );''')
except sqlite3.OperationalError as e:
    msg = f'Ha ocurrido un error al inicializar la base de datos: {e}'
    db_logger.debug(msg)



# Datos de usuarios
users = [
    {"id": 1, "nombre": "Alice", "edad": 25},
    {"id": 2, "nombre": "Bob", "edad": 30},
    {"id": 3, "nombre": "Charlie", "edad": 35},
    {"id": 4, "nombre": "Diana", "edad": 28},
    {"id": 5, "nombre": "Eve", "edad": 32}
]

# Crear el socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Servidor JSON escuchando en http://{HOST}:{PORT}")
print('El PID del proceso es el siguiente: ', os.getpid())


while True:
    conn, addr = server_socket.accept()
    completeRequest = conn.recv(1024).decode('utf-8')
    firstLineRequest = completeRequest.split('/r/n')[0]
    method = firstLineRequest.split(' ')[0]
    route = firstLineRequest.split(' ')[1]
    print(method, route, '\n\n\n', completeRequest)

    if method == 'POST' and route=='/iniciar-sesion':
        httpResponse = CABECERAHTTPOK + '''Content-Type: application/json
Access-Control-Allow-Origin: http://localhost:5173
Access-Control-Allow-Credentials: true




{status: ok, data: saved}
'''
        conn.sendall(httpResponse.encode('utf-8'))

    conn.close()


# Access-Control-Allow-Origin: http://127.0.0.1:65431
# Access-Control-Allow-Credentials: true


#      if "GET /" in request:
#         # Responder con JSON
#         response_body = json.dumps(users)
#         response = f"""\
# HTTP/1.1 200 OK
# Content-Type: application/json
# Access-Control-Allow-Origin: http://localhost:5173
# Access-Control-Allow-Credentials: true