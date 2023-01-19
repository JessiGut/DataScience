import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


# Connect to an existing database
conn = psycopg2.connect(database="", user='', password='',
                        host='', port=5432)

conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Open a cursor to perform database operations
cur = conn.cursor()


def insertDB(vivienda, ubicacion, temperatura, time):
    try:
        cur.execute("INSERT INTO iot VALUES (%s, %s, %s, %s)",
                    (vivienda, ubicacion, temperatura, time))
    except psycopg2.Error as e:
        print('Error Insertar dato: %s', str(e))