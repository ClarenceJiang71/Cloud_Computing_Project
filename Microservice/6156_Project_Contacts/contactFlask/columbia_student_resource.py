import pymysql
import os


class AccountResource:

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

        sql = "SELECT * FROM contacts."+table_name+" where accountId=%s"
        conn = AccountResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

    @staticmethod
    def get_by_union_info(key):

        sql = "SELECT * FROM contacts.email join contacts.phone using (accountId) where accountId=%s"
        conn = AccountResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

    @staticmethod
    def get_whole_table(table_name):
        sql = "SELECT * FROM contacts." + table_name
        conn = AccountResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        result = cur.fetchall()

        return result

    @staticmethod
    def get_pk(table_name):
        if table_name == "address":
            return "id"
        if table_name == "email":
            return "email_address"
        if table_name == "payment":
            return "cardNo"
        else:
            return "phoneNo"

    @staticmethod
    def get_through_two_tables(start, pk, to):
        pk_name = AccountResource.get_pk(start)
        sql = "SELECT * FROM contacts." + to + " where accountId = (select accountId from contacts." + \
            start+" where " + pk_name + "=%s)"
        print(sql)
        conn = AccountResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=pk)
        result = cur.fetchall()

        return result

    @staticmethod
    def put(tableName, parameterDict):
        pk_name = AccountResource.get_pk(start)
        sql = "SELECT * FROM contacts." + to + " where accountId = (select accountId from contacts." + \
              start + " where " + pk_name + "=%s)"
        print(sql)
        conn = AccountResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=pk)
        result = cur.fetchall()

        return result