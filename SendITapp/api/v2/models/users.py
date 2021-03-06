"""Unique identifier library."""
from werkzeug.security import generate_password_hash
import uuid
from SendITapp.db_config import DbConfig
import psycopg2
from psycopg2.extras import RealDictCursor
from flask_jwt_extended import get_jwt_identity


class UserModel(object):
    """This class does User CRUD operations."""

    def __init__(self):
        self.conn = DbConfig()
        self.db = self.conn.init_db()
        self.cursor = self.db.cursor(cursor_factory=RealDictCursor)
        self.user = get_jwt_identity()

    def create_user(self,data):
        """Allow the admin to create a user."""
        self.username = data["username"]
        self.name = data["name"]
        self.role = data["role"]
        self.email = data["email"]
        self.phone = data["phone"]
        self.password =data["password"]
        userid = str(uuid.uuid4())

        self.cursor.execute("""INSERT INTO Users_table (userid, username, name,
        email, role, phone, password) VALUES (%s, %s, %s, %s, %s, %s, %s)""", 
        (userid, self.username, self.name, self.email, self.role, self.phone, self.password))
        self.db.commit()
        self.cursor.execute("""SELECT userid, name, username,
                    phone, role, email FROM Users_table WHERE userid = %s""", (userid, ))
        row = self.cursor.fetchone()
        
        return row
      
    def get_all(self):
        """This method returns all users in the system."""

        self.cursor.execute("""SELECT userid, name, username,
                     phone, role, email FROM Users_table""")
        rows = self.cursor.fetchall()
        self.db.close()
        return rows
        
        
        
    
    def get_user(self, userid):
        """Get one user."""
        self.cursor.execute("""SELECT userid, name, username,
                     phone, role, email FROM Users_table WHERE userid = %s""", (userid, ))
        row = self.cursor.fetchone()
        self.db.close()
        return row

    def user_details(self, email):
        """Get one user."""
        self.cursor.execute("""SELECT userid, name, username,
                     phone, role, email, password FROM Users_table WHERE email = %s""", (email, ))
        row = self.cursor.fetchone()
        self.db.close()
        return row
    
    
    def get_userid(self, email):
        """Get one user."""
        self.cursor.execute("""SELECT userid, name, username,
                     phone, role, email FROM Users_table WHERE email = %s""", (email, ))
        row = self.cursor.fetchone()
        self.db.close()
        return row