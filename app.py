from flask import Flask, render_template, request, redirect, url_for
from models import db, Employee

app = Flask(__name__)
app.config.from_pyfile("config.py")
db.init_app(app)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        new_employee = Employee(name=name, email=email)
        db.session.add(new_employee)
        db.session.commit()
        return redirect(url_for("home"))

    employees = Employee.query.all()
    return render_template("index.html", employees=employees)

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    employee = Employee.query.get(id)
    if request.method == "POST":
        employee.name = request.form["name"]
        employee.email = request.form["email"]
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("update.html", employee=employee)

@app.route("/delete/<int:id>")
def delete(id):
    employee = Employee.query.get(id)
    db.session.delete(employee)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
