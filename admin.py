import psycopg2
from settings import *


class Admin():

    def __init__(self, login, password):
        self.login = login
        self.password = password

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
