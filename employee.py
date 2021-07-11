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

    def __init__(self, first_name, last_name, date_of_birth, city, chief, login, password):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.city = city
        self.chief = chief
        self.login = login
        self.password = password

    def edit_self_info(self):
        pass

    def change_order_status(self):
        pass
