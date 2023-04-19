import logging
import psycopg2
from datetime import datetime, timedelta
import os

# Configuración de registro
# quiero que el nombre tenga fecha y hora y el nivel de log Critical o Error

filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '--CRITICAL' + '.log'
filename_path = os.path.join(os.path.dirname(__file__), 'logs', filename)
logging.basicConfig(filename=filename_path, level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Configuración de conexión a la base de datos
DB_HOST = 'crypto-gym-production.cjreo3vfmhsh.us-east-2.rds.amazonaws.com'
DB_NAME = 'cryptoGym'
DB_USER = 'postgres'
DB_PASSWORD = '12345678'

# Conectar a la base de datos y ejecutar una consulta simple
try:
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cur = conn.cursor()
    cur.execute('SELECT 1')
    result = cur.fetchone()
    cur.close()
    conn.close()
    logging.info('La base de datos está activa')
except Exception as e:
    logging.critical('Error al conectarse a la base de datos: {}'.format(str(e)))

# me puedes recomendar mas tests que puedo hacer en cuanto al servidor

def test_db_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cur = conn.cursor()
        cur.execute('SELECT 1')
        result = cur.fetchone()
        cur.close()
        conn.close()
        logging.info('La base de datos está activa')
    except Exception as e:
        logging.critical('Error al conectarse a la base de datos: {}'.format(str(e)))

def test_server_internet():
    try:
        response = os.system("ping -c 1 " + DB_HOST)
        if response == 0:
            logging.info('El servidor está activo')
        else:
            logging.critical('El servidor no está activo')
    except Exception as e:
        logging.critical('Error al conectarse al servidor: {}'.format(str(e)))

def check_disk_space():
    try:
        disk = os.statvfs('/')
        free = disk.f_bavail * disk.f_frsize
        total = disk.f_blocks * disk.f_frsize
        used = (disk.f_blocks - disk.f_bfree) * disk.f_frsize
        logging.info('Espacio libre: {} GB'.format(free / 1024 / 1024 / 1024))
        logging.info('Espacio total: {} GB'.format(total / 1024 / 1024 / 1024))
        logging.info('Espacio usado: {} GB'.format(used / 1024 / 1024 / 1024))
    except Exception as e:
        logging.critical('Error al verificar el espacio en disco: {}'.format(str(e)))


if __name__ == '__main__':
    test_db_connection()
    test_server_internet()
    # check_disk_space()