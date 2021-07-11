import psycopg2
from settings import *

connection = psycopg2.connect(user=USER,
                              password=PASSWORD,
                              host=HOST,
                              port=PORT,
                              database='shop_db')
cursor = connection.cursor()
cursor.execute('')

class Employee:

    def __init__(self, first_name, last_name, city, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.login = email
        self.password = password

    def edit_self_info(self):
        pass

    def create_order(self):
        pass

    def delete_order(self):
        pass

    def get_product_info(self):
        pass
