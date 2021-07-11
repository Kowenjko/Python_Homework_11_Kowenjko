import psycopg2
from settings import *

connection = psycopg2.connect(user=USER,
                              password=PASSWORD,
                              host=HOST,
                              port=PORT,
                              database='shop_db')
cursor = connection.cursor()
cursor.execute('')

class Admin:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def add_product(self):
        pass

    def add_pr_category(self):
        pass

    def employee(self):
        pass

    def delete_product(self):
        pass

    def delete_pr_category(self):
        pass

    def delete_employee(self):
        pass

    def delete_customer(self):
        pass

    def edit_product(self):
        pass

    def edit_pr_category(self):
        pass

    def edit_employee(self):
        pass

    def get_order_info(self):
        pass
