import pymysql


class MembershipResource:

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
