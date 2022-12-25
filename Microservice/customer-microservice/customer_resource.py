import pymysql


class CustomerResource:

    def __int__(self):
        pass

    @staticmethod
    def get_connection():
        conn = pymysql.connect(
            # LOCAL
            # host="localhost",
            # port=3306,
            # user="root",
            # password="dbuserdbuser",
            # cursorclass=pymysql.cursors.DictCursor,
            # autocommit=True

            # AWS
            host="customerdb.cvjaygaiwg1r.us-east-1.rds.amazonaws.com",
            port=3306,
            user="admin",
            password="dbuserdbuser",
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

        return result

    @staticmethod
    def create_customer(customer):
        placeholder = ", ".join(["%s"] * len(customer))
        sql = "INSERT INTO customerDB.customer({columns}) VALUES ({values})".format(columns=",".join(customer.keys()),
                                                                                    values=placeholder)
        conn = CustomerResource.get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, list(customer.values()))
        result = cur.fetchone()

        return result

    @staticmethod
    def update_customer(customer):
        sql = "UPDATE customerDB.customer SET emailID=%s username=%s firstname=%s lastname=%s phone=%s"
        conn = CustomerResource.get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, [customer["emailID"],
                                customer["username"],
                                customer["firstname"],
                                customer["lastname"],
                                customer["phone"]])
        result = cur.fetchone()

        return result
