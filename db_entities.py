from db_config import db


class EmployeeDetails(db.Model):
    __tablename__ = 'employee_details'
    # __table_args__ = {'schema' : f"{db_schema}"}

    id = db.Column(db.BigInteger, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    experience = db.Column(db.BigInteger)
    designation = db.Column(db.String(255))

