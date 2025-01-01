"""
Este módulo posee una función creada con el patrón de diseño builder
para la creación de cabeceras http

"""
if __name__ == '__main__':
    print('Este archivo python ha sido creado para ser utilizado como módulo, no como archivo principal')
else:

    class ErrorCreator(Exception):
        """
        Esta clase permite crear instancias personalizadas de las 
        excepciones para crear errores personalizados
        """
        def __init__(self, error_name, message):
            self.message = message
            self.error_name = error_name
        
        def __str__(self):
            return f'{self.error_name}: {self.message}'


    class HttpProtocolBuilder():
        """
        Esta función permite crear el protocolo HTTP personalisable mediante distintos métodos
        """
        def __init__(self):
            self.header = ''
            self.has_status = False
        
        def add_ok_status(self):
            if self.has_status:
                raise ErrorCreator('MultipleStatusError', 'The HTTP header already had a status code')
            
            self.header += 'HTTP/1.1 200 Ok\r\n'
            self.has_status = True
            return self
        
        def add_created_status(self):
            if self.has_status:
                raise ErrorCreator('MultipleStatusError', 'The HTTP header already had a status code')

            self.header += 'HTTP/1.1 201 Created\r\n'
            self.has_status = True
            return self
        
        def add_no_content_status(self):
            if self.has_status:
                raise ErrorCreator('MultipleStatusError', 'The HTTP header already had a status code')

            self.header += 'HTTP/1.1 204 No Content\r\n'
            self.has_status = True
            return self
        
        def add_moved_permanently_status(self, location):
            if self.has_status:
                raise ErrorCreator('MultipleStatusError', 'The HTTP header already had a status code')

            self.header += f'HTTP/1.1 301 Moved Permanently\r\nLocation: {location}\r\n'
            self.has_status = True
            return self
        
        def add_bad_request_status(self):
            if self.has_status:
                raise ErrorCreator('MultipleStatusError', 'The HTTP header already had a status code')

            self.header += 'HTTP/1.1 400 Bad Request\r\n'
            self.has_status = True
            return self

        def add_unauthorized_status(self):
            if self.has_status:
                raise ErrorCreator('MultipleStatusError', 'The HTTP header already had a status code')

            self.header += 'HTTP/1.1 401 Unauthorized\r\n'
            self.has_status = True
            return self

        def add_forbidden_status(self):
            if self.has_status:
                raise ErrorCreator('MultipleStatusError', 'The HTTP header already had a status code')

            self.header += 'HTTP/1.1 403 Forbidden\r\n'
            return self
        
        def add_not_found_status(self):
            if self.has_status:
                raise ErrorCreator('MultipleStatusError', 'The HTTP header already had a status code')

            self.header += 'HTTP/1.1 404 Not Found\r\n'
            self.has_status = True
            return self

        

        def obtain_http_headers(self):
            return self.header + '\r\n\r\n'