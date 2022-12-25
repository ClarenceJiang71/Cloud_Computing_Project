import pymysql
import os


class AccountResource:

    def __int__(self):
        pass

    @staticmethod
    def get_connection():
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
    def get_account_by_emailID(key):
        sql = "SELECT * FROM customerDB.account WHERE emailID=%s"
        conn = AccountResource.get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

    @staticmethod
    def delete_account_by_emailID(key):
        sql = "DELETE FROM customerDB.account WHERE emailID=%s"
        conn = AccountResource.get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

    @staticmethod
    def create_account(account):
        placeholder = ", ".join(["%s"] * len(account))
        sql = "INSERT INTO customerDB.account({columns}) VALUES ({values})".format(columns=",".join(account.keys()),
                                                                                   values=placeholder)
        conn = AccountResource.get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, list(account.values()))
        result = cur.fetchone()

        return result

    @staticmethod
    def update_account(account):
        sql = "UPDATE customerDB.account SET emailID=%s password=%s"
        conn = AccountResource.get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, [account["emailID"],
                                account["password"]])
        result = cur.fetchone()

        return result
