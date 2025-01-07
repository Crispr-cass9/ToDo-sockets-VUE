"""
Este módulo permite construir protocolos HTTP de forma flexible mediante el uso del patrón de diseño Builder y el patrón Factory.
Ofrece clases para gestionar excepciones personalizadas, construir headers HTTP y crear configuraciones comunes de protocolos HTTP.
"""
if __name__ == '__main__':
    print('Este archivo python ha sido creado para ser utilizado como módulo, no como archivo principal')
else:

    class ErrorCreator(Exception):
        """
        Clase para crear instancias personalizadas de excepciones, 
        utilizada para gestionar errores específicos durante la creación de protocolos HTTP.

        Attributes:
            error_name (str): Nombre del error.
            message (str): Descripción del error.
        """
        def __init__(self, error_name, message):
            self.message = message
            self.error_name = error_name

        def __str__(self):
            return f'{self.error_name}: {self.message}'


    class HttpProtocolBuilder():
        """
        Clase para construir protocolos HTTP personalizados utilizando el patrón Builder.
        Proporciona métodos para agregar códigos de estado, encabezados de control de caché y cookies.

        Attributes:
            header (str): El encabezado HTTP construido.
            has_status (bool): Indica si ya se ha agregado un código de estado.
        """
        def __init__(self):
            """
            Inicializa una instancia del constructor HTTP con encabezado vacío y sin códigos de estado establecidos.
            """
            self.header = ''
            self.has_status = False

        def add_ok_status(self):
            """
            Agrega un código de estado HTTP 200 Ok al encabezado.

            Raises:
                ErrorCreator: Si ya se ha agregado un código de estado previamente.

            Returns:
                HttpProtocolBuilder: Instancia actual para permitir encadenamiento.
            """
            if self.has_status:
                raise ErrorCreator('MultipleStatusError', 'El encabezado HTTP ya tiene un código de estado.')
            self.header += 'HTTP/1.1 200 Ok\r\n'
            self.has_status = True
            return self

        def add_created_status(self):
            """
            Agrega un código de estado HTTP 201 Created al encabezado.

            Raises:
                ErrorCreator: Si ya se ha agregado un código de estado previamente.

            Returns:
                HttpProtocolBuilder: Instancia actual para permitir encadenamiento.
            """
            if self.has_status:
                raise ErrorCreator('MultipleStatusError', 'El encabezado HTTP ya tiene un código de estado.')
            self.header += 'HTTP/1.1 201 Created\r\n'
            self.has_status = True
            return self

        def add_no_content_status(self):
            """
            Agrega un código de estado HTTP 204 No Content al encabezado.

            Raises:
                ErrorCreator: Si ya se ha agregado un código de estado previamente.

            Returns:
                HttpProtocolBuilder: Instancia actual para permitir encadenamiento.
            """
            if self.has_status:
                raise ErrorCreator('MultipleStatusError', 'El encabezado HTTP ya tiene un código de estado.')
            self.header += 'HTTP/1.1 204 No Content\r\n'
            self.has_status = True
            return self

        def add_moved_permanently_status(self, location):
            """
            Agrega un código de estado HTTP 301 Moved Permanently al encabezado con la URL de ubicación especificada.

            Args:
                location (str): La URL a donde se redirige permanentemente.

            Raises:
                ErrorCreator: Si ya se ha agregado un código de estado previamente.

            Returns:
                HttpProtocolBuilder: Instancia actual para permitir encadenamiento.
            """
            if self.has_status:
                raise ErrorCreator('MultipleStatusError', 'El encabezado HTTP ya tiene un código de estado.')
            self.header += f'HTTP/1.1 301 Moved Permanently\r\nLocation: {location}\r\n'
            self.has_status = True
            return self

        def add_bad_request_status(self):
            """
            Agrega un código de estado HTTP 400 Bad Request al encabezado.

            Raises:
                ErrorCreator: Si ya se ha agregado un código de estado previamente.

            Returns:
                HttpProtocolBuilder: Instancia actual para permitir encadenamiento.
            """
            if self.has_status:
                raise ErrorCreator('MultipleStatusError', 'El encabezado HTTP ya tiene un código de estado.')
            self.header += 'HTTP/1.1 400 Bad Request\r\n'
            self.has_status = True
            return self

        def add_unauthorized_status(self):
            """
            Agrega un código de estado HTTP 401 Unauthorized al encabezado.

            Raises:
                ErrorCreator: Si ya se ha agregado un código de estado previamente.

            Returns:
                HttpProtocolBuilder: Instancia actual para permitir encadenamiento.
            """
            if self.has_status:
                raise ErrorCreator('MultipleStatusError', 'El encabezado HTTP ya tiene un código de estado.')
            self.header += 'HTTP/1.1 401 Unauthorized\r\n'
            self.has_status = True
            return self

        def add_forbidden_status(self):
            """
            Agrega un código de estado HTTP 403 Forbidden al encabezado.

            Raises:
                ErrorCreator: Si ya se ha agregado un código de estado previamente.

            Returns:
                HttpProtocolBuilder: Instancia actual para permitir encadenamiento.
            """
            if self.has_status:
                raise ErrorCreator('MultipleStatusError', 'El encabezado HTTP ya tiene un código de estado.')
            self.header += 'HTTP/1.1 403 Forbidden\r\n'
            self.has_status = True
            return self

        def add_not_found_status(self):
            """
            Agrega un código de estado HTTP 404 Not Found al encabezado.

            Raises:
                ErrorCreator: Si ya se ha agregado un código de estado previamente.

            Returns:
                HttpProtocolBuilder: Instancia actual para permitir encadenamiento.
            """
            if self.has_status:
                raise ErrorCreator('MultipleStatusError', 'El encabezado HTTP ya tiene un código de estado.')
            self.header += 'HTTP/1.1 404 Not Found\r\n'
            self.has_status = True
            return self

        def cache_add_no_cache(self):
            """
            Agrega la cabecera Cache-Control con la directiva no-cache.

            Raises:
                ErrorCreator: Si no se ha establecido previamente un código de estado.

            Returns:
                HttpProtocolBuilder: Instancia actual para permitir encadenamiento.
            """
            if not self.has_status:
                raise ErrorCreator('NoHttpStatusError',
                                   'Intentas añadir una cabecera antes de añadir un código de estado.')
            self.header += 'Cache-Control: no-cache\r\n'
            return self

        def cache_add_no_store(self):
            """
            Agrega la cabecera Cache-Control con la directiva no-store.

            Raises:
                ErrorCreator: Si no se ha establecido previamente un código de estado.

            Returns:
                HttpProtocolBuilder: Instancia actual para permitir encadenamiento.
            """
            if not self.has_status:
                raise ErrorCreator('NoHttpStatusError',
                                   'Intentas añadir una cabecera antes de añadir un código de estado.')
            self.header += 'Cache-Control: no-store\r\n'
            return self

        def cache_add_must_revalidate(self):
            """
            Agrega la cabecera Cache-Control con la directiva must-revalidate.

            Raises:
                ErrorCreator: Si no se ha establecido previamente un código de estado.

            Returns:
                HttpProtocolBuilder: Instancia actual para permitir encadenamiento.
            """
            if not self.has_status:
                raise ErrorCreator('NoHttpStatusError',
                                   'Intentas añadir una cabecera antes de añadir un código de estado.')
            self.header += 'Cache-Control: must-revalidate\r\n'
            return self

        def add_cookie(self, cookies_dictionary):
            """
            Agrega cookies al encabezado HTTP a partir de un diccionario.

            Args:
                cookies_dictionary (dict): Diccionario donde las claves son nombres de cookies 
                                            y los valores son sus respectivos contenidos.

            Raises:
                ErrorCreator: Si no se ha establecido previamente un código de estado.

            Returns:
                HttpProtocolBuilder: Instancia actual para permitir encadenamiento.
            """
            if not self.has_status:
                raise ErrorCreator('NoHttpStatusError', 'No has añadido un status al protocolo HTTP')
            
            for key, value in cookies_dictionary.items():
                self.header+= f'Set-Cookie: {key}={value}; Path=/; Max-Age=3600\r\n'
            
            return self

        def add_mime_type(self, mime_type, subtype):
            """
            Agrega un tipo mime al protocolo HTTP.

            Args:
                mime_type (string): String que indica el tipo mime principal del elemento a enviar
                subtype (string): Indica el subtipo de tipo de dato a enviar 

            Raises:
                ErrorCreator: Si no se ha establecido previamente un código de estado.

            Returns:
                HttpProtocolBuilder: Instancia actual para permitir encadenamiento.
            """
            if not self.has_status:
                raise ErrorCreator('NoHttpStatusError', 'No has añadido un status al protocolo HTTP')

            self.header+= f'Content-Type: {mime_type}/{subtype}\r\n'
            return self
        
        def add_allow_origin(self, origin):
            """
            Agrega un dominio para que pueda permitir su origen y evitar el error de CORS

            Args:
                origin (string): Indica el dominio de la página web a aceptar

            Raises:
                ErrorCreator: Si no se ha establecido previamente un código de estado.

            Returns:
                HttpProtocolBuilder: Instancia actual para permitir encadenamiento.
            """
            if not self.has_status:
                raise ErrorCreator('NoHttpStatusError', 'No has añadido un status al protocolo HTTP')

            self.header+= f'Access-Control-Allow-Origin: {origin}\r\n'
            self.header += 'Access-Control-Allow-Credentials: true\r\n'
            return self
            
            
        def obtain_http_headers(self):
            """
                Retorna la cabecera HTTP completa creada.

                Returns:
                    str: String con las cabeceras HTTP completas.

                Raises:
                    ErrorCreator: Si no se ha añadido un estado HTTP antes de la obtención.
            """
            if not self.has_status:
                raise ErrorCreator('NoHttpStatusError',
                'Estas intentando extraer el protocolo http sin añadir un status')
            return self.header + '\r\n\r\n'
    
