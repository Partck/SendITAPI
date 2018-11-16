"""Unique identifier library."""
import uuid
from SendITapp.db_config import init_db


class UserModel(object):
    """This class does User CRUD operations."""
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

        cur.execute("""INSERT INTO Users_table (userid, username, name,
                     email, role, phone, password) VALUES
                     (%s, %s, %s, %s, %s, %s, %s)""", (userid, self.username,
                        self.name, self.email,
                    self.role, self.phone, self.password))
        self.db.commit()
        return True

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
        cur.execute("""SELECT ((userid, name, username,
                     phone, role, email)
                      FROM Parcels_table WHERE userid = %s""", (id, ))
        row = cur.fetchone()
        conn.close()
        return row