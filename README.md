# flask_lab_iti
flask_lab_iti

- create virtual env
- install flask
- install dotenv for environment variables
- create .env file

- Create layout.html page with bootstrap enabled
- Add Navigataion bar to layout.html content
- Pass Navigation bar items to layout.html
- display navigation bar items using jinja2

- create / route
- create home.html
- write any html tags in home.html
- write any css in a css file and apply it to home.html

- create /about route
- create about.html
- write any html tags in about.html
- write any css in a css file and apply it to about.html

- install wtforms

> Using layout.html as your base do the following :
	- create a registration page for students with validation :
		- fields are :
			- username, email, password, confirm_password
		- check if data is valid , keep asking for valid data if not
		- if validated , flash registration success and redirect to login

	- create a login page for students with validation , redirect to home if validated
		- fields are :
			- username, password
		- check if data is valid , keep asking for valid data if not
		- if validated , flash login success and redirect to home

> Create database.py :
    - install sqlalchemy
    - create Student and Subject Tables
    - use registration form to insert new students into db
    - create subjects related to a student using python and print them
    - use login form to check if username and password exist or not

BONUS:
    - create "/subjects" route 
    - the route has a form to insert subjects for a student with a certain user_id
    
    
- install flask bcrypt (pip install flask-bcrypt)

> Registration :
	- hash passwords before inserting them into db
	- check for existing unique records before inserting

> Login :
	- pip install flask-login
	- using login manager , log in the user
	- if user is logged in (is_authenticated) 
		redirect to homepage if user tries to acces register/login routes
	- if user is logged in remove register and login nav items
	- if user is logged in display logout nav item with /logout as functionality
	- set users bp to register and login , automating the prefix assignment    
