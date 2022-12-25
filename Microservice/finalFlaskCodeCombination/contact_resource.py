import pymysql
import os


class ContactResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():
        usr = os.environ.get("DBUSER")
        PW = os.environ.get("DBPW")
        h = os.environ.get("DBHOST")

        conn = pymysql.connect(
            user=usr,
            password=PW,
            host=h,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    # This method use account ID as
    def get_by_key(table_name, key):

        sql = "SELECT * FROM contacts."+table_name+" where id=%s"
        conn = ContactResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

    @staticmethod
    def delete_by_key(key):
        sql = "Delete FROM contacts.address where id=%s"
        conn = ContactResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return res

    @staticmethod
    def add(address):
        placeholder = ", ".join(["%s"] * len(address))
        sql = "insert into {table} ({columns}) values ({values});".format(table='contacts.address',
                                                                          columns=",".join(address.keys()),
                                                                          values=placeholder)
        conn = ContactResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, list(address.values()))
        result = cur.fetchone()

        return res
    @staticmethod
    def update(address):
        sql = "update  contacts.address set accountID=%s, street=%s, aptNo=%s, city=%s, state=%s, zip=%s where id=%s"
        conn = ContactResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, [address['accountId'], address['street'], address['aptNo'], address['city'], address['state'], address['zip'],
                                address['id']])
        result = cur.fetchone()

        return res

    # @staticmethod
    # def get_by_union_info(key):
    #
    #     sql = "SELECT * FROM contacts.email join contacts.phone using (accountId) where accountId=%s"
    #     conn = ContactResource._get_connection()
    #     cur = conn.cursor()
    #     res = cur.execute(sql, args=key)
    #     result = cur.fetchone()
    #
    #     return result
    #
    # @staticmethod
    # def get_whole_table(table_name):
    #     sql = "SELECT * FROM contacts." + table_name
    #     conn = ContactResource._get_connection()
    #     cur = conn.cursor()
    #     res = cur.execute(sql)
    #     result = cur.fetchall()
    #
    #     return result
    #
    # @staticmethod
    # def get_pk(table_name):
    #     if table_name == "address":
    #         return "id"
    #     if table_name == "email":
    #         return "email_address"
    #     if table_name == "payment":
    #         return "cardNo"
    #     else:
    #         return "phoneNo"
    #
    # @staticmethod
    # def get_through_two_tables(start, pk, to):
    #     pk_name = ContactResource.get_pk(start)
    #     sql = "SELECT * FROM contacts." + to + " where accountId = (select accountId from contacts." + \
    #         start+" where " + pk_name + "=%s)"
    #     print(sql)
    #     conn = ContactResource._get_connection()
    #     cur = conn.cursor()
    #     res = cur.execute(sql, args=pk)
    #     result = cur.fetchall()
    #
    #     return result



