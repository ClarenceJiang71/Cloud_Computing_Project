import os

import pymysql


class CustomerResource:

    def __int__(self):
        pass

    @staticmethod
    def get_connection():
        usr = os.environ.get("DBUSER")
        pw = os.environ.get("DBPW")
        h = os.environ.get("DBHOST")

        conn = pymysql.connect(
            user=usr,
            password=pw,
            host=h,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_customer_by_emailID(key):
        sql = "SELECT * FROM customerDB.customer WHERE emailID=%s"
        conn = CustomerResource.get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

    @staticmethod
    def delete_customer_by_emailID(key):
        sql = "DELETE FROM customerDB.customer WHERE emailID=%s"
        conn = CustomerResource.get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return res

    @staticmethod
    def create_customer(customer):
        placeholder = ", ".join(["%s"] * len(customer))
        # sql = "INSERT INTO customerDB.customer ({columns}) VALUES ({values});".format(columns=",".join(customer.keys()),
        #                                                                             values=placeholder)
        sql = "insert into {table} ({columns}) values ({values});".format(table='customerDB.customer',
                                                                             columns=",".join(customer.keys()),
                                                                             values=placeholder)
        print(sql)
        conn = CustomerResource.get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, list(customer.values()))
        result = cur.fetchone()

        return res

    @staticmethod
    def update_customer(customer):
        sql = "UPDATE customerDB.customer SET username=%s, firstname=%s, lastname=%s, phone=%s where emailID = %s "
        conn = CustomerResource.get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, [
                                customer["username"],
                                customer["firstname"],
                                customer["lastname"],
                                customer["phone"],
                                customer["emailID"]
                                ])
        result = cur.fetchone()

        return res
