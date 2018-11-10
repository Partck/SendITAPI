"""Unique identifier library."""
import uuid

class UserModel(object):
    '''This class does User CRUD operations.
    '''
    user_data = []

    def create_user(self, username, name, email, role, phone, password ):
        '''This method allows the admin to create a user'''

        self.username = username
        self.name = name
        self.role = role
        self.email = email
        self.phone = phone
        self.password = password

        # id1 = str(uuid.uuid4().int)
        id1 = "4"

        payload = {"userid": str(id1), "username": self.username,
        "name": self.name, "email": self.email, "role": self.role,
        "phone": self.phone, "password": self.password}

        UserModel.user_data.append(payload)

    def get_all(self):
        """Create users."""
        return UserModel.user_data

    def get_user(self, userid):
        for user in UserModel.user_data:
            if user['userid'] == userid:
                return user
            return False

