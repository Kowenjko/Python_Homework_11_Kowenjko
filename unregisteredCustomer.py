import psycopg2
from settings import *


class UnregisteredCuctomer():
    @classmethod
    def _openDB(cls):
        connection = psycopg2.connect(user=USER, password=PASSWORD,
                                      host=HOST, port=PORT,
                                      database='shop_db')
        cursor = connection.cursor()
        return connection, cursor

    @classmethod
    def _closeDB(cls, connection, cursor):
        cursor.close()
        connection.close()

    def register(self):
        pass

    def get_product_info(self):
        pass
