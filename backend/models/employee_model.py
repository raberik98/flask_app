from ..extensions import db

class Employee(db.Model):
    __tablename__ = 'employees'

    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer)
    role = db.Column(db.String(255))


    @staticmethod
    def get_permission(uid):
        """
        A static method that gets' the permission of the user by it's user id (uid).

        Parameter:
        uid (int): The uid of the user, likely received from a JWT token.

        Returns:
        string: This method can return the following permissions:
            - quest (minimal permission for temporary registered users)
            - office (wider range of permission to access appropriate company data, like data about employees)
            - admin (almost full access)
            - storage (permission to access storage related data)
            - none (only has access to public resources)
        """
        return 'office'

    def __repr__(self):
        return f'ID: {self.pid} Name: {self.name}, Age: {self.age}, Role: {self.role}'