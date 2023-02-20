# RUN THIS FILE WITH python test.py read_student
# os.environ['SECRET_KEY']
from myPackage import db,app
import sys
from myPackage.models import Student, Subject

# create database
def create_db():
	with app.app_context():
		# you will have instance folder with site.db inside
		db.create_all()

# -------------------------- CRUD OPERATIONS --------------------------
# Create operation
def create_student():
	with app.app_context():
		student = Student(name='merna',age=26,username='mernamamdouh2', email='mernamamdouh2@gmail.com', password='123')
		student2 = Student(name='mamdouh',age=62,username='mamdouhmounir', email='mamdouhmounir@gmail.com', password='456')
		db.session.add(student2)
		db.session.commit()
  
# Read operation
def read_student():
	with app.app_context():
		student = Student.query.first()
		print(f"student is {student.username}")
		for subject in student.subjects:
			print(f"subject : {subject.name}")   

# Join queries
def read_join():
	with app.app_context():
		query = db.session.query(
			Subject,
			Student
			)\
			.join(Student, Subject.student_id == Student.id)\
			.filter(Student.email == "mernamamdouh2@gmail.com")\
			.order_by(Subject.id.asc())\
			.all()

		for record in query:
			print(f"id : {record.Subject.id}")
			print(f"name : {record.Subject.name}")
			print(f"content : {record.Subject.content}")
			print(f"Student email : {record.Student.email}\n")
        
# Update operation
def update_student():
	with app.app_context():
		student = Student.query.filter_by(username="mamdouhmounir").first()
		student.password = '$2b$12$R3LWqFUKzawaWKaPNPp1wetUF.pp67lcnYhXQD6nW8EmqMivh44WK'
		db.session.commit()
    
# Delete operation
def delete_student():
    with app.app_context():
        student = Student.query.filter_by(name='mamdouh').first()
        std = Student.query.all()
        db.session.delete(std)
        db.session.commit()
        
             
# Create operation
def create_subject():
	with app.app_context():
		student1 = Student.query.first()
		student2 = Student.query.offset(1).limit(1).first()
		# subject1 = Subject(name='HTML', content='html', duration=60, student_id=student1.id)
		# subject2 = Subject(name='CSS', content='css', duration=40, student_id=student2.id)
		subject1 = Subject(name='JAVA SCRIPT', content='java script', duration=120, student_id=student1.id)
		subject2 = Subject(name='BOOTSTRAP', content='bootstrap', duration=30, student_id=student2.id)
		db.session.add(subject1)
		db.session.add(subject2)
		db.session.commit()

# Read operation
def read_student_subject():
    with app.app_context():
        student = Student.query.first()
        print(student.subjects)
        
# Read operation       
def read_subject():
    with app.app_context():
        subject = Subject.query.first()
        print(subject)
        print(subject.student_id)
        
# Delete operation
def delete_subject():
    with app.app_context():
        #subject = Subject.query.filter_by(name='HTML').first()
        sub = Subject.query.filter_by(name='mamdouh').first()
        db.session.delete(sub)
        db.session.commit()
        
        
# snippet to allow us to run funcs from terminal with "python test.py print_func"
if __name__ == '__main__':
	globals()[sys.argv[1]]()