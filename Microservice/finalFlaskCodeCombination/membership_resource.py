import pymysql
import os


class MembershipResource:

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
    def get_membership_by_emailID(key):
        sql = "SELECT * FROM customerDB.membership WHERE emailID=%s"
        conn = MembershipResource.get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

    @staticmethod
    def delete_membership_by_emailID(key):
        sql = "DELETE FROM customerDB.membership WHERE emailID=%s"
        conn = MembershipResource.get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

    @staticmethod
    def create_membership(membership):
        placeholder = ", ".join(["%s"] * len(membership))
        sql = "INSERT INTO customerDB.membership({columns}) VALUES ({values})".format(
            columns=",".join(membership.keys()),
            values=placeholder)
        conn = MembershipResource.get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, list(membership.values()))
        result = cur.fetchone()

        return result

    @staticmethod
    def update_membership(membership):
        sql = "UPDATE customerDB.membersip SET emailID=%s valid_by=%s"
        conn = MembershipResource.get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, [membership["emailID"],
                                membership["valid_by"]])
        result = cur.fetchone()

        return result
