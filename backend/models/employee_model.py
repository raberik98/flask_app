from ..extensions import db

class Employee(db.Model):
    __tablename__ = 'employees'

    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer)
    role = db.Column(db.String(255))

    def __repr__(self):
        return f'ID: {self.pid} Name: {self.name}, Age: {self.age}, Role: {self.role}'