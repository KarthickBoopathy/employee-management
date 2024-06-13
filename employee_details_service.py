from db_config import db, engine
from db_entities import EmployeeDetails
from dto import EmployeeDetailsDto

def create_employee(employee_details: EmployeeDetails):
    db.session.add(employee_details)
    db.session.commit()


def fetch_all_employees():
    data = db.session.query(EmployeeDetails).all()
    result = []
    for each in data:
        elem = EmployeeDetailsDto(
            id=each.id,
            first_name=each.first_name,
            last_name=each.last_name,
            email=each.email,
            experience=each.experience,
            designation=each.designation,
        )
        result.append(elem)
    return result


def fetch_employee_by_id(emp_id: int):
    data = (db.session.query(EmployeeDetails).filter(EmployeeDetails.id == emp_id)).first()
    return EmployeeDetailsDto(
        id=data.id,
        first_name=data.first_name,
        last_name=data.last_name,
        email=data.email,
        experience=data.experience,
        designation=data.designation,
    )

def update_employee_designation(emp_id: str, designation : str):
    employee = EmployeeDetails.query.get_or_404(emp_id)
    employee.designation = designation
    db.session.commit()
    data =  db.session.query(EmployeeDetails).filter(EmployeeDetails.id == emp_id).first()
    return EmployeeDetailsDto(
        id=data.id,
        first_name=data.first_name,
        last_name=data.last_name,
        email=data.email,
        experience=data.experience,
        designation=data.designation,
    )

def delete_employee_by_id(emp_id: int):
    employee = EmployeeDetails.query.get_or_404(emp_id)
    db.session.delete(employee)
    db.session.commit()
