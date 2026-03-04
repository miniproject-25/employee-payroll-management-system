from flask import Flask, render_template, request

app = Flask(__name__)

# Temporary employee database
employees = {
    "101": {"name": "Ramesh", "salary": 30000, "password": "1234"},
    "102": {"name": "Sita", "salary": 35000, "password": "1234"}
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/admin')
def admin_login():
    return render_template('admin_login.html')

@app.route('/employee')
def employee_login():
    return render_template('employee_login.html')

@app.route('/admin_dashboard', methods=['POST'])
def admin_dashboard():
    username = request.form['username']
    password = request.form['password']

    if username == "admin" and password == "admin123":
        return render_template("admin_dashboard.html", employees=employees)
    else:
        return "Invalid admin login"

@app.route('/employee_dashboard', methods=['POST'])
def employee_dashboard():
    emp_id = request.form['emp_id']
    password = request.form['password']

    if emp_id in employees and employees[emp_id]["password"] == password:
        return render_template(
            "employee_dashboard.html",
            emp_id=emp_id,
            name=employees[emp_id]["name"],
            salary=employees[emp_id]["salary"]
        )
    else:
        return "Invalid employee login"

@app.route('/payslip/<emp_id>')
def payslip(emp_id):

    employee = employees[emp_id]

    bonus = 2000
    tax = 1000
    net_salary = employee["salary"] + bonus - tax

    return render_template(
        "payslip.html",
        name=employee["name"],
        salary=employee["salary"],
        bonus=bonus,
        tax=tax,
        net_salary=net_salary
    )

if __name__ == "__main__":
    app.run(debug=True)
