

---

### **Project Structure**
```
student_management/
│
├── static/
│   ├── css/
│   │   └── style.css      # CSS for styling
│   └── js/
│       └── script.js      # Optional JS for interactivity
├── templates/
│   ├── base.html          # Base template for common layout
│   ├── admin/
│   │   ├── dashboard.html # Admin dashboard
│   │   ├── students.html  # Admin view of students
│   └── student/
│       ├── register.html  # Student registration form
│       ├── profile.html   # Student profile page
├── app.py                 # Main application file
├── models.py              # Database models
├── forms.py               # WTForms for user inputs
└── database.db            # SQLite database
```

---

### **Step 1: Install Dependencies**
Install the required Python libraries:
```bash
pip install flask flask-wtf flask-sqlalchemy flask-bcrypt
```

---

### **Step 2: `models.py`**
Define the database models for Admin and Student.
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    course = db.Column(db.String(100), nullable=False)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
```

---

### **Step 3: `app.py`**
Set up routes for admin and student functionality.
```python
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, Student, Admin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

@app.route('/')
def home():
    return render_template('base.html')

# Student Routes
@app.route('/student/register', methods=['GET', 'POST'])
def student_register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        course = request.form['course']
        new_student = Student(name=name, email=email, age=age, course=course)
        db.session.add(new_student)
        db.session.commit()
        flash("Registration Successful!")
        return redirect(url_for('home'))
    return render_template('student/register.html')

@app.route('/student/profile/<int:student_id>')
def student_profile(student_id):
    student = Student.query.get(student_id)
    return render_template('student/profile.html', student=student)

# Admin Routes
@app.route('/admin/dashboard')
def admin_dashboard():
    students = Student.query.all()
    return render_template('admin/dashboard.html', students=students)

@app.route('/admin/delete/<int:student_id>')
def delete_student(student_id):
    student = Student.query.get(student_id)
    db.session.delete(student)
    db.session.commit()
    flash("Student Deleted!")
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/update/<int:student_id>', methods=['GET', 'POST'])
def update_student(student_id):
    student = Student.query.get(student_id)
    if request.method == 'POST':
        student.name = request.form['name']
        student.email = request.form['email']
        student.age = request.form['age']
        student.course = request.form['course']
        db.session.commit()
        flash("Student Updated!")
        return redirect(url_for('admin_dashboard'))
    return render_template('admin/update.html', student=student)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

---

### **Step 4: HTML Templates**

#### **`base.html` (Layout Template)**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Student Management System</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <header>
        <h1>Welcome to Student Management System</h1>
        <nav>
            <a href="/">Home</a>
            <a href="/student/register">Register</a>
            <a href="/admin/dashboard">Admin Dashboard</a>
        </nav>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

#### **`register.html` (Student Registration Form)**
```html
{% extends 'base.html' %}
{% block content %}
<h2>Register as a Student</h2>
<form method="POST" action="/student/register">
    <label>Name:</label>
    <input type="text" name="name" required>
    <label>Email:</label>
    <input type="email" name="email" required>
    <label>Age:</label>
    <input type="number" name="age" required>
    <label>Course:</label>
    <input type="text" name="course" required>
    <button type="submit">Register</button>
</form>
{% endblock %}
```

#### **`dashboard.html` (Admin Dashboard)**
```html
{% extends 'base.html' %}
{% block content %}
<h2>Admin Dashboard</h2>
<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Age</th>
            <th>Course</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        {% for student in students %}
        <tr>
            <td>{{ student.id }}</td>
            <td>{{ student.name }}</td>
            <td>{{ student.email }}</td>
            <td>{{ student.age }}</td>
            <td>{{ student.course }}</td>
            <td>
                <a href="/admin/update/{{ student.id }}">Update</a>
                <a href="/admin/delete/{{ student.id }}">Delete</a>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% endblock %}
```

---

### **Step 5: CSS Styling (`static/css/style.css`)**
```css
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
}

header {
    background: #333;
    color: #fff;
    padding: 10px 20px;
    text-align: center;
}

nav a {
    color: #fff;
    margin: 0 10px;
    text-decoration: none;
}

main {
    padding: 20px;
}

table {
    width: 100%;
    border-collapse: collapse;
}

table th, table td {
    border: 1px solid #ddd;
    padding: 10px;
    text-align: left;
}
```

---
