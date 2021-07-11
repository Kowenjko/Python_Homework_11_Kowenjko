import psycopg2
from settings import *

connection = psycopg2.connect(user=USER,
                              password=PASSWORD,
                              host=HOST,
                              port=PORT,
                              database='shop_db')
cursor = connection.cursor()
cursor.execute('')

class UnregisteredCuctomer:

    def register(self):
        pass

    def get_product_info(self):
        pass
