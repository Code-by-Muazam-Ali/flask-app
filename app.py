from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import StudentForm

# Initialize app
app = Flask(__name__)
app.config['SECRET_KEY'] = '5f0c1a87d57e99d9b1c42aa8b706a3b2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///firstapp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.permanent_session_lifetime = 3600  # 1 hour

db = SQLAlchemy(app)

# Student model
class Student(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    """Home page: show and create students. No authentication required."""
    form = StudentForm()
    if form.validate_on_submit():
        student = Student(
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            email=form.email.data,
            phone=form.phone.data
        )
        db.session.add(student)
        db.session.commit()
        flash("Student added successfully!", "success")
        return redirect(url_for('hello_world'))

    allStudents = Student.query.all()
    return render_template('index.html', allStudents=allStudents, form=form)


@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update_student(sno):
    """Update an existing student."""
    student = Student.query.get_or_404(sno)
    form = StudentForm(obj=student)
    if form.validate_on_submit():
        student.firstname = form.firstname.data
        student.lastname = form.lastname.data
        student.email = form.email.data
        student.phone = form.phone.data
        db.session.commit()
        flash('Student updated successfully.', 'success')
        return redirect(url_for('hello_world'))
    return render_template('update.html', form=form, student=student)


@app.route('/delete/<int:sno>', methods=['GET','POST'])
def delete_student(sno):
    """Delete a student. GET will perform delete for compatibility with current template links.
    Consider changing to POST with a confirmation form for production.
    """
    student = Student.query.get_or_404(sno)
    db.session.delete(student)
    db.session.commit()
    flash('Student deleted.', 'info')
    return redirect(url_for('hello_world'))
# 404 Error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

# 500 Error handler
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500


if __name__ == '__main__':
    # Ensure the database tables exist and start the development server.
    with app.app_context():
        db.create_all()
    app.run(debug=True)

if __name__ == '__main__':
    with app.app_context():  # <--- Enter application context
        db.create_all()      # Create tables if they don't exist
    app.run(debug=True)