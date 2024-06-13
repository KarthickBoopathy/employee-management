from flask import Flask, request, jsonify
import db_config
from db_entities import EmployeeDetails
from employee_details_service import create_employee, fetch_all_employees, fetch_employee_by_id, delete_employee_by_id, \
    update_employee_designation

app = Flask(__name__)

@app.route('/health')
def health_check():
    return "Status : UP"

@app.route("/addEmployee", methods=['POST'])
def addNewEmployee():
    data = request.args
    employee_request_data = EmployeeDetails(
        first_name=data["first_name"],
        last_name=data["last_name"],
        email=data["email"],
        experience=int(data["experience"]),
        designation=data["designation"]
    )
    create_employee(employee_details=employee_request_data)
    return "Employee Added Successfully"

@app.route("/getAllEmployees", methods=['GET'])
def getAllEmployees():
    return jsonify(fetch_all_employees())

@app.route("/getEmployeeById", methods=['POST'])
def getEmployeesById():
    emp_id = request.args['emp_id']
    return jsonify(fetch_employee_by_id(emp_id))

@app.route("/updateEmployee", methods=['PUT'])
def updateEmployees():
    emp_id = request.args["emp_id"]
    designation = request.args["designation"]
    return jsonify(update_employee_designation(emp_id, designation))

@app.route("/deleteEmployeeById", methods=["DELETE"])
def deleteEmployee():
    emp_id = request.args["emp_id"]
    delete_employee_by_id(emp_id)
    return "Employee Deleted Successfully"

if __name__ == '__main__':
    with app.app_context():
        db_config.db_init(app)

    app.run(host="127.0.0.1", port=8081)

