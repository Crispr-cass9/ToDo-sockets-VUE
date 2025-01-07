import socket, json, os
import smtplib, ssl
from modulesPython.my_logging import create_logger
from modulesPython.http_header_builder import HttpProtocolBuilder, HttpProtocolFactory

db_logger = create_logger('db_logger')

HOST = '127.0.0.1'
PORT = 65432

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
    dbConection.close()
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
    completeRequest = conn.recv(4096).decode('utf-8')
    print('La request es la siguiente:', completeRequest)
    firstLineRequest = completeRequest.split('\r\n')[0]
    method = firstLineRequest.split(' ')[0]
    route = firstLineRequest.split(' ')[1]

    if method == 'POST' and route=='/iniciar-sesion':
        httpResponse = HttpProtocolFactory.http_ok_origin('application',
                                                            'json',
                                                            'http://localhost:5173'
                                                        )

        httpResponse += '{"status": "Ok"}'
        print(httpResponse)

        conn.send(httpResponse.encode())
        conn.close()
