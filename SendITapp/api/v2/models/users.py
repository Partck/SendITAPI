"""Unique identifier library."""
from passlib.hash import pbkdf2_sha256 as sha256
import uuid
from SendITapp.db_config import init_db
import psycopg2


class UserModel(object):
    """This class does User CRUD operations."""
    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)



    def create_user(self, username, name, email, role, phone, password):
        """Allow the admin to create a user."""
        self.db = init_db()
        self.username = username
        self.name = name
        self.role = role
        self.email = email
        self.phone = phone
        self.password = password
        conn = self.db
        cur = conn.cursor()
        userid = str(uuid.uuid4())

        try:
            cur.execute("""INSERT INTO Users_table (userid, username, name,
                        email, role, phone, password) VALUES
                        (%s, %s, %s, %s, %s, %s, %s)""", (userid, self.username,
                        self.name, self.email,
                        self.role, self.phone, self.password))
            self.db.commit()
            cur.close()
            return True
        except (Exception, psycopg2.DatabaseError):
            return "Check you email or password"
        finally:
            if conn is not None:
                conn.close()

    
    def get_all(self):
        """This method returns all users in the system."""
        self.db = init_db()
        conn = self.db
        cur = conn.cursor()
        cur.execute("""SELECT (userid, name, username,
                     phone, role, email) FROM Users_table""")
        rows = cur.fetchall()
        conn.close()
        return rows

    
    def get_user(self, userid):
        """Get one user."""
        self.db = init_db()
        conn = self.db
        cur = conn.cursor()
        cur.execute("""SELECT (userid, name, username,
                     phone, role, email) FROM Users_table WHERE userid = %s""", (userid, ))
        row = cur.fetchall()
        conn.close()
        return row

    def user_login(self, email):
        self.db = init_db()
        conn = self.db
        cur = conn.cursor()
        cur.execute("""SELECT (userid, name, username,
                     phone, role, email) FROM Users_table WHERE
                     email = %s""", (email, ))
        row = cur.fetchall()
        conn.close()
        return row