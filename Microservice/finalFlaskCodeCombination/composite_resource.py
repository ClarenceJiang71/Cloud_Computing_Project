import os

import pymysql


class CompositeResource:

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
        # conn = pymysql.connect(
        #     # LOCAL
        #     # host="localhost",
        #     # port=3306,
        #     # user="root",
        #     # password="dbuserdbuser",
        #     # cursorclass=pymysql.cursors.DictCursor,
        #     # autocommit=True
        #
        #     # # AWS
        #     # host="customerdb.cvjaygaiwg1r.us-east-1.rds.amazonaws.com",
        #     # port=3306,
        #     # user="admin",
        #     # password="dbuserdbuser",
        #     # cursorclass=pymysql.cursors.DictCursor,
        #     # autocommit=True
        #
        #
        # )

        # return conn

    @staticmethod
    def get_composite_by_emailID(key):
        # sql1 查询 找到了 customer的信息 email, userName, lastName, firstName, phone
        sql1 = "SELECT * FROM customerDB.customer WHERE emailID=%s"
        # sql2 查询 找到 address的信息 street, aptNo, city, state, zip
        sql2 = "SELECT street, aptNo, city, state, zip FROM contacts.email join contacts.address on " \
               "contacts.email.accountID = contacts.address.accountID WHERE emailAddress = %s"
        conn = CompositeResource.get_connection()
        cur = conn.cursor()
        res = cur.execute(sql1, args=key)
        # 应该是json
        result1 = cur.fetchone()


        res = cur.execute(sql2, args=key)
        result2 = cur.fetchone()

        print({**result1, **result2})
        return {**result1, **result2}

    # @staticmethod
    # def delete_customer_by_emailID(key):
    #     sql = "DELETE FROM customerDB.customer WHERE emailID=%s"
    #     conn = CustomerResource.get_connection()
    #     cur = conn.cursor()
    #     res = cur.execute(sql, args=key)
    #     result = cur.fetchone()
    #
    #     return res
    #
    # @staticmethod
    # def create_customer(customer):
    #     placeholder = ", ".join(["%s"] * len(customer))
    #     # sql = "INSERT INTO customerDB.customer ({columns}) VALUES ({values});".format(columns=",".join(customer.keys()),
    #     #                                                                             values=placeholder)
    #     sql = "insert into {table} ({columns}) values ({values});".format(table='customerDB.customer',
    #                                                                          columns=",".join(customer.keys()),
    #                                                                          values=placeholder)
    #     print(sql)
    #     conn = CustomerResource.get_connection()
    #     cur = conn.cursor()
    #     res = cur.execute(sql, list(customer.values()))
    #     result = cur.fetchone()
    #
    #     return res
    #
    # @staticmethod
    # def update_customer(customer):
    #     sql = "UPDATE customerDB.customer SET username=%s, firstname=%s, lastname=%s, phone=%s where emailID = %s "
    #     conn = CustomerResource.get_connection()
    #     cur = conn.cursor()
    #     res = cur.execute(sql, [
    #                             customer["username"],
    #                             customer["firstname"],
    #                             customer["lastname"],
    #                             customer["phone"],
    #                             customer["emailID"]
    #                             ])
    #     result = cur.fetchone()
    #
    #     return res
