from myPackage import * 
from flask import render_template, url_for, redirect, flash, Blueprint, session
from myPackage.forms import RegistrationForm, LoginForm, SubjectForm
from myPackage.models import Student, Subject
from flask import request
from test import create_db
from flask_login import login_user, current_user, logout_user, login_required
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

# blueprint
users = Blueprint(
	'users',
	__name__,
	url_prefix='/users'
)

menu={
        'Home': "/home",
        'About': "/about",
        'Registration': "/user/register",
        'Login': "/user/login",
        'Subject': "/subject/add",
        'Logout':"/logout"
    }


# home routing
@app.route('/')
@app.route('/home')
def home():
    result = [
        {"student":"merna",
        "grade":"30",
        "year":1997},
        {"student":"mariam",
        "grade":"20",
        "year":1996},
        {"student":"sara",
        "grade":"50",
        "year":1995},
        ]
    
    create_db()   
    return render_template('home.html', result = result,title="Home Page", menu=menu)


# about routing
@app.route('/about')
@login_required
def about():
	return render_template('about.html', title ="About page", menu=menu)

# redirect function
@app.route('/redirect')
def redirectFun():
    return redirect(url_for('home'))


@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Registration Successful. You can now log in. {form.username.data} , {form.password.data}", "success"')
        with app.app_context():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf8')
            new_student=Student(name=form.name.data, age=form.age.data, username=form.username.data, email=form.email.data, password=hashed_password)
            db.session.add(new_student)
            db.session.commit()
        flash(f"Registration Successful {form.username.data}", "success")
        return redirect(url_for('login'))
            
    return render_template('register.html', title='Registration Page', form=form, menu=menu)


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()

    if form.validate_on_submit():        
        student = Student.query.filter_by(username=form.username.data).first()
        # if user exists , check his password
        if student and bcrypt.check_password_hash(student.password,form.password.data):
            login_user(student)
            flash(f"Login Successful {student.username}", "success")
            return redirect(url_for('home'))
        else:
            flash(f"Incorrect username or password. Please try again.", "danger")
            return render_template('login.html', title='Login Page', form=form, menu=menu)
        
    return render_template('login.html', title='Login Page', form=form, menu=menu)
        

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))


@app.route('/subject/add', methods=['GET', 'POST'])
def subject_add():
    form = SubjectForm()
    if form.validate_on_submit():
        # session['student_id'] = Student.id
        # current_user = Student.query.filter_by(id=session['id']).first()
        subject = Subject(name=form.name.data, content=form.content.data, duration=form.duration.data, student_id=form.student_id.data)
        db.session.add(subject)
        db.session.commit()
        flash('Subject added successfully!')
        return redirect(url_for('home'))
    
    return render_template('subjectAdd.html', form=form, menu=menu, title="Add Subject Page")
