"""
Este módulo permite crear loggings de manera más rápida
"""
import logging
from logging.handlers import RotatingFileHandler

if __name__ == '__main__':
    print('Este archivo de python funciona como un módulo, no como archivo principal')
else:

    def create_logger(name):
        """
        Crea una instancia de logger con un StreamHandler y un RotatingFileHandler.

        Args:
            name (str): El nombre que se le asignará al logger y al archivo de log generado.

        Returns:
            logger: El logger configurado
        """
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        rotating_handler = RotatingFileHandler(
            name,
            maxBytes=4096,
            backupCount=5,
            encoding='utf-8',
        )
        rotating_handler.setLevel(logging.WARNING)

        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(name)s - %(message)s - %(filename)s:%(lineno)d'
        )

        stream_handler.setFormatter(formatter)
        rotating_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
        logger.addHandler(rotating_handler)

        return logger