class HttpProtocolFactory():
    """
        Esta clase implementa el metodo factory para crear las cabeceras HTTP más comúnes
    """

    def __init__(self):
        pass

    @classmethod
    def http_ok(cls, mime_type, subtype):
        """
        Este método devuelve un string con el protocolo HTTP necesario para indicar 
        que la petición ha ido bien

        Returns:
            String con protocolo Http 200 Ok
        """
        return HttpProtocolBuilder().add_ok_status().add_mime_type(mime_type, subtype).obtain_http_headers()

    @classmethod
    def http_not_found(cls):
        """
        Este método devuelve un string con el protocolo HTTP necesario para indicar 
        que la petición no ha ido bien porque no se ha encontrado (404 not found)

        Returns:
            String con protocolo Http 404 Not Found
        """
        return HttpProtocolBuilder().add_not_found_status().obtain_http_headers()

    @classmethod
    def http_ok_cookies(cls, mime_type, subtype, cookie_dict):
        """
    Este método construye y devuelve una cabecera HTTP para una respuesta 200 OK, 
    con soporte para especificar el tipo MIME y añadir cookies.

    Args:
        mime_type (str): El tipo MIME del contenido (por ejemplo, "text").
        subtype (str): El subtipo del contenido (por ejemplo, "html").
        cookie_dict (dict): Un diccionario donde las claves son los nombres 
                            de las cookies y los valores son los datos correspondientes.

    Returns:
        str: String que contiene el protocolo HTTP con el estado 200 OK, 
             encabezados MIME y las cookies añadidas.
    
    Raises:
        ErrorCreator: Si ocurre algún error al intentar agregar un encabezado
                      antes de agregar el estado o si las cookies no se pueden configurar.
    """
        return HttpProtocolBuilder().add_ok_status()\
        .add_cookie(cookie_dict)\
        .add_mime_type(mime_type, subtype)\
        .obtain_http_headers()

    @classmethod
    def http_ok_cookies_origin(cls, mime_type, subtype, origin, cookie_dict):
        """
    Este método construye y devuelve una cabecera HTTP para una respuesta 200 OK, 
    con soporte para especificar el tipo MIME, habilitar solicitudes de dominios externos (CORS) 
    y añadir cookies.

    Args:
        mime_type (str): El tipo MIME del contenido (por ejemplo, "text").
        subtype (str): El subtipo del contenido (por ejemplo, "html").
        origin (str): El dominio que estará permitido para realizar peticiones (CORS).
        cookie_dict (dict): Un diccionario donde las claves son los nombres 
                            de las cookies y los valores son los datos correspondientes.

    Returns:
        str: String que contiene el protocolo HTTP con el estado 200 OK, 
             encabezados MIME, el origen permitido y las cookies añadidas.

    Raises:
        ErrorCreator: Si ocurre algún error al intentar agregar un encabezado 
                      antes de agregar el estado, o si las cookies no se pueden configurar.
        """

        return HttpProtocolBuilder().add_ok_status()\
        .add_mime_type(mime_type, subtype)\
        .add_allow_origin(origin)\
        .add_cookie(cookie_dict)\
        .obtain_http_headers()

    @classmethod
    def http_ok_origin(cls, mime_type, subtype, origin):
        """
    Este método construye y devuelve una cabecera HTTP para una respuesta 200 OK, 
    con soporte para especificar el tipo MIME, habilitar solicitudes de dominios externos (CORS).

    Args:
        mime_type (str): El tipo MIME del contenido (por ejemplo, "text").
        subtype (str): El subtipo del contenido (por ejemplo, "html").
        origin (str): El dominio que estará permitido para realizar peticiones (CORS).


    Returns:
        str: String que contiene el protocolo HTTP con el estado 200 OK, 
             encabezados MIME, el origen permitido

    Raises:
        ErrorCreator: Si ocurre algún error al intentar agregar un encabezado 
                      antes de agregar el estado.
        """

        return HttpProtocolBuilder().add_ok_status()\
        .add_mime_type(mime_type, subtype)\
        .add_allow_origin(origin)\
        .obtain_http_headers()