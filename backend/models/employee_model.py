from ..extensions import db
from datetime import datetime, timezone
import uuid

class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)  # Unique employee ID, auto-incremented
    name = db.Column(db.String(255), nullable=False)  # Employee name
    gender = db.Column(db.Boolean, nullable=False)  # Gender (Male, Female)
    position = db.Column(db.String(255))  # Employee's job title or position
    contract_type = db.Column(db.String(50))  # Employment type (e.g., Full-time, Part-time, Contractor)
    email = db.Column(db.String(255), unique=True, nullable=False)  # Employee email address
    phone_number = db.Column(db.String(20))  # Employee phone number
    date_joined = db.Column(db.Date)  # Date when the employee joined the company
    date_of_birth = db.Column(db.Date)  # Employee's date of birth
    nationality = db.Column(db.String(100))  # Employee's nationality
    address = db.Column(db.Text)  # Employee's full address
    emergency_contact_name = db.Column(db.String(255))  # Name of the emergency contact
    emergency_contact_phone = db.Column(db.String(20))  # Phone number of the emergency contact
    emergency_contact_relationship = db.Column(db.String(50))  # Relationship with the emergency contact
    salary = db.Column(db.Numeric(12, 2))  # Employee's salary, up to 999,999,999.99
    salary_currency = db.Column(db.String(3), default='EUR')  # Salary currency ISO 4217 standard
    vacation_balance = db.Column(db.Integer, default=0)  # Remaining vacation days balance
    warnings = db.Column(db.Integer, default=0)  # Number of warnings the employee has received
    photo = db.Column(db.Text)  # Employee photo link to an S3 bucket URL
    permission_level = db.Column(db.SmallInteger, nullable=False)  # Employee permission level (0-6)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))  # Record creation timestamp
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))  # Record update timestamp
    status_active = db.Column(db.Boolean, default=False)  # The status can be active = true or inactive = false

    def to_dict(self):
        """Convert Employee object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'position': self.position,
            'contract_type': self.contract_type,
            'email': self.email,
            'phone_number': self.phone_number,
            'date_joined': self.date_joined.isoformat() if self.date_joined else None,
            'date_of_birth': self.date_of_birth.isoformat() if self.date_of_birth else None,
            'nationality': self.nationality,
            'address': self.address,
            'emergency_contact_name': self.emergency_contact_name,
            'emergency_contact_phone': self.emergency_contact_phone,
            'emergency_contact_relationship': self.emergency_contact_relationship,
            'salary': float(self.salary) if self.salary else None,  # Convert numeric to float for JSON compatibility
            'salary_currency': self.salary_currency,
            'vacation_balance': self.vacation_balance,
            'warnings': self.warnings,
            'photo': self.photo,
            'permission_level': self.permission_level,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'status_active': self.status_active
        }

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
        return f'ID: {self.id} Name: {self.name} Role: {self.position}'