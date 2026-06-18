import logging
import os

# Obtener la ruta del directorio actual
ruta_logs = os.path.join(os.path.dirname(__file__), 'logs.txt')

# Obtener el logger raíz y limpiar handlers previos
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Limpiar handlers previos si los hay
for handler in logger.handlers[:]:
    logger.removeHandler(handler)

# Crear handler para archivo
file_handler = logging.FileHandler(ruta_logs, mode='a', encoding='utf-8')
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# Crear handler para consola
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)
